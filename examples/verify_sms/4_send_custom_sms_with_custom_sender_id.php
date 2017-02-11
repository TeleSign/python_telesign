<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\enterprise\sdk\verify\VerifyClient;

$customer_id = "customer_id";
$secret_key = "secret_key";

$phone_number = "phone_number";
$my_sender_id = "my_sender_id";  // Client Services must white list any custom sender_id for it to take effect

$verify = new VerifyClient($customer_id, $secret_key);
$response = $verify->sms($phone_number, [ "sender_id" => $my_sender_id ]);
