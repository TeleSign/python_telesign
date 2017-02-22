<?php

namespace telesign\enterprise\sdk\verify;

use telesign\enterprise\sdk\Example;
use PHPUnit\Framework\TestCase;
use GuzzleHttp\Handler\MockHandler;
use GuzzleHttp\Psr7\Response;

use Psr\Http\Message\RequestInterface;

final class VerifyClientTest extends TestCase {

  const EXAMPLE_CUSTOMER_ID = Example::CUSTOMER_ID;
  const EXAMPLE_SECRET_KEY = Example::SECRET_KEY;
  const EXAMPLE_API_HOST = Example::API_HOST;
  const EXAMPLE_PHONE_NUMBER = Example::PHONE_NUMBER;
  const EXAMPLE_UCID = Example::UCID;
  const EXAMPLE_REFERENCE_ID = Example::REFERENCE_ID;
  const EXAMPLE_VERIFY_CODE = "1234";

  /**
   * @dataProvider getRequestExamples
   */
  function testRequestFormat ($data) {
    $mock = new MockHandler([ new Response() ]);
    $client = new VerifyClient(
      self::EXAMPLE_CUSTOMER_ID, self::EXAMPLE_SECRET_KEY, self::EXAMPLE_API_HOST, 10, null, $mock
    );
    $client->$data["method"](...$data["args"]);
    $request = $mock->getLastRequest();

    $this->assertInstanceOf(RequestInterface::class, $request);
    $this->assertEquals($data["request"]["uri"], $request->getUri());

    parse_str($request->getBody()->getContents(), $actual_fields);

    $this->assertEquals($data["request"]["fields"], $actual_fields);
  }

  function getRequestExamples () {
    return [
      [[
        "method" => "sms",
        "args" => [
          self::EXAMPLE_PHONE_NUMBER,
          [
            "ucid" => self::EXAMPLE_UCID,
            "verify_code" => self::EXAMPLE_VERIFY_CODE
          ]
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v1/verify/sms",
          "fields" => [
            "ucid" => self::EXAMPLE_UCID,
            "verify_code" => self::EXAMPLE_VERIFY_CODE,
            "phone_number" => self::EXAMPLE_PHONE_NUMBER
          ]
        ]
      ]],
      [[
        "method" => "voice",
        "args" => [
          self::EXAMPLE_PHONE_NUMBER,
          [
            "ucid" => self::EXAMPLE_UCID,
            "verify_code" => self::EXAMPLE_VERIFY_CODE
          ]
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v1/verify/call",
          "fields" => [
            "ucid" => self::EXAMPLE_UCID,
            "verify_code" => self::EXAMPLE_VERIFY_CODE,
            "phone_number" => self::EXAMPLE_PHONE_NUMBER
          ]
        ]
      ]],
      [[
        "method" => "smart",
        "args" => [
          self::EXAMPLE_PHONE_NUMBER,
          self::EXAMPLE_UCID,
          [
            "verify_code" => self::EXAMPLE_VERIFY_CODE
          ]
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v1/verify/smart",
          "fields" => [
            "ucid" => self::EXAMPLE_UCID,
            "verify_code" => self::EXAMPLE_VERIFY_CODE,
            "phone_number" => self::EXAMPLE_PHONE_NUMBER
          ]
        ]
      ]],
      [[
        "method" => "push",
        "args" => [
          self::EXAMPLE_PHONE_NUMBER,
          self::EXAMPLE_UCID,
          [
            "verify_code" => self::EXAMPLE_VERIFY_CODE
          ]
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v2/verify/push",
          "fields" => [
            "ucid" => self::EXAMPLE_UCID,
            "verify_code" => self::EXAMPLE_VERIFY_CODE,
            "phone_number" => self::EXAMPLE_PHONE_NUMBER
          ]
        ]
      ]],
      [[
        "method" => "status",
        "args" => [
          self::EXAMPLE_REFERENCE_ID,
          [
            "optional_param" => "123"
          ]
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST . "/v1/verify/". self::EXAMPLE_REFERENCE_ID . "?optional_param=123",
          "fields" => []
        ]
      ]],
    ];
  }

}
