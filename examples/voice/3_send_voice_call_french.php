<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\voice\VoiceClient;

$customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
$api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

$phone_number = "phone_number";

$message = "N'oubliez pas d'appeler votre mère pour son anniversaire demain.";
$message_type = "ARN";

$voice = new VoiceClient($customer_id, $api_key);

$response = $voice->call($phone_number, $message, $message_type, [ "voice" => "f-FR-fr" ]);
