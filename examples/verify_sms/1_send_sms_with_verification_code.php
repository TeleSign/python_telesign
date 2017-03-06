<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\enterprise\sdk\verify\VerifyClient;
use function telesign\sdk\util\randomWithNDigits;

$customer_id = "customer_id";
$secret_key = "secret_key";

$phone_number = "phone_number";
$verify_code = randomWithNDigits(5);

$verify = new VerifyClient($customer_id, $secret_key);
$response = $verify->sms($phone_number, [ "verify_code" => $verify_code ]);

echo "Please enter the verification code you were sent: ";

$user_entered_verify_code = trim(fgets(STDIN));

if ($verify_code == $user_entered_verify_code) {
  echo "Your code is correct.";
}
else {
  echo "Your code is incorrect.";
}
