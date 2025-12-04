# 🤖 n8n AI Automation Suite: Professional Agentic Workflows

![Status](https://img.shields.io/badge/Status-Active-success) ![n8n](https://img.shields.io/badge/n8n-Automation-ff6e5c) ![Python](https://img.shields.io/badge/Python-3.10-blue) ![License](https://img.shields.io/badge/License-MIT-green)

**Enterprise-grade automation architectures for AI Engineers, Agencies, and Freelancers.**

> **The Problem:** Most automation tutorials use "Black Box" tools that don't scale.
> **Our Solution:** This repository provides "Glass Box" workflows using **n8n**. We break complex tasks (like video generation) into an assembly line of specialized AI agents. You own the code, the API keys, and the data.

---

## 📂 Production-Ready Modules

Choose your architecture: **Pro** (Cloud APIs for speed) or **Local** (Python/Ollama for privacy and zero cost).

| ID | Agent/Module Name | Business Use Case (ROI) | Architecture |
| :--- | :--- | :--- | :--- |
| **01** | **YouTube Documentary Generator** | **Content Automation:** Generates 10-minute, scene-by-scene documentary videos from a single prompt. | ✅ Cloud (API)<br>✅ Local (Python) |
| **02** | **Omni-Channel Social Agent** | **Marketing:** Repurposes 1 Blog/Video URL into formatted LinkedIn, X, and Instagram posts automatically. | ✅ Cloud (Buffer)<br>✅ Local (Pillow) |
| **03** | **B2B Lead Scraper & Enricher** | **Sales:** Crawls Team Pages, permutes emails, and verifies leads for outreach campaigns. | ✅ Cloud (Hunter)<br>✅ Local (Python DNS) |
| **04** | **Self-Healing Error Handler** | **DevOps:** Diagnoses workflow crashes and auto-fixes or alerts via Slack/Discord. | ✅ Cloud (Slack)<br>✅ Local (Discord) |

---

## 🎯 The "Authentic" Philosophy
*Why this repository is different:*

We reject "wrapper" tools. We focus on **Component-Based Architecture**.
* **Granular Control:** You own every step of the process.
* **Scalability:** Swap out models (e.g., GPT-4o to Claude 3.5) without breaking the system.
* **Cost Efficiency:** Toggle between high-performance APIs or local compute power based on client budget.

---

## 🚀 Getting Started

### Prerequisites
To use these workflows, you need an instance of **n8n**.
1.  **Cloud:** [n8n.io](https://n8n.io) (Easiest for Pro Workflows).
2.  **Self-Hosted:** Docker or Pinokio (Required for Local/Python Workflows).

### Installation Guide
1.  Navigate to the specific **Module Folder** (linked in the table above).
2.  **Read the module's `README.md`** for specific API requirements (OpenAI, Anthropic, etc.).
3.  Download the `.json` workflow file.
4.  **Import to n8n:** Open n8n Editor → Top Right Menu → *Import from File*.

---

## 🛠️ Tech Stack

* **Orchestration:** n8n
* **LLMs:** OpenAI (GPT-4o), Google Gemini 1.5 Flash, Ollama (Llama 3)
* **Vision:** Replicate (Flux.1), Hugging Face (SDXL)
* **Audio:** ElevenLabs, OpenAI TTS
* **Compute:** Python 3.10 (MoviePy, Pandas)

---

## 🤝 Contribution & Freelance
**Maintained by [Solih Ahmad Sohan](https://www.linkedin.com/in/solih-ahmad-sohan)**

This is an open-source project. If you find a bug or want to add a "Local" alternative to a "Pro" workflow:
1.  Fork the repo.
2.  Create a branch: `git checkout -b feature/amazing-feature`.
3.  Open a Pull Request.

*Looking for a custom automation for your agency? [Connect with me on LinkedIn](https://www.linkedin.com/in/solih-ahmad-sohan).*
