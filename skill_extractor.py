# skill_extractor.py
import re
from fuzzywuzzy import fuzz
from skills_db import skills  # your updated skill DB

def normalize_text(text):
    """
    Lowercase, remove punctuation and extra spaces
    """
    text = text.lower()
    text = re.sub(r'[\n,.;()\-]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_skills(resume_text, skills_list=None, threshold=80):
    """
    Extract skills from resume using fuzzy matching
    """
    if skills_list is None:
        skills_list = skills

    resume_text = normalize_text(resume_text)
    detected_skills = []

    for skill in skills_list:
        skill_norm = normalize_text(skill)
        if fuzz.partial_ratio(skill_norm, resume_text) >= threshold:
            detected_skills.append(skill)

    return list(set(detected_skills))