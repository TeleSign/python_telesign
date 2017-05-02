require 'telesign/rest'

TELEBUREAU_CREATE_RESOURCE = '/v1/telebureau/event'
TELEBUREAU_RETRIEVE_RESOURCE = '/v1/telebureau/event/%{reference_id}'
TELEBUREAU_DELETE_RESOURCE = '/v1/telebureau/event/%{reference_id}'

module TelesignEnterprise

  # TeleBureau is a service is based on TeleSign's watchlist, which is a proprietary database containing verified phone
  # numbers of users known to have committed online fraud. TeleSign crowd-sources this information from its customers.
  # Participation is voluntary, but you have to contribute in order to benefit.
  class TelebureauClient < Telesign::RestClient

    def initialize(customer_id,
                   api_key,
                   rest_endpoint: 'https://rest-ww.telesign.com',
                   timeout: nil)

      super(customer_id,
            api_key,
            rest_endpoint: rest_endpoint,
            timeout: timeout)
    end

    # Creates a telebureau event corresponding to supplied data.
    #
    # See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
    def create_event(phone_number, fraud_type, occurred_at, **params)

      self.post(TELEBUREAU_CREATE_RESOURCE,
                phone_number: phone_number,
                fraud_type: fraud_type,
                occured_at: occurred_at,
                **params)
    end

    # Retrieves the fraud event status. You make this call in your web application after completion of create
    # transaction for a telebureau event.
    #
    # See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
    def retrieve_event(reference_id, **params)

      self.get(TELEBUREAU_RETRIEVE_RESOURCE % {:reference_id => reference_id},
               **params)
    end

    # Deletes a previously submitted fraud event. You make this call in your web application after completion of the
    # create transaction for a telebureau event.
    #
    # See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
    def delete_event(reference_id, **params)

      self.delete(TELEBUREAU_DELETE_RESOURCE % {:reference_id => reference_id},
                  **params)
    end
  end
end
