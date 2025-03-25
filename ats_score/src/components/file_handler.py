import tempfile
from logger import logging
from exception import CustomException
import sys

class FileHandler:
    def __init__(self, uploaded_file):
        self.uploaded_file = uploaded_file

    def create_temp_file(self):
        try:
            logging.info("Entered create_temp_file method")
            temp_file = tempfile.NamedTemporaryFile(prefix = 'pre_', suffix='.pdf', delete = False)
            with temp_file as t:
                t.write(self.uploaded_file.read())
                t.flush()
                return t.name
        except Exception as e:
            CustomException(e, sys)