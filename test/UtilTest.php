<?php

namespace telesign\sdk\util;

use PHPUnit\Framework\TestCase;
use telesign\sdk\Example;
use GuzzleHttp\Psr7\Request;

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
    $this->assertNotEquals($a, $b);
  }

  function testVerifyTelesignCallback () {
    $secret_key = Example::SECRET_KEY;
    $expected_header_value = "4NzBWLbUiX4doPp5ls4rBNSZdTBO+LBo1adwJeaLt04=";
    $json_str = json_encode([
      "status" => [
        "updated_on" => "2016-07-08T20:52:46.417428Z",
        "code" => 200,
        "description" => "Delivered to handset"
      ],
      "submit_timestamp" => "2016-07-08T20:52:41.203000Z",
      "errors" => [],
      "verify" => [
        "code_state" => "UNKNOWN",
        "code_entered" => null
      ],
      "sub_resource" => "sms",
      "reference_id" => "2557312299CC1304904080F4BE17BFB4"
    ]);
    $request = new Request("POST", "https://httpbin.org/post", [
      "X-TS-Authorization" => $expected_header_value
    ]);

    $this->assertTrue(verifyTelesignCallback($secret_key, $request->getHeaders(), $json_str));
  }

}
