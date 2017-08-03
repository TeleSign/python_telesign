<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\enterprise\sdk\verify\VerifyClient;
use function telesign\sdk\util\randomWithNDigits;

$customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
$api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

$phone_number = "phone_number";
$verify_code = randomWithNDigits(5);

$verify = new VerifyClient($customer_id, $api_key);
$response = $verify->sms($phone_number, [ "verify_code" => $verify_code ]);

$reference_id = $response->json["reference_id"];

echo "Please enter the verification code you were sent: ";

$user_entered_verify_code = trim(fgets(STDIN));

if ($verify_code == $user_entered_verify_code) {
  echo "Your code is correct." . PHP_EOL;
  
  $resopnse = $verify->completion($reference_id);
  
  if ($response->ok and $response->json["status"]["code"] == 1900) {
    echo "Completion successfully reported.";
  }
  else {
    echo "Error reporting completion.";
  }
}
else {
  echo "Your code is incorrect.";
}