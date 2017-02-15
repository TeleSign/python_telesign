<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\score\ScoreClient;

$customer_id = "customer_id";
$secret_key = "secret_key";

$phone_number = "phone_number";
$account_lifecycle_event = "create";

$data = new ScoreClient($customer_id, $secret_key);
$response = $data->score($phone_number, $account_lifecycle_event);

if ($response->ok) {
  echo "Phone number $phone_number has a '{$response->json["risk"]["level"]}' risk level"
  . " and the recommendation is to '{$response->json["risk"]["recommendation"]}' the transaction.";
}
