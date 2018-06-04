<?php

namespace telesign\enterprise\sdk\appverify;

use telesign\sdk\appverify\AppVerifyClient as _AppVerifyClient;

/**
 * App Verify is a secure, lightweight SDK that integrates a frictionless user verification process into existing
 * native mobile applications.
 */
class AppVerifyClient extends _AppVerifyClient {

  function __construct ($customer_id, $api_key, $rest_endpoint = "https://rest-ww.telesign.com", ...$other) {
    parent::__construct($customer_id, $api_key, $rest_endpoint, ...$other);
  }

}
