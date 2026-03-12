from groq import Groq
import os

client = Groq(api_key=os.getenv("REMOVED"))

def generate_suggestions(resume, jd):

    prompt = f"""
You are an ATS Resume Analyzer.

Your job is to compare a resume with a job description and explain the results in SIMPLE language.

Resume:
{resume}

Job Description:
{jd}

Give the output in the following format.

1️⃣ MATCHING SKILLS  
List the important skills that already match the job description.

2️⃣ MISSING SKILLS (IMPORTANT)  
Highlight the missing skills using **bold formatting**.  
Explain why these skills are important.

3️⃣ WHAT TO ADD TO THE RESUME  
Explain clearly what the candidate should add:
- Skills
- Projects
- Experience
- Certifications

4️⃣ WHAT TO REMOVE OR AVOID  
Explain what should NOT be in the resume according to the job description.

5️⃣ SIMPLE IMPROVEMENT TIPS  
Give 3–5 simple suggestions to improve ATS score.

Use simple language and short explanations.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content