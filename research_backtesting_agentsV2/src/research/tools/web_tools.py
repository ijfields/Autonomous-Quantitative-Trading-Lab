import os
import httpx
import asyncio
import logging
import numpy as np
from typing import List
from dotenv import load_dotenv

# Docling
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, AcceleratorOptions, AcceleratorDevice

# Local Embeddings (CPU)
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from pathlib import Path
load_dotenv(Path(__file__).parent.parent.parent.parent / ".env")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("quant_tools")

SEARXNG_PORT = os.getenv("SEARXNG_PORT", "8081")
SEARXNG_URL = os.getenv("SEARXNG_BASE_URL", f"http://localhost:{SEARXNG_PORT}/")

# --- 1. CONFIGURATION ---

def _init_docling():
    """CPU-Optimized PDF Reader"""
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True
    pipeline_options.accelerator_options = AcceleratorOptions(num_threads=4, device=AcceleratorDevice.CPU)
    return DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)})

def _init_embedder():
    """Load a tiny, fast embedding model (MiniLM) for local filtering"""
    logger.info("🧠 Loading Local Embedding Model (all-MiniLM-L6-v2)...")
    return SentenceTransformer('all-MiniLM-L6-v2', device='cpu')

# Load models once (Singleton pattern)
docling_converter = _init_docling()
embedder = _init_embedder()

# --- 2. LOCAL RAG LOGIC ---

class MemoryRAG:
    """
    Splits a document into chunks, finds the 'trading logic', and returns only 
    the relevant parts to save tokens.
    """
    def __init__(self, full_markdown: str):
        self.chunks = self._chunk_text(full_markdown)
    
    def _chunk_text(self, text: str, chunk_size: int = 1000) -> List[str]:
        """
        Simple semantic chunker. Splits by double newlines to preserve paragraphs.
        """
        raw_chunks = text.split("\n\n")
        merged_chunks = []
        current_chunk = ""
        
        for p in raw_chunks:
            if len(current_chunk) + len(p) < chunk_size:
                current_chunk += p + "\n\n"
            else:
                merged_chunks.append(current_chunk.strip())
                current_chunk = p + "\n\n"
        if current_chunk:
            merged_chunks.append(current_chunk.strip())
            
        return [c for c in merged_chunks if len(c) > 50] # Filter tiny noise

    def retrieve_best_context(self, query: str, top_k: int = 5) -> str:
        """
        Finds the top_k chunks that match the query.
        """
        if not self.chunks: return ""
        
        # 1. Embed the chunks (Local CPU)
        chunk_embeddings = embedder.encode(self.chunks)
        
        # 2. Embed the query
        query_embedding = embedder.encode([query])
        
        # 3. Calculate Similarity
        similarities = cosine_similarity(query_embedding, chunk_embeddings)[0]
        
        # 4. Get Top K indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # 5. Re-order by appearance in text (to keep logical flow)
        top_indices = sorted(top_indices)
        
        best_chunks = [self.chunks[i] for i in top_indices]
        return "\n\n...[Snippet]...\n\n".join(best_chunks)

# --- 3. TOOLS ---

# Global Client for Connection Pooling
_client = httpx.AsyncClient(timeout=15.0)

async def _searxng_request(query: str, engines: str, max_results: int) -> str:
    url = f"{SEARXNG_URL.rstrip('/')}/search"
    params = {"q": query, "format": "json", "engines": engines, "language": "en-US"}
    
    for attempt in range(3):
        try:
            resp = await _client.get(url, params=params)
            resp.raise_for_status() # Raise on 4xx/5xx
            
            data = resp.json()
            results = data.get("results", [])[:max_results]
            if not results: return "No results."
            return "\n".join([f"- {r.get('title')} ({r.get('url')}): {r.get('content')}" for r in results])
            
        except Exception as e:
            if attempt == 2:
                return f"Search Error: {e}"
            await asyncio.sleep(1) # Backoff
    return "Search Failed"

async def search_academic_papers(query: str) -> str:
    """Searches ArXiv/Google Scholar."""
    return await _searxng_request(query, "arxiv,google_scholar", 4)

async def search_github_code(query: str) -> str:
    """Searches GitHub."""
    return await _searxng_request(f"site:github.com {query}", "google", 4)

async def search_general_web(query: str) -> str:
    """General Search."""
    # Use Brave (Server friendly) + Google + Bing. 
    # Removed DuckDuckGo because it CAPTCHAs servers.
    return await _searxng_request(query, "brave,google,bing", 6)

async def read_url_content(url: str) -> str:
    """
    Downloads URL -> Docling -> Local RAG -> Top 3k Tokens.
    This respects the Gemma 15k TPM limit.
    """
    logger.info(f"📖 Reading & Compressing: {url}")
    try:
        # 1. Download & Parse (Heavy CPU)
        result = await asyncio.to_thread(docling_converter.convert, url)
        full_text = result.document.export_to_markdown()
        
        # 2. RAG Filtering (Save Tokens!)
        # We assume the user wants trading logic
        rag = MemoryRAG(full_text)
        
        # We ask specifically for the "Meat" of the strategy
        query = "mathematical formulas trading strategy logic entry exit rules backtest results"
        
        # Retrieve only the top 6 chunks (approx 3000-4000 tokens)
        compressed_text = rag.retrieve_best_context(query, top_k=6)
        
        header = f"--- SMART EXTRACT FROM {url} ---\n(Irrelevant sections removed to save tokens)\n\n"
        return header + compressed_text
        
    except Exception as e:
        logger.error(f"Read Error: {e}")
        return f"Failed to read {url}: {e}"

# Cleanup hook (though Python usually cleans up)
async def close_client():
    await _client.aclose()