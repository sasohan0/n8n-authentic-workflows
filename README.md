# 🤖 Authentic n8n AI Automation Workflows

![n8n Version](https://img.shields.io/badge/n8n-1.0%2B-orange?style=flat-square) ![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square) ![Status](https://img.shields.io/badge/status-Active-green?style=flat-square)

> **Professional-grade automation architectures for AI Engineers.** > This repository contains structured, production-ready workflows for n8n, separated into "Pro" (Cloud API) and "Local" (Zero-Cost) architectures.

---

## 🎯 Philosophy: "Authentic" Automation
Most AI automation tutorials rely on "Black Box" all-in-one tools. This repository focuses on **Component-Based Architecture**. 

We break down complex tasks (like video generation) into an assembly line of specialized AI agents. This approach ensures:
* **Granular Control:** You own every step of the process.
* **Scalability:** Swap out models (e.g., GPT-4o to Claude 3.5) without breaking the system.
* **Cost Efficiency:** Choose between high-performance APIs or local compute power.

---

## 📂 Module Directory

| Module ID | Agent Name | Primary Use Case | Architecture Types |
| :--- | :--- | :--- | :--- |
| **01** | **[YouTube Long-Form Agent](./01_YouTube_Automation/README.md)** | Generates 10-minute documentary-style videos with scene-by-scene coherence. | ✅ Cloud (API)<br>✅ Local (Python) |
| **02** | **[Social Media Omni-Agent](./02_Social_Media_Agent/README.md)** | Repurposes 1 URL into LinkedIn, X, and Instagram posts. | ✅ Cloud (Buffer)<br>✅ Local (Python/Pillow) |
| **03** | **[Lead Gen Scraper](./03_Lead_Gen_Scraper/README.md)** | Intelligent Team Page crawler & Email Permutator. | ✅ Cloud (Hunter)<br>✅ Local (Python DNS) |

---

## 🚀 Getting Started

### Prerequisites
To use these workflows, you need an instance of **n8n**.
1.  **Cloud:** [n8n.io](https://n8n.io) (Easiest for Pro Workflows).
2.  **Self-Hosted:** Docker or [Pinokio](https://pinokio.computer/) (Required for Local/Python Workflows).

### Usage Guide
1.  Navigate to the specific **Module Folder** (linked in the table above).
2.  Read the module's `README.md` for specific API requirements.
3.  Download the `.json` workflow file.
4.  **Import to n8n:** Open n8n Editor → Top Right Menu → Import from File.

---

## 🛠️ Tech Stack
* **Orchestration:** [n8n](https://n8n.io/)
* **LLMs:** OpenAI (GPT-4o), Google Gemini 1.5 Flash
* **Vision:** Replicate (Flux.1), Hugging Face (SDXL)
* **Audio:** ElevenLabs, OpenAI TTS
* **Compute:** Python 3.10 (MoviePy, Pandas)

---

## 🤝 Contribution
This is an open-source project. If you find a bug or want to add a "Local" alternative to a "Pro" workflow:
1.  Fork the repo.
2.  Create a branch: `git checkout -b feature/amazing-feature`.
3.  Commit changes: `git commit -m 'Add amazing feature'`.
4.  Push to branch: `git push origin feature/amazing-feature`.
5.  Open a Pull Request.

---
*Maintained by Solih Ahmad Sohan*