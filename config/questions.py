# Auto Job Applier LinkedIn


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "/home/har5ha/Desktop/resume/resumes/Harsha_Yellela_AI-Automation-Engineer.pdf"

# Resume directory
RESUMES_DIR = "/home/har5ha/Desktop/resume/resumes"

# Map search terms (lowercase) → resume filename. Falls back to default_resume_path if no match.
resume_by_role = {
    "ai engineer":               "Harsha_Yellela_AI-Automation-Engineer.pdf",
    "ai automation engineer":    "Harsha_Yellela_AI-Automation-Engineer.pdf",
    "llm engineer":              "Harsha_Yellela_AI-Automation-Engineer.pdf",
    "ai agent developer":        "Harsha_Yellela_AI-Automation-Engineer.pdf",
    "ml engineer":               "Harsha_Yellela_ML-Engineer.pdf",
    "machine learning engineer": "Harsha_Yellela_ML-Engineer.pdf",
    "backend engineer":          "Harsha_Yellela_SDE.pdf",
    "software engineer":         "Harsha_Yellela_SDE.pdf",
}

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "3"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "Yes"              # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://har5ha.in"                                    # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/har5ha-7663"            # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Non-citizen allowed to work for any employer"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 110000           # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 0                 # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 0                    # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "AI & ML Engineer | Python, AWS, LLMs, Multi-Agent Systems" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
AI and ML Engineer with 3+ years of experience building scalable AI automation pipelines, multi-agent systems, and cloud-native backends.
MS in Computer Science (3.6 GPA) from Lawrence Technological University.
Built CrewAI + LangChain MCP agents on AWS EKS, achieving 70% reduction in manual workflow time.
Fine-tuned LLMs with QLoRA, developed MLOps pipelines on SageMaker, and deployed 94 serverless Lambda functions.
Previously at Infor India, developed production tools for global clients including Ferrari and Boeing.
Authorized to work in the US (F-1 OPT). Seeking AI Automation, ML Engineering, or Backend Engineering roles.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Manager,

I am excited to apply for this position. As an AI and ML Engineer with 3+ years of experience building production AI systems and automation pipelines, I am eager to bring my skills in LLMs, multi-agent systems, and cloud-native backends to your team.

As a Graduate Research Assistant at Lawrence Technological University, I built and deployed multi-agent AI systems using CrewAI and LangChain MCP on AWS EKS, reducing manual workflow time by 70%. I fine-tuned LLMs using QLoRA, built 8-microservice MLOps platforms on SageMaker, and developed RAG pipelines with OpenSearch Serverless. Previously at Infor India, I delivered production tools for global clients including Ferrari and Boeing, integrating AWS Lambda and API Gateway for enterprise-scale ERP automation.

I hold an MS in Computer Science (3.6 GPA) from Lawrence Technological University, specializing in AI/ML. My portfolio at har5ha.in showcases live projects in agentic AI, LLM fine-tuning, and cloud automation.

I am authorized to work in the US under F-1 OPT and will require H-1B sponsorship for long-term employment.

I would love to discuss how my experience aligns with your team's goals.

Best regards,
Harsha Vardhan Yellela
harsha.yellela@gmail.com | (248) 497-9965
linkedin.com/in/har5ha-7663 | har5ha.in
"""
##> ------ Dheeraj Deshwal : dheeraj9811 Email:dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Feature ------

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc. 
user_information_all ="""
Name: Harsha Vardhan Yellela
Email: harsha.yellela@gmail.com
Phone: (248) 497-9965
Location: Farmington Hills, MI 48335
Portfolio: https://har5ha.in
LinkedIn: https://www.linkedin.com/in/har5ha-7663
GitHub: https://github.com/HAR5HA-7663

Work Authorization: F-1 OPT (Post-Completion) — authorized to work in the US; will require H-1B sponsorship for long-term employment
Willing to Relocate: Yes
Start Date: Immediate

Education:
- MS Computer Science, Lawrence Technological University, Southfield MI — GPA 3.6/4.0, Jan 2024 – Dec 2025
- B.Tech Computer Science & Engineering, Geethanjali College, Hyderabad — GPA 7.5/10, Aug 2018 – Aug 2022

Work Experience:
- Graduate Research Assistant (Agentic AI), Lawrence Technological University (Jan 2025 – Dec 2025)
  Built multi-agent systems using CrewAI + LangChain MCP deployed on AWS EKS; achieved 70% reduction in manual workflow time; RAG with OpenSearch Serverless
- LN Technical Consultant, Infor India Pvt. Ltd. (Apr 2022 – Dec 2023)
  Developed production tools for Ferrari, Boeing, Triumph; integrated Infor ION with AWS S3, Lambda, API Gateway; containerized services with Docker
- Java Backend Apprentice, EPAM Systems (Sep 2020 – Jul 2021)
  Java 8, Spring MVC, REST APIs, CI/CD pipelines, JUnit testing

Years of Experience: 3
Desired Salary: $110,000 USD
Current CTC: $0
Notice Period: 0 days (immediate)

Skills:
- Languages: Python, Go, TypeScript, JavaScript, Java, SQL
- AI/ML: LangChain, CrewAI, LangGraph, QLoRA fine-tuning, MLOps, SageMaker, RAG, OpenSearch
- Backend: FastAPI, Flask, Gin (Go), Express.js, REST APIs
- Cloud (AWS): Lambda, ECS Fargate, EKS, EC2, SageMaker, Bedrock, S3, DynamoDB, API Gateway
- DevOps: Docker, Kubernetes, Jenkins, GitHub Actions, Terraform, Prometheus, Grafana
- ML Frameworks: TensorFlow/Keras, PyTorch, HuggingFace Transformers, scikit-learn
- LLMs: GPT-4, Gemini, DeepSeek, Qwen, LLaMA, Claude
- Databases: PostgreSQL, MongoDB, Redis, Qdrant (vector)

Salary Expectation: $100,000 - $130,000 (negotiable)
"""
##<
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "Lawrence Technological University" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "7"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = False        # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = False   # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







