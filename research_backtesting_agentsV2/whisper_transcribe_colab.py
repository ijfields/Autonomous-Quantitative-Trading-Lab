# Whisper Transcription for Google Colab
# Usage: Upload to Colab, run all cells, download the .txt output
#
# Video: Moon Dev — march 12 - hack investigation, bittensor & trading competition
# Video ID: lzW2Cggl3nA
# Duration: ~215 minutes
#
# Estimated runtime on Colab T4 GPU: ~15-25 minutes with large-v3

# %% [markdown]
# ## Step 1: Install dependencies

# %%
!pip install -q openai-whisper yt-dlp

# %% [markdown]
# ## Step 2: Download audio from YouTube

# %%
import subprocess, os

VIDEO_ID = "lzW2Cggl3nA"
VIDEO_URL = f"https://www.youtube.com/watch?v={VIDEO_ID}"
AUDIO_FILE = f"{VIDEO_ID}.mp3"

if not os.path.exists(AUDIO_FILE):
    subprocess.run([
        "yt-dlp",
        "-x", "--audio-format", "mp3",
        "--audio-quality", "5",  # medium quality, smaller file
        "-o", f"{VIDEO_ID}.%(ext)s",
        VIDEO_URL
    ], check=True)
    print(f"Downloaded: {AUDIO_FILE}")
else:
    print(f"Already exists: {AUDIO_FILE}")

# %% [markdown]
# ## Step 3: Transcribe with Whisper

# %%
import whisper

# Use large-v3 for best accuracy. Alternatives:
# "medium" — faster, slightly less accurate
# "large-v3" — best quality, ~15-25 min for 3.5hr video on T4
MODEL_SIZE = "large-v3"

print(f"Loading Whisper {MODEL_SIZE}...")
model = whisper.load_model(MODEL_SIZE)

print("Transcribing (this will take a while for a 3.5hr video)...")
result = model.transcribe(
    AUDIO_FILE,
    language="en",
    verbose=True  # shows progress
)

print("Transcription complete!")

# %% [markdown]
# ## Step 4: Save output

# %%
OUTPUT_TITLE = "march 12 -  hack investigation, bittensor & trading competition"

# Save plain text (deduplicated, matches our pipeline format)
txt_path = f"{OUTPUT_TITLE}.txt"
with open(txt_path, "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        f.write(segment["text"].strip() + "\n")
print(f"Saved: {txt_path}")

# Save VTT format (timestamped, for reference)
vtt_path = f"{OUTPUT_TITLE}.en.vtt"
with open(vtt_path, "w", encoding="utf-8") as f:
    f.write("WEBVTT\n\n")
    for seg in result["segments"]:
        start = seg["start"]
        end = seg["end"]
        text = seg["text"].strip()
        sh, sm, ss = int(start//3600), int((start%3600)//60), start%60
        eh, em, es = int(end//3600), int((end%3600)//60), end%60
        f.write(f"{sh:02d}:{sm:02d}:{ss:06.3f} --> {eh:02d}:{em:02d}:{es:06.3f}\n")
        f.write(f"{text}\n\n")
print(f"Saved: {vtt_path}")

# %% [markdown]
# ## Step 5: Download files
# Run this cell, then check the Colab file browser (left sidebar) to download

# %%
from google.colab import files

files.download(txt_path)
files.download(vtt_path)
print("Done! Place both files in research_backtesting_agentsV2/")
