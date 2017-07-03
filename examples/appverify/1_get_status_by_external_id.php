<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\appverify\AppVerifyClient;

$customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
$api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

$external_id = "external_id";

$appverify = new AppVerifyClient($customer_id, $api_key);
$response = $appverify->status($external_id);

if ($response->ok) {
  printf("App Verify transaction with external_id %s has status code %u and status description %s.",
    $external_id,
    $response->json['status']['code'],
    $response->json['status']['description']);
}
