# Step-by-Step Guide: I Gave OpenClaw Blender Skills (The Results are INSANE)

**Source:** Riley Brown (YouTube)
**Video ID:** dxlyCPGCvy8
**Upload Date:** 2026-02-17

---

## What This Guide Covers

How to connect OpenClaw to Blender via the Blender MCP (Model Context Protocol), control 3D modeling through natural language, customize a 3D asset, export it, build a landing page, and deploy it to the web -- all without coding or Blender experience.

---

## Step 1: Install Blender and the Blender MCP Add-on

1. Download Blender from the official website and install it on your machine (Mac, Windows, or Linux).
2. Open Blender.
3. Go to **Edit > Preferences > Add-ons**.
4. Search for and install the **Blender MCP** add-on.
5. Enable the add-on by checking its checkbox.

---

## Step 2: Start the MCP Server in Blender

1. In Blender, press **N** to open the side panel.
2. Find the **Blender MCP** tab.
3. Click **Connect to MCP server** -- it runs on **port 9876** by default.
4. Confirm the server is running and listening.

---

## Step 3: Tell OpenClaw to Create a Blender Skill

1. In your OpenClaw chat (e.g., via Telegram), send a message like:
   > "Search the internet and find skills about Blender. I want you to create a Blender skill that allows you to control Blender that is downloaded on my computer via the Blender MCP. Wrap the MCP so that you can use this as a skill."
2. Wait for the agent to research, build, and confirm the skill is ready.
3. Confirm connectivity: "We are running the server on 9876. Can you tell me if you see anything?"

---

## Step 4: Test Basic 3D Scene Creation

1. Ask your agent to create a simple scene:
   > "Please make a little green field with some trees on it in Blender."
2. Verify the objects appear in Blender.
3. If everything appears gray, switch the viewport shading:
   - Click the viewport shading dropdown (top-right of 3D viewport)
   - Switch from **Solid** to **Material Preview** to see actual colors.

---

## Step 5: Import and Customize a 3D Asset

1. Purchase or download a 3D model (e.g., a .blend file from an online marketplace).
2. In Blender, go to **File > New > General** to start a fresh project.
3. Ensure the Blender MCP is still connected on port 9876.
4. Tell your agent:
   > "In my downloads, I just purchased a [model name] 3D model. Can you please load it?"
5. To customize colors, identify the layer/material name in Blender's outliner (e.g., "M4001") and tell the agent:
   > "Please make [layer name] red."
6. To add images/stickers as textures:
   - Upload the image to Google Drive or make it accessible.
   - Tell the agent to create a thin circular sheet over the target surface and apply the image as a texture.
7. To change text labels, identify the text layer and tell the agent:
   > "Layer [name] has text that says X. Instead, I want it to say Y."

---

## Step 6: Export the 3D Model for Web

1. Tell your agent:
   > "Please export this as a GLB file. We're going to use it on a website."
2. Specify the export location (e.g., Downloads folder).
3. Confirm the file was created successfully.

---

## Step 7: Build and Deploy a Landing Page

1. Tell your agent to create a landing page featuring the 3D model:
   > "Have a product called [name]. Make it $X. Make the 3D model big. I want it to spin slowly. I want to be able to click and hold and move it around."
2. The agent will generate the HTML/CSS/JS and serve it locally (e.g., localhost:8080).
3. Preview the page in your browser.
4. Deploy to the web:
   > "Please deploy it to Vercel and then send me the public link."
5. Approve the Vercel deployment when prompted.
6. Your site is now live (e.g., `your-project.vercel.app`).

---

## Key Takeaway

> "I don't know how to use Blender and I don't know how to code, but I got OpenClaw to create a skill that allows us to use Blender and then I had it put it in a website." The Blender MCP turns a complex 3D workflow into a conversational process, and the agent can even send screenshots via Telegram so you can direct the work remotely.

*Guide derived from: I Gave OpenClaw Blender Skills (The Results are INSANE).txt*
