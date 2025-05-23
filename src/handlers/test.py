# src/handlers/healthcheck.py

import json
import azure.functions as func
from azure.functions import HttpRequest, HttpResponse

def lambda_handler(req: HttpRequest) -> HttpResponse:
    """
    Returns HTTP 200 OK with {"test":"works"}.
    """
    body = json.dumps({"test": "works"})
    return func.HttpResponse(
        body=body,
        status_code=200,
        mimetype="application/json"
    )