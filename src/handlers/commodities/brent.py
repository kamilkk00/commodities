import json
import azure.functions as func

def handler(req: func.HttpRequest) -> func.HttpResponse:
    body = req.get_json()
    number = body["number"]

    return func.HttpResponse(
        json.dumps({"result": number}, default=str),
        status_code=200,
        mimetype="application/json"
    )