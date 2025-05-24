import os
import sys
from azure.cosmos import CosmosClient, exceptions

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from utils.config import Config

class DataSaving:
    def __init__(self):
        cfg = Config()
        self.endpoint   = cfg.COSMOS_ENDPOINT
        self.key        = cfg.COSMOS_KEY
        self.database   = cfg.COSMOS_DB
        self.container  = cfg.COSMOS_CONTAINER
        # create client once
        self.client = CosmosClient(self.endpoint, credential=self.key)
        self.db     = self.client.get_database_client(self.database)
        self.cont   = self.db.get_container_client(self.container)

    def add(self):
        items = [
            {"id": "item8", "category": "toys",        "name": "Building Blocks Set", "brand": "Contoso",  "pieceCount": 150,   "ageRange": "3+",   "price": 24.99},
            {"id": "item9", "category": "apparel",     "title": "Hooded Sweatshirt",   "brand": "Fabrikam", "size": "L",         "color": "Navy",    "price": 34.99}
        ]
        for it in items:
            try:
                resp = self.cont.upsert_item(it)
                print(f"Added {resp['id']}")
            except exceptions.CosmosHttpResponseError as e:
                print(f"Failed to add {it['id']}: {e.message}")

    def close(self):
        self.client.close()

if __name__ == "__main__":
    save = DataSaving()
    save.add()
