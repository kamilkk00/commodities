import os
import sys
import json
from azure.cosmos import CosmosClient, exceptions

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.config import Config

class FetchBrentPrice:
    def __init__(self):
        cfg = Config()
        client = CosmosClient(
            cfg.COSMOS_ENDPOINT_BRENT,
            credential=cfg.COSMOS_KEY_BRENT
        )
        database = client.get_database_client(cfg.COSMOS_DB_BRENT)
        self.container = database.get_container_client(cfg.COSMOS_CONTAINER_BRENT)

    def lookup_by_date(self, date_str):
        try:
            doc = self.container.read_item(item=date_str, partition_key=date_str)
            return(doc['spotPrice'])
        except exceptions.CosmosResourceNotFoundError:
            return(f"No record found for {date_str!r}")

    def list_date_range(self, start, end):
        sql = (
            'SELECT c.id, c.date, c.spotPrice '
            'FROM c '
            'WHERE c.date >= @start AND c.date <= @end '
            'ORDER BY c.date'
        )
        params = [
            {"name": "@start", "value": start},
            {"name": "@end",   "value": end}
        ]
        result = []
        for item in self.container.query_items(
            query=sql,
            parameters=params,
            enable_cross_partition_query=True
        ):
            result.append(f"{item['date']}: {item['spotPrice']}")
        return result

def main():
    # fetcher = FetchBrentPrice()
    # # Hard-coded range for this example
    # start, end = "2025-05-09", "2025-05-16"
    # print(f"Fetching Brent prices from {start} to {end}:\n")
    # price = fetcher.list_date_range(start, end)
    # print (price)

    fetcher = FetchBrentPrice()
    # Single-date fetch for example
    date = "2025-05-12"
    price = fetcher.lookup_by_date(date)
    print(price)
    

if __name__ == "__main__":
    main()