import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Config:
    COSMOS_ENDPOINT_TEST = os.environ.get("COSMOS_ENDPOINT_TEST", "")
    COSMOS_KEY_TEST = os.environ.get("COSMOS_KEY_TEST", "")
    COSMOS_DB_TEST = os.environ.get("COSMOS_DB_TEST", "")
    COSMOS_CONTAINER_TEST = os.environ.get("COSMOS_CONTAINER_TEST", "")

    COSMOS_ENDPOINT_BRENT = os.environ.get("COSMOS_ENDPOINT_BRENT", "")
    COSMOS_KEY_BRENT = os.environ.get("COSMOS_KEY_BRENT", "")
    COSMOS_DB_BRENT = os.environ.get("COSMOS_DB_BRENT", "")
    COSMOS_CONTAINER_BRENT = os.environ.get("COSMOS_CONTAINER_BRENT", "")