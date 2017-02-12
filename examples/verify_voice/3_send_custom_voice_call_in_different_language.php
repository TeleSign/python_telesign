<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\enterprise\sdk\verify\VerifyClient;

$customer_id = "customer_id";
$secret_key = "secret_key";

$phone_number = "phone_number";
$language = "fr-FR";
$tts_message = 'Votre code de vérification Widgets \'n\' More est $$CODE$$.';

$verify = new VerifyClient($customer_id, $secret_key);
$response = $verify->voice($phone_number, [ "language" => $language, "tts_message" => $tts_message ]);
