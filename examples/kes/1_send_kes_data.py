from __future__ import print_function
from telesign.kes import KESClient

customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

kes_payload = {
    "event_type": "completion",
    "event_data": {
        "score_transaction_id":  1234,
        "account_lifecycle_event": "create",
        "industry_type": "fishing",
        "transaction_type": "payment",
        "label": "fraudulent",
        "label_timestamp": "2021-07-01 12:23:23",
        "fraud_type": "Abuse",
        "transaction_cost": "$.12",
        "device_id": "xx",
        "account_id": "yy",
        "call_completed": True,
    }
}

data = KESClient(customer_id, api_key)
response = data.kes(**kes_payload)

if response.ok:
    print("Known Event Data request accepted by Telesign")
