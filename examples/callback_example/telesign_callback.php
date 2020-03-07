<?php
const CUSTOMER_ID = "Your 40 Character Customer ID Goes here";
const API_KEY = "YOUR API KEY GOES HERE";

function _log($log_level, $log_message) {
  //syslog($log_level, $log_message);
  $stderr = fopen('php://stderr', 'w');
  fwrite($stderr,sprintf("%s: %s\n", $log_level, $log_message));
}

// TeleSign sends callback for Delivery Reports, Status Updates, and Mobile Originating SMS using the POST HTTP method.
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  // Generate a signature based on the contents of the callback request body signing with your API Secret Key.
  $postBody = file_get_contents('php://input');
  $signature = base64_encode(
    hash_hmac("sha256", utf8_encode($postBody), base64_decode(API_KEY), true)
  );
  list($authType, $authToken) = explode(' ', $_SERVER['HTTP_AUTHORIZATION'], 2);
  list($requestCustomerID, $requestSignature) = explode(':', $authToken, 2);
  if (hash_equals(CUSTOMER_ID, $requestCustomerID)) {
    if (hash_equals($signature, $requestSignature)) {
      $callbackContents = json_decode($postBody, true);
      // You have now validated the request, and may use the contents of the callback to take some action.
      _log(LOG_DEBUG, sprintf(
        "Received callback for Transaction %s with status %s (%s): %s",
        $callbackContents['reference_id'], $callbackContents['status']['description'], $callbackContents['status']['code'], $postBody
      ));
      header('HTTP/1.1 200 OK', true, 200);
    } else {
      _log(LOG_INFO, sprintf("Invalid signature: %s != %s", $signature, $requestSignature));
      header('HTTP/1.1 401 Unuthorized', true, 401);
    }
  } else {
    _log(LOG_INFO,"Request for unknown Customer ID");
    header('HTTP/1.1 401 Unuthorized', true, 401);
  }
} else {
  _log(LOG_INFO, sprintf("Unexpected HTTP Method: %s", $_SERVER['REQUEST_METHOD']));
  header('HTTP/1.1 405 Method Not Allowed', true, 405);
}