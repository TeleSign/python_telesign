<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\voice\VoiceClient;
use function telesign\sdk\util\randomWithNDigits;

$customer_id = "customer id";
$secret_key = "secret key";

$phone_number = "phone number";

$message = "N'oubliez pas d'appeler votre mère pour son anniversaire demain.";
$message_type = "ARN";
$api_host = "https://rest-api.telesign.com";

$voice = new VoiceClient($customer_id, $secret_key, $api_host);

$response = $voice->call($phone_number, $message, $message_type, [ "voice" => "f-FR-fr" ]);

var_dump($response->status_code, $response->headers, $response->body, $response->ok, $response->json);

// wait a bit to give the call a chance to go through
sleep(60);

$response = $voice->status($response->json['reference_id']);

var_dump($response->status_code, $response->headers, $response->body, $response->ok, $response->json);
