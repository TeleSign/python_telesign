"""Client to make requests to intelligence API."""
from __future__ import unicode_literals

from telesign.rest import RestClient
from telesign.util import AuthMethod

INTELLIGENCE_BASE_URL = "https://detect.telesign.com"


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