<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\phoneid\PhoneIdClient;

$customer_id = "customer_id";
$secret_key = "secret_key";

$extra_digit = "0";
$phone_number = "phone_number";
$incorrect_phone_number = "$phone_number$extra_digit";

$data = new PhoneIdClient($customer_id, $secret_key);
$response = $data->phoneid($incorrect_phone_number);

if ($response->ok) {
  printf("Cleansed phone number has country code %s and phone number is %s.",
  $response->json['numbering']['cleansing']['call']['country_code'],
  $response->json['numbering']['cleansing']['call']['phone_number']);

  printf("Original phone number was %s.",
  $response->json['numbering']['original']['complete_phone_number']);
}
