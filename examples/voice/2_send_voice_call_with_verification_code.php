<?php

require __DIR__ . "/../../vendor/autoload.php";

use telesign\sdk\voice\VoiceClient;
use function telesign\sdk\util\randomWithNDigits;

$customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
$api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

$phone_number = "phone_number";
$verify_code = randomWithNDigits(5);
$message = sprintf('Hello, your code is %1$s. Once again, your code is %1$s. Goodbye.',
  join(", ", str_split($verify_code)));
$message_type = "OTP";

$voice = new VoiceClient($customer_id, $api_key);
$response = $voice->call($phone_number, $message, $message_type);

echo "Please enter the verification code you were sent: ";

$user_entered_verify_code = trim(fgets(STDIN));

if ($verify_code == $user_entered_verify_code) {
  echo "Your code is correct.";
}
else {
  echo "Your code is incorrect.";
}
