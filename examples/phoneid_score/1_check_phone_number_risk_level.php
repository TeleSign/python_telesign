<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\enterprise\sdk\phoneid\PhoneIdClient;

$customer_id = "customer_id";
$secret_key = "secret_key";

$phone_number = "phone_number";
$ucid = "BACF";

$phoneid = new PhoneIdClient($customer_id, $secret_key);
$response = $phoneid->score($phone_number, $ucid);

echo "Phone number $phone_number has a '{$response->json["risk"]["level"]}' risk level"
  . " and the recommendation is to '{$response->json["risk"]["recommendation"]}' the transaction.";
