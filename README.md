# 📄 AI Resume Screening & Ranking System

An NLP-powered application designed to automate candidate shortlisting by extracting resume text (PDF/DOCX) and scoring similarity against job descriptions using TF-IDF vectorization and Cosine Similarity.

---

## 📌 Project Overview

Manual resume parsing across hundreds of applicants is time-consuming and subjective. This system provides automated ranking through a multi-stage NLP pipeline:
1. **Document Parsing:** Extracts raw text from multi-page PDFs and DOCX files.
2. **Text Normalization:** Cleans data via tokenization, stop-word removal, and alphanumeric sanitization.
3. **Vectorization & Scoring:** Transforms resumes and job descriptions into TF-IDF term vectors and calculates cosine similarity scores.
4. **Interactive Dashboard:** Generates a ranked leaderboard with matching percentages and keyword overlap metrics.

---

## 🛠️ Tech Stack
- **Language:** Python
- **NLP & Machine Learning:** scikit-learn, NLTK
- **Document Processing:** PyPDF2 / pdfplumber, python-docx
- **Web Interface:** Streamlit
- **Data Manipulation:** pandas, numpy

---

## ⚙️ Setup & Installation

```bash
git clone [https://github.com/Sinchana-175/ai-resume-screener.git](https://github.com/Sinchana-175/ai-resume-screener.git)
cd ai-resume-screener
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
