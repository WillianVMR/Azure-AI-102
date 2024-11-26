import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT_URL = os.getenv("ENDPOINT_URL")
    KEY = os.getenv("SUBSCRIPTION_KEY")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    AZURE_STORAGE_CONTAINER_NAME = os.getenv("AZURE_STORAGE_CONTAINER_NAME")
