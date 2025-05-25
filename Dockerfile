# Dockerfile
FROM mcr.microsoft.com/azure-functions/python:4-python3.12-appservice

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true \
    FUNCTIONS_WORKER_RUNTIME=python \
    AzureWebJobsStorage=UseDevelopmentStorage=true

WORKDIR /home/site/wwwroot

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only your config & code
COPY host.json functions.yml function_app.py ./
COPY src/ ./src

# Functions host listens on port 80 inside
EXPOSE 80
# (ENTRYPOINT is baked into the base image)