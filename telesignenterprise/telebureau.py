from __future__ import unicode_literals

from telesign.rest import RestClient

TELEBUREAU_CREATE_RESOURCE = "/v1/telebureau/event"
TELEBUREAU_RETRIEVE_RESOURCE = "/v1/telebureau/event/{reference_id}"
TELEBUREAU_DELETE_RESOURCE = "/v1/telebureau/event/{reference_id}"


class TelebureauClient(RestClient):
    """
    TeleBureau is a service is based on TeleSign's watchlist, which is a proprietary database containing verified phone
    numbers of users known to have committed online fraud. TeleSign crowd-sources this information from its customers.
    Participation is voluntary, but you have to contribute in order to benefit.
    """

    def __init__(self, customer_id, api_key, rest_endpoint='https://rest-ww.telesign.com', **kwargs):
        super(TelebureauClient, self).__init__(customer_id, api_key, rest_endpoint=rest_endpoint, **kwargs)

    def create_event(self, phone_number, fraud_type, occurred_at, **params):
        """
        Creates a telebureau event corresponding to supplied data.

        See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
        """
        return self.post(TELEBUREAU_CREATE_RESOURCE,
                         phone_number=phone_number,
                         fraud_type=fraud_type,
                         occurred_at=occurred_at,
                         **params)

    def retrieve_event(self, reference_id, **params):
        """
        Retrieves the fraud event status. You make this call in your web application after completion of create
        transaction for a telebureau event.

        See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
        """
        return self.get(TELEBUREAU_RETRIEVE_RESOURCE.format(reference_id=reference_id),
                        **params)

    def delete_event(self, reference_id, **params):
        """
        Deletes a previously submitted fraud event. You make this call in your web application after completion of the
        create transaction for a telebureau event.

        See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
        """
        return self.delete(TELEBUREAU_DELETE_RESOURCE.format(reference_id=reference_id),
                           **params)
