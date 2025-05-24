import os
import sys
import json
from azure.cosmos import CosmosClient, exceptions

# allow importing your Config helper
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from utils.config import Config

def main():
    # load your Cosmos settings
    cfg = Config()
    endpoint   = cfg.COSMOS_ENDPOINT_BRENT
    key        = cfg.COSMOS_KEY_BRENT
    database   = cfg.COSMOS_DB_BRENT
    container  = cfg.COSMOS_CONTAINER_BRENT

    # create client + container handle
    client = CosmosClient(endpoint, credential=key)
    container_client = client \
        .get_database_client(database) \
        .get_container_client(container)

    # stream through your JSONL and upsert each document
    with open("brent.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            doc = json.loads(line)
            try:
                resp = container_client.upsert_item(doc)
                print(f"Upserted {resp['id']}")
            except exceptions.CosmosHttpResponseError as e:
                print(f"Failed to upsert {doc.get('id')}: {e.message}")


if __name__ == "__main__":
    main()