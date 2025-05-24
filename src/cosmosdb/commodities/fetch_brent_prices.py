import os
import sys
import json
from azure.cosmos import CosmosClient, exceptions
from datetime import datetime

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

def list_date_range(container, start, end, page_size=10):
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

    # get the pages iterator
    pages = container.query_items(
        query=sql,
        parameters=params,
        enable_cross_partition_query=True
    ).by_page(page_size)

    for page in pages:
        items = list(page)
        if not items:
            # nothing more to fetch
            break
        print(f"\n--- Next {len(items)} items ---")
        for item in items:
            print(f"{item['date']}: {item['spotPrice']}")

def main():
    container = get_container()

    raw = input(
      "Enter a date (YYYY-MM-DD) or a range YYYY-MM-DD:YYYY-MM-DD (no backticks or quotes): "
    ).strip()
    # strip any backticks or quotes the user might have typed
    raw = raw.strip('`"\'').strip()

    if ':' in raw:
        start, end = raw.split(':', 1)
        # normalize order
        if start > end:
            start, end = end, start
        list_date_range(container, start, end)
    else:
        lookup_by_date(container, raw)

if __name__ == "__main__":
    main()