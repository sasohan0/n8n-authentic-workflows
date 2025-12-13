# 🚀 Automated Lead Enrichment Agent (n8n + Clay + OpenAI)

> **Stop manually researching leads.** This workflow replaces the manual SDR role by treating lead generation as an engineering problem.

![n8n](https://img.shields.io/badge/Orchestrator-n8n-orange?style=flat-square)
![Clay](https://img.shields.io/badge/Data-Clay_API-blue?style=flat-square)
![OpenAI](https://img.shields.io/badge/Intelligence-GPT4o-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=flat-square)

## 📖 Overview

Most "AI Lead Gen" tools just blast generic emails. This agent builds a **"Waterfall Enrichment"** pipeline.

It takes a raw domain, extracts deep context (Tech Stack, Recent News, Hiring Trends) via Clay, and uses a **Logic Router** to draft 100% personalized messages based on the prospect's actual technology stack.

### ✨ Key Features (v3 Update)
* **Waterfall Enrichment:** Fetches 15+ data points per company (not just email).
* **Intelligent Routing:** Automatically switches context:
    * If they use *Python* → Write about Python SDK.
    * If they use *No-Code* → Write about Integrations.
    * *Default* → Write generic value prop.
* **Error Handling Layer:** Detects missing data and logs errors to Slack/Sheets instead of breaking the pipeline.
* **Visual Zoning:** Organized with color-coded phases for easy maintenance.

---

## 🛠 Architecture

The system follows a strict "Input -> Process -> Router -> Output" logic:

1.  **Phase 1: Ingestion (Gray Zone)**
    * **Trigger:** Manual Mock Data or Google Sheets Row.
    * **Clay API:** Hits the endpoint to retrieve the "Digital Twin" of the company.
2.  **Phase 2: Intelligence (Blue Zone)**
    * **Logic Switch:** Checks `tech_stack` variable.
    * **LLM (GPT-4o):** Drafts the email using a hyper-specific prompt for that segment.
3.  **Phase 3: Output (Green Zone)**
    * **Storage:** Appends the final draft + meta-data to Google Sheets/Airtable.

---

## ⚙️ Setup Guide

### 1. Installation (n8n)
You need a running instance of n8n. You can run it for free locally using Docker.
* **[👉 Official Self-Hosting Guide (Docker)](https://docs.n8n.io/hosting/)** - *Recommended for developers.*
* **[☁️ n8n Cloud Signup](https://n8n.io/)** - *Easiest way to start if you don't want to manage servers.*

### 2. Import Workflow
1.  Download the `workflow.json` file from this folder.
2.  Open your n8n dashboard.
3.  Click **"Add Workflow"** (top right) → **"Import from File"**.

### 3. Configure Credentials
* **OpenAI:** Add your API Key in the `AI Drafter` nodes.
* **Clay API:**
    * Get your key from Clay Settings.
    * Open the `Clay Enrichment API` node → **Header Parameters**.
    * Name: `Authorization` | Value: `Bearer YOUR_CLAY_API_KEY`.
* **Google Sheets:** Authenticate your Google account in the `Save to Sheets` node.

---

## 🧪 Example Use Case (Practice Run)

**Scenario:** You are selling a **Vector Database** solution.

1.  **Input Data (Mock Node):**
    * Domain: `openai.com`
    * Tech Stack: `Python`
2.  **The Agent's Action:**
    * Detects "Python".
    * Routes to the "Python Drafter" branch.
    * **Generated Email:** *"Saw you guys are heavy on Python. Our vector DB has a native `pip install` library that handles your embeddings..."*
3.  **Alternative Input:**
    * Domain: `bubble.io`
    * Tech Stack: `No-Code`
    * **Generated Email:** *"Since you built on Bubble, you'll love our direct API integration that doesn't require backend code..."*

---

## 🤝 Contributing

This project is Open Source. I built it to help freelancers and agencies move away from manual work.

* **Found a bug?** Open an Issue.
* **Have an optimization?** Fork the repo and submit a Pull Request.
* **Want to add a new Data Provider?** Feel free to swap Clay for Apollo/PeopleDataLabs and PR it!

---

## 🔗 Connect with the Builder

I share the "Build Logs" and architecture breakdowns behind these workflows weekly.

* **👨‍💻 LinkedIn:** [Solih Ahmad Sohan](https://www.linkedin.com/in/solih-ahmad-sohan-9a741b250/) - *Daily Engineering tips.*
* **📩 Newsletter:** [The Autonomous Systems](https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7399354044802199552) - *Deep dives into my agency stack.*
* **🐦 X (Twitter):** [@sasohan0](https://x.com/sasohan0)

> *Starred this repo? Let me know on LinkedIn so I can say thanks!*
