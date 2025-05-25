import json
import azure.functions as func
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from cosmosdb.commodities.fetch_natural_gas_prices import FetchNaturalGasPrice

def handler(req: func.HttpRequest) -> func.HttpResponse:

    gas = FetchNaturalGasPrice()

    body = req.get_json()
    date = body["date"]

    price = gas.lookup_by_date(date)


    return func.HttpResponse(
        json.dumps({"price": price}, default=str),
        status_code=200,
        mimetype="application/json"
    )