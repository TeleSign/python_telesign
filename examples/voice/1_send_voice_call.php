<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\voice\VoiceClient;

$customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
$api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

$phone_number = "phone_number";
$message = "You're scheduled for a dentist appointment at 2:30PM.";
$message_type = "ARN";

$voice = new VoiceClient($customer_id, $api_key);
$response = $voice->call($phone_number, $message, $message_type);
