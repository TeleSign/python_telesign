<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\voice\VoiceClient;
use function telesign\sdk\util\randomWithNDigits;

$customer_id = "customer_id";
$secret_key = "secret_key";

$phone_number = "phone_number";
$verify_code = randomWithNDigits(5);
$message = sprintf('Hello, your code is %1$s. Once again, your code is %1$s. Goodbye.',
  join(", ", str_split($verify_code)));
$message_type = "OTP";

$voice = new VoiceClient($customer_id, $secret_key);
$response = $voice->call($phone_number, $message, $message_type);

echo "Please enter the verification code you were sent: ";

$user_entered_verify_code = trim(fgets(STDIN));

if ($verify_code == $user_entered_verify_code) {
  echo "Your code is correct.";
}
else {
  echo "Your code is incorrect.";
}
