import os
from azure.cosmos import CosmosClient, exceptions


class FetchBrentPrice:
    def __init__(self):
        COSMOS_ENDPOINT_COMMODITIES=os.environ.get("COSMOS_ENDPOINT_COMMODITIES", "")
        COSMOS_KEY_COMMODITIES=os.environ.get("COSMOS_KEY_COMMODITIES", "")
        COSMOS_DB_COMMODITIES=os.environ.get("COSMOS_DB_COMMODITIES", "")
        COSMOS_CONTAINER_BRENT=os.environ.get("COSMOS_CONTAINER_BRENT", "")

        client = CosmosClient(COSMOS_ENDPOINT_COMMODITIES, credential=COSMOS_KEY_COMMODITIES)
        db_client = client.get_database_client(COSMOS_DB_COMMODITIES)
        self.container = db_client.get_container_client(COSMOS_CONTAINER_BRENT)

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