<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\enterprise\sdk\verify\VerifyClient;

$customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
$api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

$phone_number = "phone_number";
$template = 'Votre code de vérification Widgets \'n\' More est $$CODE$$.';

$verify = new VerifyClient($customer_id, $api_key);
$response = $verify->sms($phone_number, [ "template" => $template ]);
