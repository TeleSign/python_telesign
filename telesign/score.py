from __future__ import unicode_literals

from telesign.rest import RestClient

SCORE_RESOURCE = "/v1/score/{phone_number}"


class ScoreClient(RestClient):
    """
    Score provides risk information about a specified phone number.
    """

    def __init__(self, customer_id, api_key, **kwargs):
        super(ScoreClient, self).__init__(customer_id, api_key, **kwargs)

    def score(self, phone_number, account_lifecycle_event, **params):
        """
        Score is an API that delivers reputation scoring based on phone number intelligence, traffic patterns, machine
        learning, and a global data consortium.

        See https://developer.telesign.com/docs/score-api for detailed API documentation.
        """
        return self.post(SCORE_RESOURCE.format(phone_number=phone_number),
                         account_lifecycle_event=account_lifecycle_event,
                         **params)
