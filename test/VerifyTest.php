<?php

/*
  Copyright (c) TeleSign Corporation 2012.
  License: MIT
  Support email address "support@telesign.com"
  Author: lqm1010
 */

require_once("PHPUnit/Autoload.php");
require_once("../telesign/api.class.php");

// load config test file
require_once("config_test.php");

class VerifyTest extends PHPUnit_Framework_TestCase {

	const CUSTOMER_ID = TEST_CUSTOMER_ID;
	const SECRET_KEY = TEST_SECRET_KEY;
	const PHONE_NUMBER = TEST_PHONE_NUMBER;

	public function test_verify_error() {
		$verify = new Verify("Junk", "Fake");

		$result = $verify->call("13102224444");
		$this->assertNotNull($result);
		$this->assertTrue($result['errors']['0']['code'] == -30000);
	}

	public function test_verify_request_call() {
		if (VerifyTest::CUSTOMER_ID == "" || VerifyTest::SECRET_KEY == "" || VerifyTest::PHONE_NUMBER == "") {
			$this->fail("CUSTOMER_ID, SECRET_KEY and PHONE_NUMBER must be set to pass this test");
		}

		$verify = new Verify(VerifyTest::CUSTOMER_ID, VerifyTest::SECRET_KEY);
		$result = $verify->call(VerifyTest::PHONE_NUMBER);
		$this->assertNotNull($result);
		$this->assertTrue(count($result['errors']) == 0);
	}

	public function test_verify_request_call_with_language() {
		if (VerifyTest::CUSTOMER_ID == "" || VerifyTest::SECRET_KEY == "" || VerifyTest::PHONE_NUMBER == "") {
			$this->fail("CUSTOMER_ID, SECRET_KEY and PHONE_NUMBER must be set to pass this test");
		}

		$verify = new Verify(VerifyTest::CUSTOMER_ID, VerifyTest::SECRET_KEY);
		$result = $verify->call(VerifyTest::PHONE_NUMBER, "", "en-US");
		$this->assertNotNull($result);
		$this->assertTrue(count($result['errors']) == 0);
	}

	public function test_verify_request_call_with_all_params() {
		if (VerifyTest::CUSTOMER_ID == "" || VerifyTest::SECRET_KEY == "" || VerifyTest::PHONE_NUMBER == "") {
			$this->fail("CUSTOMER_ID, SECRET_KEY and PHONE_NUMBER must be set to pass this test");
		}

		$verify = new Verify(VerifyTest::CUSTOMER_ID, VerifyTest::SECRET_KEY);
		$result = $verify->call(VerifyTest::PHONE_NUMBER, "12345", "en-US", "keypress", 1, "1234", true);
		$this->assertNotNull($result);
		$this->assertTrue(count($result['errors']) == 0);
	}

	public function test_verify_request_sms() {
		if (VerifyTest::CUSTOMER_ID == "" || VerifyTest::SECRET_KEY == "" || VerifyTest::PHONE_NUMBER == "") {
			$this->fail("CUSTOMER_ID, SECRET_KEY and PHONE_NUMBER must be set to pass this test");
		}

		$verify = new Verify(VerifyTest::CUSTOMER_ID, VerifyTest::SECRET_KEY);
		$result = $verify->sms(VerifyTest::PHONE_NUMBER);
		$this->assertNotNull($result);
		$this->assertTrue(count($result['errors']) == 0);
	}

	public function test_verify_request_sms_with_language() {
		if (VerifyTest::CUSTOMER_ID == "" || VerifyTest::SECRET_KEY == "" || VerifyTest::PHONE_NUMBER == "") {
			$this->fail("CUSTOMER_ID, SECRET_KEY and PHONE_NUMBER must be set to pass this test");
		}

		$verify = new Verify(VerifyTest::CUSTOMER_ID, VerifyTest::SECRET_KEY);
		$result = $verify->sms(VerifyTest::PHONE_NUMBER, "", "en-US");
		$this->assertNotNull($result);
		$this->assertTrue(count($result['errors']) == 0);
	}

	public function test_verify_request_sms_with_all_params() {
		if (VerifyTest::CUSTOMER_ID == "" || VerifyTest::SECRET_KEY == "" || VerifyTest::PHONE_NUMBER == "") {
			$this->fail("CUSTOMER_ID, SECRET_KEY and PHONE_NUMBER must be set to pass this test");
		}

		$verify = new Verify(VerifyTest::CUSTOMER_ID, VerifyTest::SECRET_KEY);
		$result = $verify->sms(VerifyTest::PHONE_NUMBER, "", "en-US", "12345", 'Thanks! Custom code template pass! Code: $$CODE$$');
		$this->assertNotNull($result);
		$this->assertTrue(count($result['errors']) == 0);
	}

	public function test_verify_request_call_with_result() {
		if (VerifyTest::CUSTOMER_ID == "" || VerifyTest::SECRET_KEY == "" || VerifyTest::PHONE_NUMBER == "") {
			$this->fail("CUSTOMER_ID, SECRET_KEY and PHONE_NUMBER must be set to pass this test");
		}

		$verify = new Verify(VerifyTest::CUSTOMER_ID, VerifyTest::SECRET_KEY);
		$result = $verify->call(VerifyTest::PHONE_NUMBER);
		$this->assertNotNull($result);
		$this->assertTrue(count($result['errors']) == 0);

		$reference_id = $result['reference_id'];
		$result_2 = $verify->status($reference_id);
		$this->assertNotNull($result_2);
		$this->assertTrue(count($result_2['errors']) == 0);
	}

	public function test_verify_request_sms_with_result() {
		if (VerifyTest::CUSTOMER_ID == "" || VerifyTest::SECRET_KEY == "" || VerifyTest::PHONE_NUMBER == "") {
			$this->fail("CUSTOMER_ID, SECRET_KEY and PHONE_NUMBER must be set to pass this test");
		}

		$verify = new Verify(VerifyTest::CUSTOMER_ID, VerifyTest::SECRET_KEY);
		$result = $verify->sms(VerifyTest::PHONE_NUMBER);
		$this->assertNotNull($result);
		$this->assertTrue(count($result['errors']) == 0);

		$reference_id = $result['reference_id'];
		$result_2 = $verify->status($reference_id);
		$this->assertNotNull($result_2);
		$this->assertTrue(count($result_2['errors']) == 0);
	}

}
