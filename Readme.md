# 📄 Resume Analyser

An AI-powered web app that compares a candidate's resume with a job description, calculates a match score, and identifies missing skills using ESCO skill taxonomy and spaCy PhraseMatcher.
👉 Useful for HR teams, recruiters, and job seekers to optimize resumes for specific job postings.

---

## ✨Features
- 📑 Upload Resume (PDF) and paste a Job Description (JD).
- 📊 Get a Resume Match Score (0–100%) against the JD.
- 🚫 Identify Missing Skills from the JD that aren’t present in the resume.

🖼️ Snapshots of the Analyzer:
<img width="1546" height="794" alt="image" src="https://github.com/user-attachments/assets/47856167-abca-4b24-a617-88ab22fe1737" />

## 🛠️ Technologies Used
- Python
- Streamlit (UI framework)
- SentenceTransformers (embeddings)
- spaCy + ESCO Skill Taxonomy (skill extraction)
---

## Installation

Instructions to set up locally:

```bash
git clone https://github.com/Thespideycoder/ResumeAnalyser.git
cd ResumeAnalyser
# If using virtual environment:
python ‑m venv venv
source venv/bin/activate     # on macOS/Linux
venv\Scripts\activate         # on Windows
pip install ‑r requirements.txt
```

## 📌 Future Improvements
- Support for multiple resume uploads (batch analysis).
- Screenshot-to-text JD parsing (OCR).
- Integration with LinkedIn jobs API for auto JD fetching.

