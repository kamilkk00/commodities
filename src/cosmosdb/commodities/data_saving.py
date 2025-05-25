import os
import sys
import json
from azure.cosmos import CosmosClient, exceptions

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from utils.config import Config

def main():
    # Initialize configuration to retrieve Cosmos DB endpoint, key, database and container names
    cfg = Config()
    endpoint   = cfg.COSMOS_ENDPOINT_COMMODITIES
    key        = cfg.COSMOS_KEY_COMMODITIES
    database   = cfg.COSMOS_DB_COMMODITIES
    container  = cfg.COSMOS_CONTAINER_NATURAL_GAS

    # Create CosmosClient and obtain a reference to the target container
    client = CosmosClient(endpoint, credential=key)
    container_client = client \
        .get_database_client(database) \
        .get_container_client(container)

    # Open the JSONL file, parse each line, and upsert the document into Cosmos DB
    # Log success or failure for each record
    with open("natural_gas.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            doc = json.loads(line)
            try:
                resp = container_client.upsert_item(doc)
                print(f"Upserted {resp['id']}")
            except exceptions.CosmosHttpResponseError as e:
                print(f"Failed to upsert {doc.get('id')}: {e.message}")


if __name__ == "__main__":
    main()