<?php

/*
  Copyright (c) TeleSign Corporation 2012.
  License: MIT
  Support email address "support@telesign.com"
  Author: lqm1010
 */

require_once("../telesign/api.class.php");
require_once("config_test.php");

$customer_id = TEST_CUSTOMER_ID;
$secret_key = TEST_SECRET_KEY;

$verify = new Verify($customer_id, $secret_key);

$phone_number = "13103409700";
$result = $verify->call($phone_number);

print_r($result);