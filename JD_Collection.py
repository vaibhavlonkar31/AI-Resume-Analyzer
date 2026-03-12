import json
import os

# Create folder
os.makedirs("data", exist_ok=True)

job_descriptions = [

# ---------------- DATA SCIENTIST ----------------

{
"role": "Data Scientist",
"job_title": "Data Scientist",
"responsibilities": [
"Build predictive machine learning models",
"Analyze structured and unstructured datasets",
"Create visualizations and business reports"
],
"skills": ["Python","SQL","Machine Learning","TensorFlow","Power BI"],
"education": "B.Tech/M.Sc in Computer Science or Data Science",
"experience": "3+ years"
},

{
"role": "Data Scientist",
"job_title": "ML Scientist",
"responsibilities": [
"Develop statistical and ML models",
"Work with engineering teams to deploy models",
"Interpret model results"
],
"skills": ["Python","R","Statistics","Scikit-learn","SQL"],
"education": "M.Sc in Data Science or Statistics",
"experience": "3+ years"
},

{
"role": "Data Scientist",
"job_title": "AI Data Scientist",
"responsibilities": [
"Design AI algorithms",
"Work with big data platforms",
"Build deep learning models"
],
"skills": ["Python","PyTorch","Deep Learning","SQL","Spark"],
"education": "B.Tech/M.Tech in AI or CS",
"experience": "4+ years"
},

{
"role": "Data Scientist",
"job_title": "Senior Data Scientist",
"responsibilities": [
"Lead data science projects",
"Build advanced predictive models",
"Mentor junior analysts"
],
"skills": ["Python","Machine Learning","SQL","TensorFlow","Statistics"],
"education": "Masters in Data Science",
"experience": "5+ years"
},

{
"role": "Data Scientist",
"job_title": "Applied Data Scientist",
"responsibilities": [
"Translate business problems into ML solutions",
"Analyze datasets",
"Build dashboards"
],
"skills": ["Python","Pandas","SQL","Tableau","ML"],
"education": "B.Tech/M.Sc in Data Science",
"experience": "3+ years"
},

# ---------------- DATA ANALYST ----------------

{
"role": "Data Analyst",
"job_title": "Data Analyst",
"responsibilities": [
"Analyze business datasets",
"Create dashboards",
"Prepare reports"
],
"skills": ["SQL","Excel","Python","Power BI","Tableau"],
"education": "Bachelor's in Data/Business",
"experience": "2+ years"
},

{
"role": "Data Analyst",
"job_title": "Business Data Analyst",
"responsibilities": [
"Generate business insights",
"Perform statistical analysis",
"Create reports"
],
"skills": ["Excel","SQL","Power BI","Python","Statistics"],
"education": "Bachelor's in Business Analytics",
"experience": "2+ years"
},

{
"role": "Data Analyst",
"job_title": "Reporting Analyst",
"responsibilities": [
"Build dashboards",
"Automate reporting processes",
"Monitor business metrics"
],
"skills": ["Excel","Tableau","SQL","Python","Power BI"],
"education": "Bachelor's in Statistics or Analytics",
"experience": "2+ years"
},

{
"role": "Data Analyst",
"job_title": "Analytics Specialist",
"responsibilities": [
"Interpret data trends",
"Prepare visualization reports",
"Support business decisions"
],
"skills": ["SQL","Excel","Tableau","Python","Statistics"],
"education": "Bachelor's in Data Analytics",
"experience": "3+ years"
},

{
"role": "Data Analyst",
"job_title": "Junior Data Analyst",
"responsibilities": [
"Clean datasets",
"Assist senior analysts",
"Create data reports"
],
"skills": ["Excel","SQL","Python","Power BI","Data Cleaning"],
"education": "Bachelor's in Computer Science",
"experience": "1-2 years"
},

# ---------------- PYTHON DEVELOPER ----------------

{
"role": "Python Developer",
"job_title": "Python Developer",
"responsibilities": [
"Develop backend applications",
"Integrate APIs",
"Write scalable Python code"
],
"skills": ["Python","Django","Flask","REST API","SQL"],
"education": "B.Tech in Computer Science",
"experience": "2+ years"
},

{
"role": "Python Developer",
"job_title": "Backend Python Developer",
"responsibilities": [
"Develop backend services",
"Build APIs",
"Optimize performance"
],
"skills": ["Python","Flask","Django","PostgreSQL","Docker"],
"education": "B.Tech in IT",
"experience": "3+ years"
},

{
"role": "Python Developer",
"job_title": "Software Engineer (Python)",
"responsibilities": [
"Develop scalable applications",
"Write clean code",
"Maintain backend systems"
],
"skills": ["Python","FastAPI","SQL","Git","Docker"],
"education": "B.Tech in Computer Science",
"experience": "2+ years"
},

{
"role": "Python Developer",
"job_title": "Automation Python Developer",
"responsibilities": [
"Develop automation scripts",
"Optimize workflows",
"Maintain automation systems"
],
"skills": ["Python","Selenium","Automation","Linux","Git"],
"education": "Bachelor's in Computer Science",
"experience": "2+ years"
},

{
"role": "Python Developer",
"job_title": "API Developer",
"responsibilities": [
"Build REST APIs",
"Integrate microservices",
"Test backend systems"
],
"skills": ["Python","FastAPI","REST API","SQL","Docker"],
"education": "B.Tech in CS",
"experience": "3+ years"
},

# ---------------- DATA ANNOTATOR ----------------

{
"role": "Data Annotator",
"job_title": "Image Data Annotator",
"responsibilities": [
"Label image datasets",
"Ensure annotation quality",
"Support AI training datasets"
],
"skills": ["Data Labeling","Image Annotation","CVAT","Attention to Detail"],
"education": "Bachelor's degree",
"experience": "1+ years"
},

{
"role": "Data Annotator",
"job_title": "AI Data Annotator",
"responsibilities": [
"Label datasets for AI models",
"Validate annotations",
"Maintain annotation accuracy"
],
"skills": ["Annotation Tools","Data Labeling","Quality Control"],
"education": "Bachelor's degree",
"experience": "1+ years"
},

{
"role": "Data Annotator",
"job_title": "Text Data Annotator",
"responsibilities": [
"Annotate text datasets",
"Tag NLP data",
"Ensure annotation guidelines"
],
"skills": ["Text Annotation","NLP Basics","Data Labeling"],
"education": "Bachelor's degree",
"experience": "1+ years"
},

{
"role": "Data Annotator",
"job_title": "ML Data Annotator",
"responsibilities": [
"Label ML datasets",
"Review annotations",
"Prepare datasets"
],
"skills": ["Annotation Tools","ML Dataset Prep","Quality Assurance"],
"education": "Bachelor's degree",
"experience": "1+ years"
},

{
"role": "Data Annotator",
"job_title": "Dataset Labeling Specialist",
"responsibilities": [
"Label and categorize datasets",
"Maintain annotation quality",
"Support AI training teams"
],
"skills": ["Data Labeling","Annotation Tools","Data Quality"],
"education": "Bachelor's degree",
"experience": "1+ years"
},

# ---------------- DATA ENGINEER ----------------

{
"role": "Data Engineer",
"job_title": "Data Engineer",
"responsibilities": [
"Build data pipelines",
"Manage large datasets",
"Optimize data infrastructure"
],
"skills": ["Python","SQL","Spark","ETL","AWS"],
"education": "B.Tech in Computer Science",
"experience": "3+ years"
},

{
"role": "Data Engineer",
"job_title": "Big Data Engineer",
"responsibilities": [
"Work with big data tools",
"Develop ETL pipelines",
"Manage distributed systems"
],
"skills": ["Hadoop","Spark","Python","SQL","Kafka"],
"education": "B.Tech in IT",
"experience": "3+ years"
},

{
"role": "Data Engineer",
"job_title": "Cloud Data Engineer",
"responsibilities": [
"Build cloud data pipelines",
"Manage cloud databases",
"Optimize storage"
],
"skills": ["AWS","Python","SQL","ETL","Spark"],
"education": "B.Tech in CS",
"experience": "3+ years"
},

{
"role": "Data Engineer",
"job_title": "ETL Engineer",
"responsibilities": [
"Develop ETL processes",
"Clean and transform datasets",
"Maintain data warehouse"
],
"skills": ["ETL","SQL","Python","Airflow","Data Warehousing"],
"education": "Bachelor's in Computer Science",
"experience": "2+ years"
},

{
"role": "Data Engineer",
"job_title": "Analytics Data Engineer",
"responsibilities": [
"Prepare analytics datasets",
"Build pipelines",
"Ensure data quality"
],
"skills": ["Python","SQL","Spark","Airflow","BigQuery"],
"education": "B.Tech in CS",
"experience": "3+ years"
},

# ---------------- ELECTRICAL ENGINEER ----------------

{
"role": "Electrical Engineer",
"job_title": "Electrical Design Engineer",
"responsibilities": [
"Design electrical systems",
"Create circuit diagrams",
"Test electrical components"
],
"skills": ["Circuit Design","MATLAB","AutoCAD","Power Systems"],
"education": "B.Tech in Electrical Engineering",
"experience": "2+ years"
},

{
"role": "Electrical Engineer",
"job_title": "Power Systems Engineer",
"responsibilities": [
"Maintain power systems",
"Analyze electrical loads",
"Ensure system safety"
],
"skills": ["Power Systems","MATLAB","Electrical Design"],
"education": "B.Tech in Electrical",
"experience": "3+ years"
},

{
"role": "Electrical Engineer",
"job_title": "Control Systems Engineer",
"responsibilities": [
"Develop control systems",
"Test automation systems",
"Maintain electrical controls"
],
"skills": ["PLC","Control Systems","MATLAB","Automation"],
"education": "B.Tech Electrical",
"experience": "3+ years"
},

{
"role": "Electrical Engineer",
"job_title": "Electrical Maintenance Engineer",
"responsibilities": [
"Maintain electrical equipment",
"Troubleshoot systems",
"Ensure operational efficiency"
],
"skills": ["Electrical Maintenance","Troubleshooting","PLC"],
"education": "B.Tech Electrical",
"experience": "2+ years"
},

{
"role": "Electrical Engineer",
"job_title": "Electronics Engineer",
"responsibilities": [
"Design electronic circuits",
"Test electronic components",
"Develop prototypes"
],
"skills": ["Electronics","Circuit Design","PCB","Embedded Systems"],
"education": "B.Tech Electronics",
"experience": "2+ years"
},

# ---------------- MECHANICAL ENGINEER ----------------

{
"role": "Mechanical Engineer",
"job_title": "Mechanical Design Engineer",
"responsibilities": [
"Design mechanical systems",
"Create CAD models",
"Test prototypes"
],
"skills": ["AutoCAD","SolidWorks","Mechanical Design","Thermodynamics"],
"education": "B.Tech Mechanical",
"experience": "2+ years"
},

{
"role": "Mechanical Engineer",
"job_title": "Production Engineer",
"responsibilities": [
"Manage manufacturing processes",
"Improve production efficiency",
"Maintain production equipment"
],
"skills": ["Production Planning","Lean Manufacturing","CAD"],
"education": "B.Tech Mechanical",
"experience": "2+ years"
},

{
"role": "Mechanical Engineer",
"job_title": "Maintenance Engineer",
"responsibilities": [
"Maintain machinery",
"Troubleshoot mechanical failures",
"Ensure operational efficiency"
],
"skills": ["Mechanical Maintenance","Troubleshooting","Hydraulics"],
"education": "B.Tech Mechanical",
"experience": "2+ years"
},

{
"role": "Mechanical Engineer",
"job_title": "Thermal Engineer",
"responsibilities": [
"Analyze thermal systems",
"Design cooling systems",
"Perform simulations"
],
"skills": ["Thermodynamics","ANSYS","Heat Transfer"],
"education": "B.Tech Mechanical",
"experience": "3+ years"
},

{
"role": "Mechanical Engineer",
"job_title": "Automotive Engineer",
"responsibilities": [
"Design vehicle components",
"Test automotive systems",
"Improve vehicle performance"
],
"skills": ["Automotive Engineering","CAD","Vehicle Design"],
"education": "B.Tech Mechanical",
"experience": "3+ years"
}

]

# Save JSON
with open("data/job_descriptions.json", "w") as f:
    json.dump(job_descriptions, f, indent=4)

print("job_descriptions.json created successfully in data/ folder")