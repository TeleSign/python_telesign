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

class PhoneIdTest extends PHPUnit_Framework_TestCase {

	const CUSTOMER_ID = TEST_CUSTOMER_ID;
	const SECRET_KEY = TEST_SECRET_KEY;
	const PHONE_NUMBER = TEST_PHONE_NUMBER;

	public function test_phoneid_error() {
		$phoneid = new PhoneId("Junk", "Fake");

		$result_1 = $phoneid->standard("13102224444");
		$this->assertNotNull($result_1);
		$this->assertTrue($result_1['errors']['0']['code'] == -30000);

		$result_2 = $phoneid->score("13102224444", "BACS");
		$this->assertNotNull($result_2);
		$this->assertTrue($result_2['errors']['0']['code'] == -30000);

		$result_3 = $phoneid->contact("13102224444", "BACS");
		$this->assertNotNull($result_3);
		$this->assertTrue($result_3['errors']['0']['code'] == -30000);

		$result_4 = $phoneid->live("13102224444", "BACS");
		$this->assertNotNull($result_4);
		$this->assertTrue($result_4['errors']['0']['code'] == -30000);
	}

	public function test_phoneid_standard() {
		if (PhoneIdTest::CUSTOMER_ID == "" || PhoneIdTest::SECRET_KEY == "") {
			$this->fail("CUSTOMER_ID and SECRET_KEY must be set to pass this test");
		}

		$phoneid = new PhoneId(PhoneIdTest::CUSTOMER_ID, PhoneIdTest::SECRET_KEY);
		$result = $phoneid->standard("13102224444");
		$this->assertNotNull($result);

		$this->assertTrue(count($result['errors']) == 0);
		$this->assertTrue($result['status']['code'] == 300);
	}

	public function test_phoneid_score() {
		if (PhoneIdTest::CUSTOMER_ID == "" || PhoneIdTest::SECRET_KEY == "") {
			$this->fail("CUSTOMER_ID and SECRET_KEY must be set to pass this test");
		}

		$phoneid = new PhoneId(PhoneIdTest::CUSTOMER_ID, PhoneIdTest::SECRET_KEY);
		$result = $phoneid->score("13105551234", "BACS");
		$this->assertNotNull($result);
		$this->assertTrue(count($result['errors']) == 0);
		$this->assertTrue($result['status']['code'] == 300);
		$this->assertTrue(strlen($result['risk']['level']) > 0);
	}

	public function test_phoneid_contact() {
		if (PhoneIdTest::CUSTOMER_ID == "" || PhoneIdTest::SECRET_KEY == "") {
			$this->fail("CUSTOMER_ID and SECRET_KEY must be set to pass this test");
		}

		$phoneid = new PhoneId(PhoneIdTest::CUSTOMER_ID, PhoneIdTest::SECRET_KEY);
		$result = $phoneid->contact("13105551234", "BACS");
		$this->assertNotNull($result);
		$this->assertTrue($result['status']['code'] == 301); // for this fake number we expect a partially completed request
	}

	public function test_phoneid_live_dummy() {
		if (PhoneIdTest::CUSTOMER_ID == "" || PhoneIdTest::SECRET_KEY == "") {
			$this->fail("CUSTOMER_ID and SECRET_KEY must be set to pass this test");
		}

		$phoneid = new PhoneId(PhoneIdTest::CUSTOMER_ID, PhoneIdTest::SECRET_KEY);
		$result = $phoneid->live("13105551234", "BACS");
		$this->assertNotNull($result);
		$this->assertTrue($result['status']['code'] == 301); // for this fake number we expect a partially completed request
	}

	public function test_phoneid_live_real() {
		if (PhoneIdTest::CUSTOMER_ID == "" || PhoneIdTest::SECRET_KEY == "" || PhoneIdTest::PHONE_NUMBER == "") {
			$this->fail("CUSTOMER_ID, SECRET_KEY and PHONE_NUMBER must be set to pass this test");
		}

		$phoneid = new PhoneId(PhoneIdTest::CUSTOMER_ID, PhoneIdTest::SECRET_KEY);
		$result = $phoneid->live(PhoneIdTest::PHONE_NUMBER, "BACS");
		$this->assertTrue($result['status']['code'] == 300);
		$this->assertNotNull($result['live']);
		$this->assertTrue(!empty($result['live']['subscriber_status']));
	}

}
