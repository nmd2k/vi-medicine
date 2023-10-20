import os
from dotenv import load_dotenv

class ENV:
    load_dotenv()
    API_PORT = os.environ.get("API_PORT")
    API_HOST = os.environ.get("API_HOST")
    OPENAI_KEY = os.environ.get("OPENAI_KEY")
    KEY_VAULT_NAME = os.environ.get("KEY_VAULT_NAME")

    ### Azure OpenAI ###
    AZ_OAI_MODEL = os.environ.get("AZ_OAI_MODEL")
    AZ_OAI_VERSION = os.environ.get("AZ_OAI_VERSION")
    AZ_OAI_BASE = os.environ.get("AZ_OAI_BASE")
