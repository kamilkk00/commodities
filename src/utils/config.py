import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Config:
    COSMOS_ENDPOINT = os.environ.get("COSMOS_ENDPOINT", "")
    COSMOS_KEY = os.environ.get("COSMOS_KEY", "")
    COSMOS_DB = os.environ.get("COSMOS_DB", "")
    COSMOS_CONTAINER = os.environ.get("COSMOS_CONTAINER", "")