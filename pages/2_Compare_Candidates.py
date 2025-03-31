from src.components.file_handler import FileHandler
from logger import logging
from exception import CustomException
import streamlit as st
from src.components.text_preprocessor import GetTextFromPdf
import sys
from src.services.prompt_templates import CreatePrompt
from src.services.model_service import Model
from dotenv import load_dotenv
import os
from langchain_core.runnables import RunnableLambda
from PyPDF2 import PdfReader

load_dotenv()


os.environ["LANGSMITH_TRACING"] = "true"
LANGSMITH_API_KEY = os.environ["LANGSMITH_API_KEY"]

st.set_page_config(
    page_title = "Compare candidate"
)

def read_resume_files(uploaded_file):
    reader=PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):

        page=reader.pages[page]
        text+=str(page.extract_text())
    return text


st.title('Compare candidates')
st.markdown('Compare how different candidates rank relative to each other for the advertised job.')
job_description_text = st.text_area("Add the job description here")
resume_file = st.file_uploader(label = "Add Resume (PDF Only)", type = "pdf", accept_multiple_files=True)

upload_button = st.button('Upload', 'pdfButton')



def main():
    try:
        logging.info("Entered the main function")
        if upload_button:
            if resume_file is not None:
                resumes_text = [read_resume_files(f) for f in resume_file]
                cp = CreatePrompt()
                prompt = cp.multiple_resume_comparison(resumes_text, job_description_text)
                logging.info(f"My prompt = {prompt}")
                m = Model()
                # llm = m.llm_model()
                # ollama_llm = m.ollama_llm_model()
                groq_llm = m.groq_llm_model()
                # logging.info("Model created")
                score_response = groq_llm.invoke(prompt)
                # logging.info("Runnable invoked")
                st.write(score_response.content)
                # logging.info("Response written")
            else:
                st.warning("Please upload pdf file")
    except Exception as e:
        CustomException(e, sys)


if __name__ == "__main__":
    main()