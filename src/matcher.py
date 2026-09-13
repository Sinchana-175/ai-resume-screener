import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class ResumeScreeningEngine:
    def __init__(self):
        # Lightweight, high-accuracy semantic embedding model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def rank_candidates(self, job_description: str, resumes: list) -> pd.DataFrame:
        """
        resumes: list of dicts [{'name': 'alex_resume.pdf', 'text': '...'}]
        """
        if not resumes or not job_description.strip():
            return pd.DataFrame()

        # Generate embeddings
        jd_embedding = self.model.encode([job_description])
        resume_texts = [r['text'] for r in resumes]
        resume_embeddings = self.model.encode(resume_texts)

        # Calculate cosine similarities
        scores = cosine_similarity(jd_embedding, resume_embeddings)[0]

        results = []
        for i, resume in enumerate(resumes):
            match_percentage = round(float(scores[i]) * 100, 2)
            results.append({
                "Candidate / File Name": resume['name'],
                "Match Score (%)": match_percentage,
                "Status": "Strong Match" if match_percentage >= 70 else ("Moderate Match" if match_percentage >= 50 else "Low Match")
            })

        # Sort descending by match score
        df = pd.DataFrame(results).sort_values(by="Match Score (%)", ascending=False).reset_index(drop=True)
        df.index += 1  # 1-based ranking index
        return df