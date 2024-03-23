import os
import random

def generate_paragraph():
    terms = [ #topics 
        "minimum wage", "worker rights", "labor unions", "employment regulations", "workplace safety standards",
        "unemployment benefits", "equal pay", "overtime regulations", "family leave policies", "discrimination laws",
        "collective bargaining", "job training programs", "employee healthcare benefits", "workplace discrimination",
        "retirement benefits", "part-time employment", "temporary worker protections", "child labor laws", 
        "workplace harassment policies", "worker's compensation", "job security", "maternity/paternity leave",
        "telecommuting policies", "flexible work arrangements", "workplace diversity initiatives",
        "workplace accommodations for disabilities", "elder care leave", "retraining programs",
        "workplace surveillance regulations", "gender equality initiatives", "employee privacy rights",
        "gig economy regulations", "workplace automation policies", "severance pay regulations", "internship regulations",
        "workplace whistleblowing protections", "employee ownership programs", "workplace wellness programs",
        "remote work policies", "outsourcing regulations", "offshoring policies", "job sharing arrangements",
        "wage theft laws", "independent contractor regulations", "career advancement opportunities"
    ]
    
    num_terms = random.randint(80, 150) #rand num btw 
    paragraph = ' '.join(random.choices(terms, k=num_terms))
    return paragraph


directory = "LabourPoliciesTask2"
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate files
for i in range(1, 201):  # 200 files
    filename = f"{i}.txt"
    filepath = os.path.join(directory, filename.replace("\\", "/"))  
    with open(filepath, "w") as file:
        paragraph = generate_paragraph()
        file.write(paragraph)
