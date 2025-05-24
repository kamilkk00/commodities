import os
import sys
import json
from azure.cosmos import CosmosClient, exceptions

# adjust path so that `utils.config` is importable
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../')
    )
)
from utils.config import Config

def get_container():
    cfg = Config()
    client = CosmosClient(cfg.COSMOS_ENDPOINT_BRENT, credential=cfg.COSMOS_KEY_BRENT)
    return client \
      .get_database_client(cfg.COSMOS_DB_BRENT) \
      .get_container_client(cfg.COSMOS_CONTAINER_BRENT)

def lookup_by_date(container, date_str):
    try:
        doc = container.read_item(item=date_str, partition_key=date_str)
        print(json.dumps(doc, indent=2))
    except exceptions.CosmosResourceNotFoundError:
        print(f"No record found for {date_str!r}")

def list_date_range(container, start, end):
    sql = """
      SELECT c.id, c.date, c.spotPrice
      FROM c
      WHERE c.date >= @start AND c.date <= @end
      ORDER BY c.date
    """
    params = [
        { "name":"@start", "value": start },
        { "name":"@end",   "value": end   }
    ]

    # Simple single-pass query (no manual paging)
    for item in container.query_items(
        query=sql,
        parameters=params,
        enable_cross_partition_query=True
    ):
        print(f"{item['date']}: {item['spotPrice']}")

def main():
    container = get_container()

    # Hard-coded range for this example
    start, end = "2025-05-09", "2025-05-16"
    print(f"Fetching Brent prices from {start} to {end}:\n")
    list_date_range(container, start, end)

if __name__ == "__main__":
    main()