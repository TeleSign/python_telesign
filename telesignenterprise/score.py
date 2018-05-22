from __future__ import unicode_literals

from telesign.score import ScoreClient as _ScoreClient


class ScoreClient(_ScoreClient):
    """
    Score provides risk information about a specified phone number.
    """

    def __init__(self, customer_id, api_key, rest_endpoint="https://rest-ww.telesign.com", **kwargs):
        super(ScoreClient, self).__init__(customer_id, api_key, rest_endpoint=rest_endpoint, **kwargs)
