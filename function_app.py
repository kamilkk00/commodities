import logging
import yaml
import importlib

import azure.functions as func
from azure.functions import HttpRequest, HttpResponse, FunctionApp

# Create the FunctionApp instance
app = FunctionApp()

# 1) Load functions configuration from YAML
with open("functions.yml", "r") as f:
    cfg = yaml.safe_load(f)

for fn_name, fn_cfg in cfg["functions"].items():
    # 2a) Import the handler
    module_path, handler_name = fn_cfg["handler"].rsplit(".", 1)
    module = importlib.import_module(module_path)
    handler = getattr(module, handler_name)

    # 2b) Extract HTTP settings
    http = fn_cfg["http"]
    methods = [m.upper() for m in http["methods"]]
    route = http["path"]
    auth_level = getattr(func.AuthLevel, http["authLevel"].upper())

    # 3) Decorate the handler:
    fn = handler
    # assign a unique function name (must differ for each entry)
    fn = app.function_name(fn_name)(fn)
    # attach the HTTP trigger
    fn = app.route(
        route=route,
        methods=methods,
        auth_level=auth_level
    )(fn)