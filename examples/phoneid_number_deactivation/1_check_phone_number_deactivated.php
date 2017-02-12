<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\enterprise\sdk\phoneid\PhoneIdClient;

$customer_id = "customer_id";
$secret_key = "secret_key";

$phone_number = "phone_number";
$ucid = "ATCK";

$phoneid = new PhoneIdClient($customer_id, $secret_key);
$response = $phoneid->numberDeactivation($phone_number, $ucid);

print_r($response->json);

if ($response->json['number_deactivation']['last_deactivated']) {
  echo "Phone number {$response->json["number_deactivation"]["number"]}"
    . " was last deactivated {$response->json["number_deactivation"]["last_deactivated"]}.";
}
else {
  echo "Phone number {$response->json['number_deactivation']['number']} has not been deactivated.";
}
