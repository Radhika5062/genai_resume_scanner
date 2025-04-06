from langchain_core.prompts import PromptTemplate
from logger import logging

class CreatePrompt:
    def __init__(self):
        pass

    def get_job_alignment_prompt(self, job_description, resume_text):
        logging.info("Entered get_job_alignment_prompt")
        prompt =  prompt = f"""

            Give me answer in the below steps

            Ensure that you only evaluate the resume text with respect to the job description provided.
            You are a highly skilled resume reviewer with 20 years of experience in talent acquisition in fields of Data Science, Machine Learning, Deep Learning and Generative AI.
            Your task is to evaluate whether the candidate's resume aligns with the provided job descriotion in these roles.
            Your review should follow these steps:

            ### Step 1: Job resume alignement scoring
            - This section should first include a percentage in bold and then from next line the description should follow. 
            - Analyse the job description andResume provided below.
            - Calculate a percentage match score based on:
                - Technical skill match: Check for alignment with required tools, coding languages and techniques.
                - Relevant experience: Does the candidate have the required experience for the job role?
                - Keywords: Does the resume include necessary technical and role-specifig keywords?
                - Problem solving approach: Is the candidate familiar with problem solving techniques used in this role like data wrangling, feature engineering, model evaluation? There are a lot of other problem solving techniques and I have only included a few examples.
                - Provide the match percentage (0% - 100%) that reflects how well the resume aligns with the job description.
            
            ### Step 2: Resume sections analysis
            - Break down the analysis into key sections of the resume.
                - Experience: Analyse how the candidate's previous work experience aligns with the given job description. Does the candidate have experience with machine learning models, data pipelines or AI systems?
                - Skills: Check for the presence of relevant programming languages, tools and frameworks such as but not limited to Python, R, Tensorflow, Pytorch, SQL, Hadoop, spark, Keras, scikit learn, nlp. Check for the skills which are mentioned in the job description and compare it with resume.
                - Education: Evaluate whether the candidate's educational background is relevant. For example degree in computer science, Mathematics, statistics, AI related fields. Also check if the educational background of the candidate can bring role knowledge.
                - Certifications: Suggest whether the candidate has relevant certifications in areas such as Data Science, Machine Learning, Deep learning, Generative AI. Check for certifications from renouned bodies like Google AI, AWS certified machine learning engineer, Coursera, Udacity certifications.
                - Soft skills: Analyse of the soft skills of candidate are a good match for job or not. 
            
            ### Step 3: Formatting and readability
                - Check if the resume follows best practices in formatting. Some examples (but not limited to)
                    - Clear sections(experince, education, skills, projects)
                    - Bullet points instead of large text blocks
                    - Consistent font and layout. 
                - Flag excessive wordiness or lack of clarity
            
            ### Step 4: Bias detection and inclusive language
                - Check for any unconscious biases in the resume.

            ### Step 5: Suggestions for improvement
                - Provide actionable tips to improve the alignment of the resume with the job description:
                    - Missing skills: Recommend any technical skills that the candidate should add. For example, specific frameworks or tools.
                    - Missing experience: Suggest how better candidate can highlight their relevant experience with examples for example AI projects, model deployment, data analysis.
                    - Actionable improvements for each section: For example, if the job requires Tensorflow and resume only mentions Keras, recommend updating the experience section to include Tensorflow experience as well.
                - Highlight the skills that that the candidate lacks or is not mentioned in resume which is mentioned in job description.
                - Suggest improvements in resume structure if any.
                - Suggest replacing gendered language or ensuring neutral phrasing in descriptions.
                

            ### Step 6: Missing Keyword
                - Suggest relevant keywords from the job description and common terms that one should include in resume from these fields. Some examples (you can add whatever is relevant to the job description and role)
                    - Machine Learning: Model Optimization, Hyperparameter Tuning, feature selection, feature engineering, cross validation, Exploratory Data Analysis (EDA)
                    - Deep learning: neural network, CNN, GAN, Transfer learning
                    - Data Science: Statistical modelling, Exploratory Data Analysis (EDA), A/B testing
                    - Generative AI: Transformer model, LLM
                - You do not need to suggest all these keywords as is. Analyse the job description and resume and then check which of these keywords would be relevant or what other keywords apart from this would be relevant and suggest those keywords only. Suggest only 5-7 keywords and at max 10 if highly important ones are missing.

            ### Step 7: Feedback:
                - Give a summary of your analysis, including whether a candidate is a good fit for the job and any final recommendations. Make this professional, constructive and friendly. Talk about role knowledge and role expertise of the candidate with respect to job description.
            
            ### Step 8: What to expect in interview?
                - Give 5 interview questions that the candidate can expect on the basis of tools, skills and experience required in the job description. 
            
            ### Step 9: Write an email to the candidate giving summary of their strengths and weaknesses in skills only with respect to the job description. Suggest them some improvements as per your analysis. 
                - Do not suggest keywords that need to be added in the resume. That is just for internal purpose only.
                - Make this professional, constructive and friendly. 
                - This feedback should be encouraging and motivating. 
                - Don't forget to mention that the suggestions that you are making should be added to your resume if you hold the skill otherwise the approach should be to first learn the skill and then write in resume. 
                - Be polite. 
                - Email should not be too lengthy.
                - Include 3 interview questions that the candidate can expect during interview. This should be on the basis of candidate's resume and job description.
        
            
            ### In the output, do not mention step numbers. Just give the step headings. 

            ### Job description
                {job_description}
            
            ### Resume
                {resume_text}
        """
        return prompt
    
    def get_similar_role_names(self, role):
        role_names = f'''
            Give 5 job role names/position titles/designations similar to {role}.
        '''
        return role_names
    
    def get_job_alignment_prompt_any_field(self, job_description, resume_text, role):
        logging.info("Entered get_job_alignment_prompt_any_field")
        prompt =  prompt = f"""

            Give me answer in the below steps

            Ensure that you only evaluate the resume text with respect to the job description provided.
            You are a highly skilled resume reviewer with 20 years of experience in talent acquisition in {role}
            Your task is to evaluate whether the candidate's resume aligns with the provided job descriotion in these roles.
            Your review should follow these steps:

            ### Step 1: Job resume alignement scoring
            - This section should first include a percentage in bold and then from next line the description should follow.
            - Analyse the job description and Resume provided below.
            - Calculate a percentage match score based on:
                - Technical skill match: Check for alignment with required tools and techniques in {role}.
                - Relevant experience: Does the candidate have the required experience for the job role?
                - Keywords: Does the resume include necessary technical and role-specifi keywords?
                - Problem solving approach: Is the candidate familiar with problem solving techniques used in {role}
                - Provide the match percentage (0% - 100%) that reflects how well the resume aligns with the job description.
            
            ### Step 2: Resume sections analysis
            - Break down the analysis into key sections of the resume.
                - Experience: Analyse how the previous work experience aligns with the given job description. 
                - Skills: Check for the skills which are mentioned in the job description and compare it with resume.
                - Education: Evaluate whether the candidate's educational background is relevant. For example degree in field of {role}
                - Certifications: Suggest whether the candidate has relevant certifications in {role}. Check for certifications from renouned bodies in {role}.
                - Soft skills: Analyse of the soft skills of candidate are a good match for job or not. 

            ### Step 3: Formatting and readability
                - Check if the resume follows best practices in formatting. Some examples (but not limited to)
                    - Clear sections(experince, education, skills, projects)
                    - Bullet points instead of large text blocks
                    - Consistent font and layout. 
                - Flag excessive wordiness or lack of clarity
            
            ### Step 4: Bias detection and inclusive language
                - Check for any unconscious biases in the resume.   

            ### Step 5: Suggestions for improvement
                - Provide actionable tips to improve the alignment of the resume with the job description:
                    - Missing skills: Recommend any technical/non-technical skills that the candidate should add related to {role}.
                    - Missing experience: Suggest how better candidate can highlight their relevant experience with examples.
                    - Actionable improvements for each section: For example, if the job requires Tensorflow and resume only mentions Keras, recommend updating the experience section to include Tensorflow experience as well.
                - Highlight the necessary or required skills that that the candidate lacks or is not mentioned in resume which is mentioned in job description.
                - Suggest improvements in resume structure if any.
                - Suggest replacing gendered language or ensuring neutral phrasing in descriptions.
            
            ### Step 6: Missing Keyword
                - Suggest relevant keywords from the job description and common terms that one should include in resume from {role} fields. Some examples (you can add whatever is relevant to the job description and role)
                    - Machine Learning: Model Optimization, Hyperparameter Tuning, feature selection, feature engineering, cross validation, Exploratory Data Analysis (EDA)
                    - Deep learning: neural network, CNN, GAN, Transfer learning
                    - Data Science: Statistical modelling, Exploratory Data Analysis (EDA), A/B testing
                    - Generative AI: Transformer model, LLM
                - You do not need to suggest all these keywords as is. Analyse the job description and resume and then check which keywords would be relevant or what other keywords apart from this would be relevant and suggest those keywords only. Suggest only 5-7 keywords and at max 10 if highly important ones are missing.
            
            ### Step 7: Feedback:
                - Give a summary of your analysis, including whether a candidate is a good fit for the job and any final recommendations. Make this professional, constructive and friendly. This feedback should be encouraging and motivating. Talk about role knowledge and role expertise of the candidate with respect to job description.
            
            ### Step 8: Questions that can be asked in interview?
                - On the basis of resume at hand and the job description provided, suggest me 5 interview questions that can be asked to candidate. 
            
            ### Step 9: Write an email to the candidate giving summary of their strengths and weaknesses in skills only with respect to the job description. Suggest them some improvements as per your analysis. 
                - Do not suggest keywords that need to be added in the resume. That is just for internal purpose only.
                - Make this professional, constructive and friendly. 
                - This feedback should be encouraging and motivating. 
                - Don't forget to mention that the suggestions that you are making should be added to your resume if you hold the skill otherwise the approach should be to first learn the skill and then write in resume. 
                - Be polite. 
                - Email should not be too lengthy.
                - Include 3 interview questions that the candidate can expect during interview. This should be on the basis of candidate's resume and job description. 
                
            
            ### In the output, do not mention step numbers. Just give the step headings. 

            ### Job description
                {job_description}
            
            ### Resume
                {resume_text}
        """
        return prompt
    
    def get_score_prompt(self, job_description, resume_text):
        logging.info("Entered get_score_prompt")
        prompt = f"""

                Ensure that you only evaluate the resume text with respect to the job description provided.
                You are a highly skilled resume reviewer with 20 years of experience in talent acquisition in fields of Data Science, Machine Learning, Deep Learning and Generative AI.
                Your task is to evaluate whether the candidate's resume aligns with the provided job descriotion in aforementioned roles.


                - Only give one score to show the percentage match on the basis of below criterion
                - Analyse the job description and Resume provided below.
                - Calculate a percentage match score based on:
                    -  Technical skill match: Check for alignment with required tools, coding languages and techniques.
                    - Relevant experience: Does the candidate have the required experience for the job role?
                    - Keywords: Does the resume include necessary technical and role-specifig keywords?
                    - Problem solving approach: Is the candidate familiar with problem solving techniques used in this role like data wrangling, feature engineering, model evaluation? There are a lot of other problem solving techniques and I have only included a few examples.
                    - Provide the match percentage (0% - 100%) that reflects how well the resume aligns with the job description.
            
            
            ### Job description
                {job_description}
            
            ### Resume
                {resume_text}
            """
        return prompt
    
    def multiple_resume_comparison(self,resume:list, job_description):
        text = ''
        for i, t in resume:
            text = text + f"Candidate {i} - {t}"

        prompt = f"""
            For this full analysis, ensure that you stick to facts and what is known and present in individual resume and job application. DO NOT MAKE STUFF OF YOUR OWN.
            You are expert with 20 years of experience in hiring for. 
            Your task is to compare the resumes which are given to you in context relative to each other on given job description.
            Rank these from the best fit to the least fit. 

            ### Evaluation criteria (Total: 100%):
            1. Technical skills match (40%): Rate the candidate on technical skills on the basis of their technical skills. Some examples - 
                - Does the candidate possess the required technical skills, tools and knowledge.
                - Are they proficient in the tools mentioned in the job description.
                - Do they have certifications.
            2. Relevant Experience (30%): Rate the candidate on the relevant exp
                - Do they have relevant experience with the tools and technologies and skills that are mentioned in the job description?
                - Have they worked in similar projects, industries or domains?
            3. Keyword match (10%):
                - Does the resume contain important domain specific terms that are present in job description? 
            4. Certification and education (10%):
                - Do they have relevant degrees, courses or certifications which match what is mentioned in job description?
            5. Soft skills:
                - Does the soft skills mentioned in resume align with what is present in job description. 
            
            ### Input:
                ### Job description
                {job_description}

                ### Candidate resumes
                {text}

            ### Output:
                ### Ranked list (Best fit -> Least fit)
                    - Rank the candidates from best fit to least fit considering alignment with the job description
                ### Justification for ranking
                    - For each candidate, explain why they are ranked higher or lower than the others. 
                    - Strengths that placed them higher
                    - Weakeness that made them rank lower.
                Put the above information in the form of a table with columns - candidate number, strengths, weaknesses, additional comments. 
                ### Key takeways and final thoughts
                    - Summarise the strengths of talent pool.
                    - Recommend the top 2-3 candidates which should be moved to the next stage.
                
                Provide structured and professional feedback. Be constructive and encouraging with your tone.
        """
        return prompt
    