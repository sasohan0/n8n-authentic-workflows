# 🎥 Automated Long-Form YouTube Agent

> **A production-grade n8n architecture for generating 10-minute documentary-style videos on autopilot.**

## 📖 Executive Summary
Most "YouTube Automation" workflows rely on simple black-box tools that output generic, repetitive content. This module uses a **Component-Based Architecture** to mimic a real production studio. It treats the script, voice, and visuals as separate assembly lines, merging them programmatically for broadcast-quality results.

**Key Features:**
* **Scene-by-Scene Granularity:** The AI generates a structured storyboard, not just a block of text.
* **Parallel Processing:** Generates audio and visuals simultaneously to reduce runtime.
* **Asset Management:** Automatically manages file storage (S3 or Local) to prevent link rot.

---

## 🏗️ System Architecture

### The "Assembly Line" Logic
Unlike simple linear workflows, this agent uses a loop to process specific scenes, ensuring the image matches the exact sentence being spoken.

```mermaid
graph TD
    A[Start / Scheduler] --> B{AI Brain (GPT-4o/Gemini)};
    B -->|Generates JSON Storyboard| C[Scene Loop];
    
    subgraph "Parallel Production Factory"
    C --> D[Track A: Audio Engine];
    C --> E[Track B: Visual Engine];
    D -->|Generate Voiceover| F[Save Audio Asset];
    E -->|Generate Flux/SDXL Image| G[Save Image Asset];
    end
    
    F --> H[Aggregator];
    G --> H;
    H -->|Timeline Data| I[Video Renderer (Python/API)];
    I --> J[YouTube Upload];

## ⚖️ Architecture Comparison

Choose the workflow that fits your budget and technical capability.

| Feature | 🚀 Pro Architecture (Cloud) | 💻 Local Architecture (Free) |
| :--- | :--- | :--- |
| **Best For** | Agencies, "Cash Cow" Channels, High Quality | Developers, Students, Experimentation |
| **Orchestrator** | n8n Cloud or Self-Hosted | **Self-Hosted n8n Only** (Required) |
| **Scripting Model** | OpenAI GPT-4o | Google Gemini 1.5 Flash (Free) |
| **Voice Engine** | **ElevenLabs** (Human-like Emotion) | **Google Gemini Audio** (Standard) |
| **Visual Engine** | **Replicate: Flux.1 Pro** (Photorealistic) | **Hugging Face: SDXL** (High Quality) |
| **Video Rendering** | **Creatomate/Shotstack API** | **Local Python Script** (MoviePy) |
| **Asset Storage** | AWS S3 / Supabase | Local Hard Drive |
| **Est. Cost** | ~$4.00 - $6.00 per video | **$0.00** (Uses your hardware) |

---

## 🚀 Option A: The Pro Workflow (Cloud API)

This version uses premium APIs to achieve "Human-Level" quality that is undetectable as AI.

### 📥 Installation
1.  **[Download pro_workflow.json](./pro_workflow.json)**
2.  Import the file into your n8n instance.

### 🔑 Configuration
You need to set up credentials for the following services in n8n:
* **OpenAI:** For script generation.
* **ElevenLabs:** For voice synthesis.
* **Replicate:** For image generation (Model: `black-forest-labs/flux-1.1-pro`).
* **AWS S3:** For hosting the temporary assets.
* **Creatomate:** For rendering the final `.mp4`.

### 💡 Pro Tip
> If the workflow times out on "Image Generation," increase the `Limit` on the **Wait Node** or check your Replicate API spending limit.

---

## 💻 Option B: The Local Workflow (Zero Cost)

This version runs entirely on your machine using free tiers and local Python processing. **Note: You must be running n8n locally (Docker/npm/Pinokio).**

### 📥 Installation
1.  **[Download local_workflow.json](./local_workflow.json)**
2.  Import the file into your n8n instance.

### ⚙️ Python Environment Setup
Since n8n cannot natively render video locally, we use a Python script.

1.  **Install Dependencies:**
    Open your terminal/command prompt and run:
    ```bash
    pip install moviepy
    ```
    *(Note: You must have [FFmpeg](https://ffmpeg.org/download.html) installed on your system path).*

2.  **Setup the Script:**
    * Navigate to the `scripts/` folder in this repo.
    * Open `video_editor.py`.
    * **CRITICAL:** Edit the `ASSET_DIR` variable on Line 5 to match the folder where n8n saves files on your computer (e.g., `C:/Users/You/n8n_assets/`).

3.  **Configure n8n:**
    * Open the imported workflow.
    * Open the **"Save Image"** and **"Save Audio"** nodes.
    * Ensure the `File Name` path matches the folder you set in the Python script.

---

## 🔧 Troubleshooting

**Q: The Local Workflow says "Permission Denied" on the Python node.**
**A:** Ensure your n8n instance has read/write access to the folder you specified in `ASSET_DIR`. If using Docker, you must mount the volume.

**Q: The video has no sound.**
**A:** Check the `video_editor.py` script. Ensure `img_clip.set_audio(audio_clip)` is executing correctly. Some versions of MoviePy require `ffmpeg` updates.

**Q: The Pro workflow costs too much.**
**A:** Swap the **Replicate (Flux)** node for **OpenAI (DALL-E 2)** or **Stability AI** to reduce image costs by 50%.