# src/handlers/healthcheck.py

import json
import azure.functions as func
from azure.functions import HttpRequest, HttpResponse

def lambda_handler(req: HttpRequest) -> HttpResponse:
    """
    Returns HTTP 200 OK with {"result":"OK"}.
    """
    body = json.dumps({"result": "OK"})
    return func.HttpResponse(
        body=body,
        status_code=200,
        mimetype="application/json"
    )