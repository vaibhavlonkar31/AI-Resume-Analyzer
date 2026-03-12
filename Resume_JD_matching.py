import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# 1. Load Resumes CSV (with proper parsing)
# -----------------------------
df_resumes = pd.read_csv(
    "resume_parsed_structured.csv",
    quotechar='"',  # handles commas inside quotes
    skipinitialspace=True
)

# Remove rows with invalid names (like 'Pandas', 'Power Distribution')
df_resumes['Name'] = df_resumes['Name'].str.strip()
df_resumes = df_resumes[df_resumes['Name'].notna()]
df_resumes = df_resumes[df_resumes['Name'] != '']

# -----------------------------
# 2. Load Job Descriptions JSON
# -----------------------------
with open("data/job_descriptions.json", "r", encoding="utf-8") as f:
    jd_data = json.load(f)

# -----------------------------
# 3. Skills List for Matching
# -----------------------------
skills_list = [
    "sql","excel","tableau","power bi","python","pandas","numpy","spark","hadoop",
    "airflow","aws redshift","c/c++","matlab","autocad","etap","power distribution",
    "pcb design","iot","microcontrollers","solidworks","catia","fea","thermodynamics",
    "quality control","labelbox","cvat","prodigy","nlp annotation","quality assurance"
]

# -----------------------------
# 4. Function to Extract Skills
# -----------------------------
def extract_skills(text):
    text = str(text).lower()
    return [skill for skill in skills_list if skill in text]

df_resumes['Resume_Skills'] = df_resumes['Skills'].apply(extract_skills)

# -----------------------------
# 5. Combine all Resume Text (for TF-IDF)
# -----------------------------
df_resumes['Resume_text_combined'] = (
    df_resumes['Skills'].fillna('') + ' ' +
    df_resumes['Education'].fillna('') + ' ' +
    df_resumes['Experience'].fillna('') + ' ' +
    df_resumes['Projects'].fillna('')
)

# -----------------------------
# 6. Section-wise Matching & Scoring
# -----------------------------
scores_list = []

for idx, resume in df_resumes.iterrows():
    resume_name = resume['Name']
    resume_skills = resume['Resume_Skills']
    resume_education = str(resume['Education']).lower()
    resume_experience = str(resume['Experience']).lower()
    resume_text = str(resume['Resume_text_combined']).lower()

    for jd in jd_data:
        jd_title = jd['job_title']
        jd_skills = [s.lower() for s in jd['skills']]
        jd_education = str(jd['education']).lower()
        jd_experience = str(jd['experience']).lower()
        jd_text = " ".join(jd['skills']) + " " + " ".join(jd['responsibilities']) + " " + jd_education + " " + jd_experience
        jd_text = jd_text.lower()

        # --- Skills Match Score ---
        matched_skills = set(resume_skills).intersection(set(jd_skills))
        skill_score = round(len(matched_skills)/len(jd_skills)*100, 2) if jd_skills else 0

        # --- Education Match Score ---
        edu_score = 100 if any(word in resume_education for word in jd_education.split()) else 0

        # --- Experience Match Score ---
        exp_score = 100 if any(word in resume_experience for word in jd_experience.split()) else 0

        # --- TF-IDF Similarity ---
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, jd_text])
        tfidf_score = round(cosine_similarity(vectors[0], vectors[1])[0][0]*100, 2) # type: ignore

        # --- Final Weighted Score ---
        final_score = round(
            skill_score*0.5 + edu_score*0.2 + exp_score*0.1 + tfidf_score*0.2, 2
        )

        # --- Save Result ---
        scores_list.append({
            "Resume_Name": resume_name,
            "JD_Title": jd_title,
            "Matched_Skills": list(matched_skills),
            "Skill_Score": skill_score,
            "Education_Score": edu_score,
            "Experience_Score": exp_score,
            "TFIDF_Score": tfidf_score,
            "Final_Score": final_score
        })

# -----------------------------
# 7. Save All Scores
# -----------------------------
df_scores = pd.DataFrame(scores_list)
df_scores.to_csv("resume_vs_all_jds_sectionwise.csv", index=False)

# -----------------------------
# 8. Best JD per Resume
# -----------------------------
best_matches = df_scores.loc[df_scores.groupby("Resume_Name")["Final_Score"].idxmax()]
best_matches.to_csv("best_jd_per_resume_bestmatch.csv", index=False)

print("✅ Matching complete! Scores saved.")