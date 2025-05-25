import os

class Config:
    COSMOS_ENDPOINT_BRENT = os.environ.get("COSMOS_ENDPOINT_BRENT", "")
    COSMOS_KEY_BRENT = os.environ.get("COSMOS_KEY_BRENT", "")
    COSMOS_DB_BRENT = os.environ.get("COSMOS_DB_BRENT", "")
    COSMOS_CONTAINER_BRENT = os.environ.get("COSMOS_CONTAINER_BRENT", "")