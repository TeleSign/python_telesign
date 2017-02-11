<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\enterprise\sdk\verify\VerifyClient;

$customer_id = "customer_id";
$secret_key = "secret_key";

$phone_number = "phone_number";
$template = 'Your Widgets \'n\' More verification code is $$CODE$$.';

$verify = new VerifyClient($customer_id, $secret_key);
$response = $verify->sms($phone_number, [ "template" => $template ]);
