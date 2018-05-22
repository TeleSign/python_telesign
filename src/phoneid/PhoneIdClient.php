<?php

namespace telesign\sdk\phoneid;

use telesign\sdk\rest\RestClient;
use telesign\sdk\rest\Response;

use Ramsey\Uuid\Uuid;

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
  
  protected function execute ($method_name, $resource, $fields = [], $date = null, $nonce = null) {
    $json_fields = json_encode($fields, JSON_FORCE_OBJECT);
    
    $content_type = in_array($method_name, ["POST", "PUT"]) ? "application/json" : "";
    
    $headers = $this->generateTelesignHeaders(
      $this->customer_id,
      $this->api_key,
      $method_name,
      $resource,
      $json_fields,
      $date,
      $nonce,
      $this->user_agent,
      $content_type
    );

    $option = in_array($method_name, [ "POST", "PUT" ]) ? "body" : "query";

    return new Response($this->client->request($method_name, $resource, [
      "headers" => $headers,
      $option => in_array($method_name, [ "POST", "PUT"]) ? $json_fields : $fields,
      "http_errors" => false
    ]));
  }

}
