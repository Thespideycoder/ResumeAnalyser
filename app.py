import streamlit as st
from utils.embeddings import get_embedding
from utils.generic_skills import extract_skills
from utils.parse_resume import extract_text_from_pdf
from utils.similarity import calculate_similarity
from utils.skills import get_skills
import numpy as np
from utils.visuals import coverage_gauge, skill_match_chart

st.set_page_config(page_title="Resume Analytzer", layout="wide")

st.title("📄 Resume Analyzer")

# ========== INPUT SECTION ==========
col1, col2 = st.columns(2)
with col1:
    # --- Upload Resume ---
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

with col2:
    # ---- Job Description ------
    job_description = st.text_area("Job Description here....", height=300)
    

with st.container():
    spacer1, center_col, spacer2 = st.columns([3, 1, 3])
    with center_col:
        generate_botton = st.button("🔍 Generate Match Report")

resume_text = ""
if uploaded_file:
    with open("temp_resume.pdf","wb") as f:
        f.write(uploaded_file.read())
    resume_text = extract_text_from_pdf("temp_resume.pdf")
    # st.success("Resume Uploaded")


if generate_botton:
    if not resume_text or not job_description.strip():
        st.warning("⚠️ Please upload both your resume and job description before analyzing.")
    else:
        if len(job_description.strip()) < 20:
            st.warning("⚠️ Please enter a meaningful job description.")
        else:    
            with st.spinner("Analysing results..."):
                context_score = calculate_similarity(get_embedding(resume_text),get_embedding(job_description))
                skill_score = calculate_similarity(get_embedding(' '.join(extract_skills(resume_text))), get_embedding(' '.join(extract_skills(job_description))))
                score = np.mean([context_score,skill_score])
                missing_skills, matched_skills = get_skills(job_description, resume_text)
                st.subheader("📊 Match Report")
                st.metric("Match Score", f"{score}%")
                st.subheader("🚫 Missing Skills")
                st.write(missing_skills)
                coverage_gauge(score)
                skill_match_chart(matched_skills, missing_skills)




