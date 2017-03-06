<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\voice\VoiceClient;

$customer_id = "customer id";
$secret_key = "secret key";

$phone_number = "phone number";

$message = "N'oubliez pas d'appeler votre mère pour son anniversaire demain.";
$message_type = "ARN";

$voice = new VoiceClient($customer_id, $secret_key);

$response = $voice->call($phone_number, $message, $message_type, [ "voice" => "f-FR-fr" ]);
