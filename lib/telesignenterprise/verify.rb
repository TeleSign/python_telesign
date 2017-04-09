require 'telesign/rest'

VERIFY_SMS_RESOURCE = '/v1/verify/sms'
VERIFY_VOICE_RESOURCE = '/v1/verify/call'
VERIFY_SMART_RESOURCE = '/v1/verify/smart'
VERIFY_PUSH_RESOURCE = '/v2/verify/push'
VERIFY_STATUS_RESOURCE = '/v1/verify/%{reference_id}'

module TelesignEnterprise

  # The Verify API delivers phone-based verification and two-factor authentication using a time-based, one-time passcode
  # sent via SMS message, Voice call or Push Notification.
  class VerifyClient < Telesign::RestClient

    def initialize(customer_id,
                   secret_key,
                   api_host: 'https://rest-ww.telesign.com',
                   timeout: nil)

      super(customer_id,
            secret_key,
            api_host: api_host,
            timeout: timeout)
    end

    # The SMS Verify API delivers phone-based verification and two-factor authentication using a time-based,
    # one-time passcode sent over SMS.
    #
    # See https://developer.telesign.com/docs/rest_api-verify-sms for detailed API documentation.
    def sms(phone_number, **params)

      self.post(VERIFY_SMS_RESOURCE,
                phone_number: phone_number,
                **params)
    end

    # The Voice Verify API delivers patented phone-based verification and two-factor authentication using a one-time
    # passcode sent over voice message.
    #
    # See https://developer.telesign.com/docs/rest_api-verify-call for detailed API documentation.
    def voice(phone_number, **params)

      self.post(VERIFY_VOICE_RESOURCE,
                phone_number: phone_number,
                **params)
    end

    # The Smart Verify web service simplifies the process of verifying user identity by integrating several TeleSign
    # web services into a single API call. This eliminates the need for you to make multiple calls to the TeleSign
    # Verify resource.
    #
    # See https://developer.telesign.com/docs/rest_api-smart-verify for detailed API documentation.
    def smart(phone_number, ucid, **params)

      self.post(VERIFY_SMART_RESOURCE,
                phone_number: phone_number,
                ucid: ucid,
                **params)
    end

    # The Push Verify web service allows you to provide on-device transaction authorization for your end users. It
    # works by delivering authorization requests to your end users via push notification, and then by receiving their
    # permission responses via their mobile device's wireless Internet connection.
    #
    # See https://developer.telesign.com/docs/rest_api-verify-push for detailed API documentation.
    def push(phone_number, ucid, **params)

      self.post(VERIFY_PUSH_RESOURCE,
                phone_number: phone_number,
                ucid: ucid,
                **params)
    end

    # Retrieves the verification result for any verify resource.
    #
    # See https://developer.telesign.com/docs/rest_api-verify-transaction-callback for detailed API documentation.
    def status(reference_id, **params)

      self.get(VERIFY_STATUS_RESOURCE % {:reference_id => reference_id},
               **params)
    end

  end
end
