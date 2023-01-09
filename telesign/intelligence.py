"""Client to make requests to intelligence API."""
from __future__ import unicode_literals

from telesign.rest import RestClient
from telesign.util import AuthMethod

INTELLIGENCE_BASE_URL = "https://detect.telesign.com"
INTELLIGENCE_ENDPOINT_PATH = "/intelligence"


class IntelligenceClient(RestClient):
    """
    It is critical today to evaluate fraud risk throughout the entire customer journey.

    Telesign Intelligence makes it easy to understand the risk and the reason behind it with tailored scoring models
    and comprehensive reason codes.
    """

    def __init__(self, customer_id, api_key, **kwargs):
        super(IntelligenceClient, self).__init__(
            customer_id=customer_id,
            api_key=api_key,
            rest_endpoint=INTELLIGENCE_BASE_URL,
            auth_method=AuthMethod.BASIC.value,
            **kwargs
        )

    def intelligence(self, params):
        """
        Telesign Intelligence is like a credit check for digital profiles.

        You submit a phone number, IP, and email to the service, the individual
        identifiers are each evaluated, and then a score is returned telling you how risky
        that user is. You decide whether to proceed based on the score.

        See https://developer.telesign.com/enterprise/docs/intelligence-overview
        for detailed API documentation.
        """
        return self.post(INTELLIGENCE_ENDPOINT_PATH, body=params, query_params=None)
