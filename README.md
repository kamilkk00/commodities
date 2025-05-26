# Commodities Price API

Azure Functions for serving Brent, WTI and Natural Gas spot prices from Cosmos DB.

## Setup

```bash
git clone https://github.com/kamilkk00/commodities
cd commodities
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp local.settings.example.json local.settings.json
# Add your Cosmos DB connection string
func start
```

## API

**Health Check**
```
GET /api/health
```

**Get Price**
```
POST /api/price
Content-Type: application/json

{
  "date": "2024-08-22"
}

Response:
{
  "price": 1.93
}
```

## Requirements

- Python 3.12
- Azure Functions Core Tools
- Azure subscription with Cosmos DB