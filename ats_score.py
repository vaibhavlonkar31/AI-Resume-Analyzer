# ats_score.py
def calculate_ats(resume_skills, jd_skills, resume_text, semantic_score):
    """
    Hybrid ATS scoring:
    - Skill Match (40%)
    - Semantic Similarity (40%)
    - Keyword Density (20%)
    """
    # Skill match
    if not jd_skills:
        skill_match_score = 0
    else:
        skill_match_score = len(set(resume_skills).intersection(set(jd_skills))) / len(jd_skills)

    # Keyword density: count occurrences of JD skills in resume
    resume_text_lower = resume_text.lower()
    keyword_count = sum(resume_text_lower.count(skill.lower()) for skill in jd_skills)
    max_possible = len(jd_skills) * 3  # assume max 3 mentions per skill
    keyword_density_score = min(keyword_count / max_possible, 1.0)  # cap at 100%

    # Weighted hybrid score
    final_score = (skill_match_score * 40) + (semantic_score * 0.4) + (keyword_density_score * 20)
    return round(final_score, 2)