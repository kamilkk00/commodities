import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    COSMOS_ENDPOINT_COMMODITIES = os.environ.get("COSMOS_ENDPOINT_COMMODITIES", "")
    COSMOS_KEY_COMMODITIES = os.environ.get("COSMOS_KEY_COMMODITIES", "")
    COSMOS_DB_COMMODITIES = os.environ.get("COSMOS_DB_COMMODITIES", "")

    COSMOS_CONTAINER_BRENT = os.environ.get("COSMOS_CONTAINER_BRENT", "")
    COSMOS_CONTAINER_WTI = os.environ.get("COSMOS_CONTAINER_WTI", "")