from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from ats_score.src.constants.constant import *
from langchain_ollama.llms import OllamaLLM
from langchain_groq import ChatGroq
from logger import logging

load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API")



class Model:
    def __init__(self):
        pass

    def llm_model(self):
        llm = HuggingFaceEndpoint(
            repo_id = REPO_ID,
            max_new_tokens=MAX_LENGTH,
            temperature=TEMPERATURE,
            top_k=TOP_K,
            top_p = TOP_P,
            repetition_penalty=REPETION_PENALTY,
            huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
        )
        return llm
    
    def ollama_llm_model(self):
        return OllamaLLM(model="gemma3:12b")
    
    def groq_llm_model(self):
        logging.info("Entered groq_llm_model")
        llm = ChatGroq(
                        model_name="llama-3.3-70b-versatile",
                        temperature=0.7,
                        api_key=GROQ_API_KEY,
                        max_tokens=MAX_LENGTH
                      )
        return llm