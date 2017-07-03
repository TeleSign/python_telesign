<?php

namespace telesign\sdk\appverify;

use telesign\sdk\rest\RestClient;

/**
 * App Verify is a secure, lightweight SDK that integrates a frictionless user verification process into existing
 * native mobile applications.
 */
class AppVerifyClient extends RestClient {

  const APPVERIFY_STATUS_RESOURCE = "/v1/mobile/verification/status/%s";

  /**
   * Retrieves the verification result for an App Verify transaction by external_id. To ensure a secure verification
   * flow you must check the status using TeleSign's servers on your backend. Do not rely on the SDK alone to
   * indicate a successful verification.
   *
   * See https://developer.telesign.com/docs/app-verify-android-sdk-self#section-get-status-service or
   * https://developer.telesign.com/docs/app-verify-ios-sdk-self#section-get-status-service for detailed
   * API documentation.
   */
  function status ($external_id, array $params = []) {
    return $this->get(sprintf(self::APPVERIFY_STATUS_RESOURCE, $external_id), $params);
  }

}
