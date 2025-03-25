from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from ats_score.src.constants.constant import *
from langchain_ollama.llms import OllamaLLM

load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print(HUGGINGFACEHUB_API_TOKEN)

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

