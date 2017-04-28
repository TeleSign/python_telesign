<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\autoverify\AutoVerifyClient;

$customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
$api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

$external_id = "external_id";

$autoverify = new AutoVerifyClient($customer_id, $api_key);
$response = $autoverify->status($external_id);

if ($response->ok) {
  printf("AutoVerify transaction with external_id %s has status code %u and status description %s.",
    $external_id,
    $response->json['status']['code'],
    $response->json['status']['description']);
}
