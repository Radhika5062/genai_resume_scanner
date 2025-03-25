import sys
from src.components.file_handler import FileHandler
from langchain_community.document_loaders import PyPDFLoader
from logger import logging
from exception import CustomException
import os

class GetTextFromPdf:
    def __init__(self, temp_file_name):
        self.temp_file_name = temp_file_name

    def read_text_from_pdf(self):
        try:
            
            loader = PyPDFLoader(self.temp_file_name)
            documents = loader.load()
            text_content = "\n".join([doc.page_content for doc in documents])
            logging.info(f"Temporary file - {self.temp_file_name}")
            os.remove(self.temp_file_name)
            return text_content
        except Exception as e:
            CustomException(e, sys)