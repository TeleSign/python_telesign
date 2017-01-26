<?php

namespace telesign\sdk\util;

/**
 * Helper function to format a timezone unaware datetime in rfc3339 utc timestamp the easy way
 */
function toUtcRfc3339 ($a_datetime) {
  return \DateTime::createFromFormat(DATE_RFC3339, $a_datetime, new \DateTimeZone("UTC"))->format(DATE_ISO8601);
}

/**
 * Helper function to generate a random number n digits in length using a system random
 */
function randomWithNDigits ($n) {
  $randomDigits = array($n);

  for ($i = 0; $i < $n; ++$i) {
    $randomDigits[$i] = rand(0, 9);
  }

  return join("", $randomDigits);
}

/**
 * Verify that a callback was made by TeleSign and was not sent by a malicious client by verifying the signature.
 *
 * @param string $secret_key The TeleSign API secret_key associated with your account
 * @param array  $headers    HTTP POST request headers
 * @param string $json_str   The POST body text, that is, the JSON string sent by TeleSign describing the transaction status
 */
function verifyTelesignCallback ($secret_key, $headers, $json_str) {
  $callback_signature = $headers["X-TS-Authorization"][0];
  $your_signature = base64_encode(hash_hmac("sha256", $json_str, base64_decode($secret_key), true));

  if (strlen($callback_signature) != strlen($your_signature)) {
    return false;
  }

  // Avoid timing attack with constant time equality check

  return hash_equals($callback_signature, $your_signature);
}
