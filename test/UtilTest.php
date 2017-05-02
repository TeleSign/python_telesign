<?php

namespace telesign\sdk\util;

use PHPUnit\Framework\TestCase;
use telesign\sdk\Example;

final class UtilTest extends TestCase {

  function testToUtcRfc3339 () {
    $now = time();
    $date_rfc3339 = gmdate(DATE_RFC3339, $now);
    $date_iso8601 = date(DATE_ISO8601, $now);
    $this->assertEquals($date_iso8601, toUtcRfc3339($date_rfc3339));
  }

  function testRandomWithNDigits () {
    $n = 7;
    $a = randomWithNDigits($n);
    $b = randomWithNDigits($n);

    $this->assertEquals($n, strlen($a));
    $this->assertTrue(ctype_digit($a));
    $this->assertNotEquals($a, $b);
  }

  function testVerifyTelesignCallbackSignatureCorrect () {
    $api_key = Example::API_KEY;
    $header_value = "B97g3N9lPdVaptvifxRau7bzVAC5hhRBZ6HKXABN744=";
    $json_str = "{'test': 123}";

    $this->assertTrue(verifyTelesignCallbackSignature($api_key, $header_value, $json_str));
  }

  function testVerifyTelesignCallbackSignatureIncorrect () {
    $api_key = Example::API_KEY;
    $header_value = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=";
    $json_str = "{'test': 123}";

    $this->assertFalse(verifyTelesignCallbackSignature($api_key, $header_value, $json_str));
  }

}
