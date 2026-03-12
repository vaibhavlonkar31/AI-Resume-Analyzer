import os
from pdfminer.high_level import extract_text
import pandas as pd

# Folder containing all PDF resumes
folder = "sample_resumes"

# List to store extracted data
data = []

# Loop through all files in the folder
for file in os.listdir(folder):
    if file.endswith(".pdf"):
        # Extract text from each PDF
        text = extract_text(os.path.join(folder, file))
        data.append({"filename": file, "resume_text": text})
        print(f"Processed {file}")

# Save all extracted text to a single CSV
df = pd.DataFrame(data)
df.to_csv("all_resumes.csv", index=False)
print("All resumes saved to all_resumes.csv")