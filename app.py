import streamlit as st
import pandas as pd
from src.extractor import extract_text
from src.matcher import ResumeScreeningEngine

st.set_page_config(page_title="AI Resume Screening System", page_icon="📄", layout="wide")

st.title("📄 AI-Powered Resume Screening & Ranking System")
st.caption("Upload multiple candidate resumes and compare them against a Job Description.")

@st.cache_resource
def get_engine():
    return ResumeScreeningEngine()

engine = get_engine()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Job Description (JD)")
    jd_input = st.text_area(
        "Paste the Job Description here:",
        height=250,
        placeholder="e.g., Looking for a Python Developer proficient in Django, FastAPI, SQL, REST APIs, and Docker..."
    )

with col2:
    st.subheader("2. Upload Resumes")
    uploaded_files = st.file_uploader(
        "Upload candidate resumes (PDF, DOCX, TXT):",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True
    )

if st.button("🚀 Screen & Rank Resumes", type="primary"):
    if not jd_input.strip():
        st.warning("Please provide a Job Description first.")
    elif not uploaded_files:
        st.warning("Please upload at least one resume.")
    else:
        with st.spinner("Extracting text and calculating relevance..."):
            parsed_resumes = []
            for file in uploaded_files:
                file_bytes = file.read()
                extracted_text = extract_text(file.name, file_bytes)
                if extracted_text:
                    parsed_resumes.append({
                        "name": file.name,
                        "text": extracted_text
                    })

            if not parsed_resumes:
                st.error("Could not extract readable text from the uploaded files.")
            else:
                ranking_df = engine.rank_candidates(jd_input, parsed_resumes)

                st.success("Screening Complete!")
                st.subheader("📊 Candidate Ranking Results")
                
                # Highlight styling for scores
                st.dataframe(
                    ranking_df,
                    use_container_width=True,
                    column_config={
                        "Match Score (%)": st.column_config.ProgressColumn(
                            "Match Score",
                            help="Semantic match score against the JD",
                            format="%.2f%%",
                            min_value=0,
                            max_value=100,
                        ),
                    }
                )