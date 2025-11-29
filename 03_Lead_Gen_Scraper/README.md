# 🕵️‍♂️ Lead Gen Scraper (Team & Email)

> **An intelligent agent that crawls company websites to find specific employees and generates valid corporate email addresses.**

## 📖 Executive Summary
Most lead generation tools are expensive black boxes. This agent reverses the process: it visits a target company's homepage, intelligently navigates to their "Team" or "About" page, extracts real employee names, and uses an algorithmic permutation engine (Python) to generate valid email candidates (e.g., `first.last@company.com`).

**Key Features:**
* **Smart Navigation:** Uses AI to identify the correct "Team" URL from a homepage's navigation menu.
* **HTML Parsing:** Extracts names and job titles from messy HTML structures.
* **Email Permutation:** Generates 30+ common corporate email formats for each name.
* **MX Validation:** (Local Version) Checks if the company domain actually accepts emails.

---

## 🏗️ System Architecture

```mermaid
graph TD
    A[Input: Company Domain] --> B[Homepage Crawler];
    B --> C{AI Navigator};
    C -->|Finds /team or /about| D[Team Page Scraper];
    
    D --> E[Name Extractor];
    E --> F[Python Permutation Engine];
    F -->|Generates Candidates| G[Email Validator];
    
    G --> H[Final Lead List (CSV/Sheet)];
```

---

## ⚖️ Architecture Comparison

| Feature | 🚀 Pro Architecture (Cloud) | 💻 Local Architecture (Free) |
| :--- | :--- | :--- |
| **Best For** | High-volume sales teams | Individual researchers/Developers |
| **Scraping Engine** | **ZenRows / ScrapingBee API** (Bypasses Captchas) | **n8n HTTP Request** (Basic) |
| **Navigation AI** | **GPT-4o** (High reasoning) | **Gemini 1.5 Flash** (Free) |
| **Email Discovery** | **Hunter.io / Snov.io API** (Verified Database) | **Python Permutator + DNS Check** |
| **Validation** | **ZeroBounce / NeverBounce** | **Regex + MX Record Lookup** |
| **Est. Cost** | ~$30/mo (API costs) | **$0.00** |

---

## 🚀 Option A: The Pro Workflow (Hunter.io Integration)

This version uses professional APIs to guarantee high-quality data and avoid IP bans.

### 📥 Installation
1.  **[Download pro_workflow.json](./pro_workflow.json)**
2.  Import into n8n.
3.  **Requirements:**
    * **ZenRows API Key** (or any scraping proxy)
    * **Hunter.io API Key** (For email finding)
    * **OpenAI API Key**

---

## 💻 Option B: The Local Workflow (Zero Cost)

This version uses your local machine to scrape, guess, and validate. **Note:** Validation is limited to "Syntax" and "Domain Existence" to avoid getting your IP blacklisted by SMTP servers.

### 📥 Installation
1.  **[Download local_workflow.json](./local_workflow.json)**
2.  Import into n8n.

### ⚙️ Python Setup (The Email Engine)
This script generates email permutations (john.d@, j.doe@) and checks if the domain has valid MX records.

1.  **Install Dependencies:**
    ```bash
    pip install dnspython
    ```

2.  **Setup Scripts:**
    * Ensure `email_permutator.py` is in the `scripts/` folder.
    * **Note:** This script requires an active internet connection to perform DNS lookups.

3.  **Configure n8n:**
    * Open the **"Execute Python"** node.
    * Ensure the path points to your `scripts/email_permutator.py`.

---

## 🔧 Troubleshooting

**Q: The scraper can't find the Team page.**
**A:** Some websites use complex JavaScript frameworks (React/Vue) that basic HTTP requests can't read. In the Local version, this is a limitation. The Pro version uses ZenRows which handles this.

**Q: The Python script fails on DNS lookup.**
**A:** Ensure you have `dnspython` installed (`pip install dnspython`). If you are behind a corporate firewall, DNS queries might be blocked.