import re
import spacy
import pandas as pd
import docx
from pdfminer.high_level import extract_text

# Step 1: Read resume text

# For PDF
# Read CSV containing resumes
df = pd.read_csv("C:\\Users\\VAIBHAV\\OneDrive\\Desktop\\AI Resume Analyzer\\Extract_resumes\\all_resumes.csv")  # your CSV file

# Assume your CSV has a column named "Resume_Text"
resume_texts = df["resume_text"].tolist()

parsed_data = []

for resume_text in resume_texts:
    # Skills
    skills = re.findall(r"(Skills|Technical Skills|Technologies)(.*?)(Education|Experience|Projects|$)", resume_text, re.I|re.S)
    skills_text = skills[0][1].strip() if skills else ""

    # Education
    education = re.findall(r"(Education|Qualifications|Academic Background)(.*?)(Experience|Projects|Skills|$)", resume_text, re.I|re.S)
    education_text = education[0][1].strip() if education else ""

    # Experience
    experience = re.findall(r"(Experience|Work Experience|Professional Experience)(.*?)(Education|Projects|Skills|$)", resume_text, re.I|re.S)
    experience_text = experience[0][1].strip() if experience else ""

    # Projects
    projects = re.findall(r"(Projects|Academic Projects|Personal Projects)(.*?)(Education|Experience|Skills|$)", resume_text, re.I|re.S)
    projects_text = projects[0][1].strip() if projects else ""

    parsed_data.append({
        "Skills": skills_text,
        "Education": education_text,
        "Experience": experience_text,
        "Projects": projects_text
    })


nlp = spacy.load("en_core_web_sm")

for i, resume_text in enumerate(resume_texts):
    doc = nlp(resume_text)

    # Name (first PERSON entity)
    name = None
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break

    # Email
    emails = [token.text for token in doc if token.like_email]

    # Phone
    phones = re.findall(r"\+?\d[\d -]{8,12}\d", resume_text)

    # Add to parsed_data
    parsed_data[i].update({
        "Name": name,
        "Email": ", ".join(emails),
        "Phone": ", ".join(phones)
    })


df_parsed = pd.DataFrame(parsed_data)
df_parsed.to_csv("resume_parsed_structured.csv", index=False)
print("Saved structured data to resume_parsed_structured.csv")