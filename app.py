# app.py

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from resume_parser import extract_resume_text
from matcher import analyze_resume
from genai_suggestions import generate_suggestions


st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# HEADER
st.title("🚀 AI Resume Analyzer")
st.markdown(
"""
AI-powered resume evaluation tool that analyzes how well your resume matches a job description.

✔ ATS Score  
✔ Semantic Similarity  
✔ Skill Gap Detection  
✔ Resume Section Analysis  
✔ AI Resume Improvement Suggestions
"""
)

st.markdown("---")


# INPUT SECTION
st.subheader("📄 Upload Resume & Job Description")

resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
jd_text = st.text_area("Paste Job Description")


if resume_file and jd_text:

    with st.spinner("🔍 AI analyzing your resume..."):
        resume_text = extract_resume_text(resume_file)
        result = analyze_resume(resume_text, jd_text)

    ats_score = result["ats_score"]
    semantic_score = round(result["semantic_score"], 2)
    overall_score = int((ats_score + semantic_score) / 2)

    st.markdown("---")

    # DASHBOARD METRICS
    st.subheader("📊 Resume Match Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ATS Match Score", f"{ats_score}%")

    with col2:
        st.metric("Semantic Similarity", f"{semantic_score}%")

    with col3:
        st.metric("Overall Resume Fit", f"{overall_score}%")

    st.markdown("")

    # SCORE PROGRESS
    st.write("### ATS Score Progress")
    st.progress(int(ats_score))

    st.write("### Semantic Similarity Progress")
    st.progress(int(semantic_score))

    st.markdown("---")

    # GAUGE CHART
    st.subheader("🎯 AI Resume Fit Score")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=overall_score,
        title={'text': "Resume Fit Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 50], 'color': "lightcoral"},
                {'range': [50, 75], 'color': "khaki"},
                {'range': [75, 100], 'color': "lightgreen"}
            ]
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # SKILLS SECTION
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🛠️ Detected Skills")

        if result["resume_skills"]:
            for skill in result["resume_skills"]:
                st.success(skill)
        else:
            st.warning("No known skills detected.")

    with col2:
        st.subheader("⚠️ Missing Skills")

        missing_skills = result["missing_skills"]

        if missing_skills:
            for skill in missing_skills:
                st.error(skill)

            st.info("Add these skills to Skills, Projects, or Experience sections.")
        else:
            st.success("All required skills detected!")

    st.markdown("---")

    # SKILL DISTRIBUTION CHART
    st.subheader("📊 Skill Match Overview")

    skills_data = {
        "Type": ["Detected"] * len(result["resume_skills"]) +
                ["Missing"] * len(result["missing_skills"]),
        "Skill": result["resume_skills"] + result["missing_skills"]
    }

    df_skills = pd.DataFrame(skills_data)

    if not df_skills.empty:
        fig = px.histogram(df_skills, x="Type", color="Type")
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # MISSING SKILLS GRAPH
    if result["missing_skills"]:
        st.subheader("⚠️ Important Missing Skills")

        df_missing = pd.DataFrame({
            "Skill": result["missing_skills"],
            "Importance": [1]*len(result["missing_skills"])
        })

        fig = px.bar(df_missing, x="Skill", y="Importance")
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # RESUME SECTION ANALYSIS
    st.subheader("📑 Resume Section Strength")

    sections = {
        "Skills": len(result["resume_skills"]),
        "Experience": resume_text.lower().count("experience"),
        "Projects": resume_text.lower().count("project"),
        "Education": resume_text.lower().count("education")
    }

    df_sections = pd.DataFrame(
        list(sections.items()),
        columns=["Section", "Score"]
    )

    fig = px.bar(df_sections, x="Section", y="Score")

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # AI SUGGESTIONS
    st.subheader("💡 AI Resume Improvement Suggestions")

    with st.spinner("Generating AI suggestions..."):
        suggestions = generate_suggestions(resume_text, jd_text)

    st.markdown(suggestions)

    st.markdown("---")

    # FOOTER
    st.caption(
        "Powered by NLP, semantic similarity, skill extraction, and generative AI."
    )


else:
    st.info("Please upload a resume and paste the job description to start the analysis.")