# GTM Engineering Internship Assignment  
### Submitted by Gauri

---

## Overview

Built a lightweight GTM workflow for CAMX exhibitors focused on lead generation, personalized outreach, and a simple dashboard for lead review.

The goal was to collect company data, enrich it with useful business details, generate relevant first lines for cold emails, and present the final output in an easy-to-use format.

---

## Workflow

1. Tested exhibitor data scraping using Python  
2. Structured a clean company dataset  
3. Added enrichment fields:
   - Website  
   - LinkedIn discovery link  
   - Industry  
   - Outreach status  

4. Generated personalized first lines using company-specific business signals such as materials, composites, and manufacturing relevance.

5. Exported the final outreach-ready sheet.

6. Built a lightweight Streamlit dashboard for reviewing leads and outputs.

---

## Files Included

- `scraper.py` – initial scraping workflow  
- `enrich.py` – data enrichment  
- `firstline.py` – personalized line generation  
- `app.py` – Streamlit dashboard  
- `final_output.csv` – final output dataset  

---

## Deliverables

### Google Sheet  
[Open Google Sheet](https://docs.google.com/spreadsheets/d/1HRlhmWB-ESkJpkKfbDcJQsihmtlYVHcvSgOmC7ZOiv4/edit?usp=sharing)

### Loom Video  
[Watch Loom Walkthrough](https://drive.google.com/file/d/1mEBaVNznJaWyHNSb71zKUayWtHvGjyPH/view?usp=sharing)

### Streamlit Dashboard  


---

## Key Thought Process

I approached this as a practical GTM problem, not only a coding task.

The priority was to build a usable workflow that balances:

- execution speed  
- clean structured data  
- personalization quality  
- simple usability  
- clear final output

---

## If Given More Time

- Dynamic browser scraping  
- Google Sheets API sync  
- Deeper company enrichment  
- Multiple outreach variants  
- CRM integration  
- Advanced dashboard analytics  

---

## Tech Used

Python, Pandas, Requests, Streamlit, Google Sheets

---

## Final Note

This project was built to demonstrate practical problem solving at the intersection of automation, data, and go-to-market execution.