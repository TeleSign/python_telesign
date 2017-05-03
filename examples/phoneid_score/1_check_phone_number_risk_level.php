<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\enterprise\sdk\phoneid\PhoneIdClient;

$customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
$api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

$phone_number = "phone_number";
$ucid = "BACF";

$phoneid = new PhoneIdClient($customer_id, $api_key);
$response = $phoneid->score($phone_number, $ucid);

if ($response->ok) {
  echo "Phone number $phone_number has a '{$response->json["risk"]["level"]}' risk level"
    . " and the recommendation is to '{$response->json["risk"]["recommendation"]}' the transaction.";
}
