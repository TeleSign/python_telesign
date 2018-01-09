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
    print("\n********PHONEID*********\n");
    $json_fields = json_encode($fields);
    
    $headers = $this->generateTelesignHeaders(
      $this->customer_id,
      $this->api_key,
      $method_name,
      $resource,
      $json_fields,
      $date,
      $nonce,
      $this->user_agent
    );

    $option = in_array($method_name, [ "POST", "PUT" ]) ? "body" : "query";

    return new Response($this->client->request($method_name, $resource, [
      "headers" => $headers,
      $option => $json_fields,
      "http_errors" => false
    ]));
  }
  
  static function generateTelesignHeaders (
    $customer_id,
    $api_key,
    $method_name,
    $resource,
    $url_encoded_fields,
    $date = null,
    $nonce = null,
    $user_agent = null
  ) {
    if (!$date) {
      $date = gmdate("D, d M Y H:i:s T");
    }

    if (!$nonce) {
      $nonce = Uuid::uuid4()->toString();
    }

    $content_type = in_array($method_name, ["POST", "PUT"]) ? "application/json" : "";
    
    $auth_method = "HMAC-SHA256";

    $string_to_sign_builder = [
      $method_name,
      "\n$content_type",
      "\n$date",
      "\nx-ts-auth-method:$auth_method",
      "\nx-ts-nonce:$nonce"
    ];

    if ($content_type && $url_encoded_fields) {
      $string_to_sign_builder[] = "\n$url_encoded_fields";
    }

    $string_to_sign_builder[] = "\n$resource";

    $string_to_sign = join("", $string_to_sign_builder);

    $signature = base64_encode(
      hash_hmac("sha256", utf8_encode($string_to_sign), base64_decode($api_key), true)
    );
    $authorization = "TSA $customer_id:$signature";

    $headers = [
      "Authorization" => $authorization,
      "Date" => $date,
      "Content-Type" => $content_type,
      "x-ts-auth-method" => $auth_method,
      "x-ts-nonce" => $nonce
    ];

    if ($user_agent) {
      $headers["User-Agent"] = $user_agent;
    }

    return $headers;
  }

}
