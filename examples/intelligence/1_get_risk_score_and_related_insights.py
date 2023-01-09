"""Example code that makes requests to intelligence API."""
from __future__ import print_function
from telesign.intelligence import IntelligenceClient

customer_1 = "your_customer_id-44ZA-47B5-95B9-ACXM9B1E5CAA"
api_key_1 = "your_api_key_or_password"

phone_number = "15555551212"
account_lifecycle_event = "create"

body = {
    "contact_details": {"email": "ghopper@gmail.com", "phone_number": "15555551212"},
    "external_id": "REG432538",
    "account_lifecycle_event": "create",
    "ip": "1.1.1.1",
    "device_id": "2e4fa042234d",
}

client = IntelligenceClient(customer_1, api_key_1)
response = client.intelligence(body)

if response.ok:
    print(
        "Phone number {} has a '{}' risk level and the score is '{}'.".format(
            response.json["phone_details"]["numbering"]["original"]["phone_number"],
            response.json["risk"]["level"],
            response.json["risk"]["score"],
        )
    )
