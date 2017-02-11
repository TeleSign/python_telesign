<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\enterprise\sdk\verify\VerifyClient;

$customer_id = "customer_id";
$secret_key = "secret_key";

$phone_number = "phone_number";
$template = 'Votre code de vérification Widgets \'n\' More est $$CODE$$.';

$verify = new VerifyClient($customer_id, $secret_key);
$response = $verify->sms($phone_number, [ "template" => $template ]);
