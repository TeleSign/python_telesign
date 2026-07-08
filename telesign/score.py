from telesign.rest import RestClient

DETECT_HOST = "https://detect.telesign.com"
INTELLIGENCE_RESOURCE = "/intelligence/phone"
EMAIL_INTELLIGENCE_RESOURCE = "/intelligence/email"


class ScoreClient(RestClient):
    """
    ScoreClient for TeleSign Intelligence Cloud.
    Supports POST /intelligence/phone endpoint(Cloud migration).
    """

    def __init__(self, customer_id, api_key, rest_endpoint=DETECT_HOST, **kwargs):
        super(ScoreClient, self).__init__(customer_id, api_key, rest_endpoint, **kwargs)

    def score(self, phone_number, account_lifecycle_event, **params):
        """
        Obtain a risk recommendation for a phone number using Telesign Intelligence Cloud API.
        Required parameters:
          - phone_number
          - account_lifecycle_event ("create", "sign-in", "transact", "update", "delete")
        Optional parameters: account_id, device_id, email_address, external_id, originating_ip, etc.
        """
        if not phone_number:
            raise ValueError("phone_number cannot be null or empty")

        if not account_lifecycle_event:
            raise ValueError("account_lifecycle_event cannot be null or empty")

        params["phone_number"] = phone_number
        params["account_lifecycle_event"] = account_lifecycle_event

        return self.post(INTELLIGENCE_RESOURCE, **params)

    def email_intelligence(self, email_address, account_lifecycle_event, **params):
        """
        Obtain a risk recommendation for this email address, as well as other relevant information using Email Intelligence API.
        Required parameters:
          - email_address
          - account_lifecycle_event ("create", "sign-in", "transact", "update", "delete")
        """
        if not email_address:
            raise ValueError("email_address cannot be null or empty")

        if not account_lifecycle_event:
            raise ValueError("account_lifecycle_event cannot be null or empty")

        params["email_address"] = email_address
        params["account_lifecycle_event"] = account_lifecycle_event

        return self.post(EMAIL_INTELLIGENCE_RESOURCE, **params)
