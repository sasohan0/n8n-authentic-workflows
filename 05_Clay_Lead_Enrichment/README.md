# 🚀 Automated Lead Enrichment Agent (n8n + Clay + OpenAI)

This workflow replaces the manual SDR process. It takes a domain list, enriches it with "Waterfall" data (Tech stack, Recent News, Hiring trends) using Clay, and uses GPT-4o to draft a hyper-personalized cold email.

## 🛠 Architecture
1. **Trigger:** Manual Input or Google Sheets Row.
2. **Data Engine:** Connects to **Clay API** to fetch deep company attributes.
3. **Logic Core:** **GPT-4o** analyzes the data to find a "Conversation Starter."
4. **Output:** Saves the draft to Google Sheets / Airtable.

## 📦 How to Use
1. **Import:** Download the `workflow.json` file and import it into your n8n instance.
2. **Credentials:**
   - Add your OpenAI API Key.
   - Add your Clay API Key (in the HTTP Request Header).
3. **Run:** Click "Execute" to test with the mock data.

---
*Built by Solih Ahmad Sohan. Open Sourced for the community.*
