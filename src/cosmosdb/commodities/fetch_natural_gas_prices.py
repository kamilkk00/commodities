import os
from azure.cosmos import CosmosClient, exceptions


class FetchNaturalGasPrice:
    def __init__(self):
        COSMOS_ENDPOINT_COMMODITIES=os.environ.get("COSMOS_ENDPOINT_COMMODITIES", "")
        COSMOS_KEY_COMMODITIES=os.environ.get("COSMOS_KEY_COMMODITIES", "")
        COSMOS_DB_COMMODITIES=os.environ.get("COSMOS_DB_COMMODITIES", "")
        COSMOS_CONTAINER_NATURAL_GAS=os.environ.get("COSMOS_CONTAINER_NATURAL_GAS", "")

        client = CosmosClient(COSMOS_ENDPOINT_COMMODITIES, credential=COSMOS_KEY_COMMODITIES)
        db_client = client.get_database_client(COSMOS_DB_COMMODITIES)
        self.container = db_client.get_container_client(COSMOS_CONTAINER_NATURAL_GAS)

    def lookup_by_date(self, date_str):
        try:
            doc = self.container.read_item(item=date_str, partition_key=date_str)
            return(doc['spotPrice'])
        except exceptions.CosmosResourceNotFoundError:
            return(f"No record found for {date_str!r}")


def main():
    fetcher = FetchNaturalGasPrice()
    date = "2021-05-12"
    price = fetcher.lookup_by_date(date)
    print(price)
    

if __name__ == "__main__":
    main()