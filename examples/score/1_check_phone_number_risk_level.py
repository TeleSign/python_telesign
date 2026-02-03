from __future__ import print_function
from telesign.score import ScoreClient

customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

phone_number = "phone_number"
account_lifecycle_event = "create"

score_client = ScoreClient(customer_id, api_key)
response = score_client.score(phone_number, account_lifecycle_event)

if response.ok:
    print(
        "Phone number {} has a '{}' risk level and the recommendation is to '{}' the transaction.".format(
            phone_number,
            response.json['risk']['level'],
            response.json['risk']['recommendation'])
    )
else:
    print(
        "Request failed with status code: {}. Details: {}".format(
            response.status_code, 
            response.json)
    )
