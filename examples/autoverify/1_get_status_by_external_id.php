<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\autoverify\AutoVerifyClient;

$customer_id = "customer_id";
$secret_key = "secret_key";

$external_id = "external_id";

$autoverify = new AutoVerifyClient($customer_id, $secret_key);
$response = $autoverify->status($external_id);

if ($response->ok) {
  printf("AutoVerify transaction with external_id %s has status code %u and status description %s.",
    $external_id,
    $response->json['status']['code'],
    $response->json['status']['description']);
}
