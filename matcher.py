# matcher.py
from skill_extractor import extract_skills
from semantic_matcher import semantic_similarity
from ats_score import calculate_ats
from skills_db import skills

def analyze_resume(resume_text, jd_text):
    """
    Returns:
    - detected resume skills
    - JD skills
    - semantic similarity
    - ATS score (hybrid)
    - missing skills
    """
    # Fuzzy skill detection in resume
    resume_skills = extract_skills(resume_text)

    # Extract relevant JD skills from DB
    jd_skills = [skill for skill in skills if skill.lower() in jd_text.lower()]

    # Semantic similarity (0-100)
    semantic_score = semantic_similarity(resume_text, jd_text)

    # Hybrid ATS score
    ats_score = calculate_ats(resume_skills, jd_skills, resume_text, semantic_score)

    # Missing skills
    missing_skills = list(set(jd_skills) - set(resume_skills))

    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "semantic_score": semantic_score,
        "ats_score": ats_score,
        "missing_skills": missing_skills
    }