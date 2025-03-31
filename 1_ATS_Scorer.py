from ats_score.src.components.file_handler import FileHandler
from logger import logging
from exception import CustomException
import streamlit as st
from ats_score.src.components.text_preprocessor import GetTextFromPdf
import sys
from ats_score.src.services.prompt_templates import CreatePrompt
from ats_score.src.services.model_service import Model
from dotenv import load_dotenv
import os
from langchain_core.runnables import RunnableLambda


load_dotenv()


os.environ["LANGSMITH_TRACING"] = "true"
LANGSMITH_API_KEY = os.environ["LANGSMITH_API_KEY"]

st.title('ATS Resume Scorer')
st.markdown('Add you resume in the form of PDF file and get ATS score. Not only this, we will also provide some tips on how to improve your resume')
job_description_text = st.text_area("Add the job description here")
resume_file = st.file_uploader("Add Resume (PDF Only)", "pdf")

upload_button = st.button('Upload', 'pdfButton')

role_options = st.selectbox(
    "For which domain are you analysing the resume for?",
    ("Machine Learning Engineer", "Generative AI Engineer", "Data Scientist", "Customer Support",
     "Technical Support Engineer", "Software developer", "Product Manager", "Account Executive", "Marketing"),
     index = None,
     placeholder="Select the role"
)

def choose_prompt(role, resume_text, job_description):
    cp = CreatePrompt()
    if role in ("Data Science", "Artificial Intelligence", "Machine Learning", "Generative AI"):
        prompt = cp.get_job_alignment_prompt(job_description, resume_text)
    else:
        prompt = cp.get_job_alignment_prompt_any_field(job_description, resume_text, role)
    return prompt
        

def main():
    try:
        logging.info("Entered the main function")
        if role_options:
            if resume_file is not None:
                fh = FileHandler(resume_file)
                tmp_file = fh.create_temp_file()
                logging.info("Temp file created")
                gtfp = GetTextFromPdf(tmp_file)
                resume_text = gtfp.read_text_from_pdf()
                logging.info("Resume text extracted")
                prompt = choose_prompt(role=role_options, resume_text=resume_text, job_description=job_description_text)
                m = Model()
                llm = m.llm_model()
                ollama_llm = m.ollama_llm_model()
                groq_llm = m.groq_llm_model()
                logging.info("Model created")
                score_response = groq_llm.invoke(prompt)
                logging.info("Runnable invoked")
                st.write(score_response.content)
                logging.info("Response written")
            else:
                st.warning("Please upload pdf file")
    except Exception as e:
        CustomException(e, sys)


if __name__ == "__main__":
    main()