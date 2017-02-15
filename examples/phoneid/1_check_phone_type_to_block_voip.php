<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\phoneid\PhoneIdClient;

$customer_id = "customer_id";
$secret_key = "secret_key";

$phone_number = "phone_number";
$phone_type_voip = "5";

$data = new PhoneIdClient($customer_id, $secret_key);
$response = $data->phoneid($phone_number);

if ($response->ok) {
  if ($response->json['phone_type']['code'] == $phone_type_voip) {
    echo "Phone number $phone_number is a VOIP phone.";
  }
  else {
    echo "Phone number $phone_number is not a VOIP phone.";
  }
}
