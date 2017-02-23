<?php

namespace telesign\sdk\phoneid;

use telesign\sdk\rest\RestClient;

/**
 * A set of APIs that deliver deep phone number data attributes that help optimize the end user
 * verification process and evaluate risk.
 */
class PhoneIdClient extends RestClient {

  const PHONEID_RESOURCE = "/v1/phoneid/%s";

  /**
   * The PhoneID API provides a cleansed phone number, phone type, and telecom carrier information to determine the
   * best communication method - SMS or voice.
   *
   * See https://developer.telesign.com/docs/phoneid-api for detailed API documentation.
   */
  function phoneid ($phone_number, array $fields = []) {
    return $this->post(sprintf(self::PHONEID_RESOURCE, $phone_number), $fields);
  }

}
