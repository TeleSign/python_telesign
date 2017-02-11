<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\messaging\MessagingClient;
use function telesign\sdk\util\randomWithNDigits;

$customer_id = "customer_id";
$secret_key = "secret_key";

$phone_number = "phone_number";
$verify_code = randomWithNDigits(5);
$message = "Your code is $verify_code";
$message_type = "OTP";

$messaging = new MessagingClient($customer_id, $secret_key);
$response = $messaging->message($phone_number, $message, $message_type);

echo "Please enter the verification code you were sent: ";

$user_entered_verify_code = trim(fgets(STDIN));

if ($verify_code == $user_entered_verify_code) {
  echo "Your code is correct.";
}
else {
  echo "Your code is incorrect.";
}

echo PHP_EOL;
