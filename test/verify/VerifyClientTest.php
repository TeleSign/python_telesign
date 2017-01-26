<?php

namespace telesign\sdk\verify;

use telesign\sdk\Example;
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
    $this->assertEquals($data["request"]["body"], $request->getBody());
  }

  function getRequestExamples () {
    $fields = [
      [
        "fields" => [
          "phone_number" => self::EXAMPLE_PHONE_NUMBER,
          "ucid" => self::EXAMPLE_UCID,
          "verify_code" => self::EXAMPLE_VERIFY_CODE
        ],
        "url_encoded_fields" => sprintf(
          "phone_number=%s&ucid=%s&verify_code=%s",
          self::EXAMPLE_PHONE_NUMBER,
          self::EXAMPLE_UCID,
          self::EXAMPLE_VERIFY_CODE
        )
      ],
      [
        "fields" => [
          "verify_code" => self::EXAMPLE_VERIFY_CODE
        ],
        "url_encoded_fields" => "verify_code=" . self::EXAMPLE_VERIFY_CODE
      ]
    ];

    return [
      [[
        "method" => "sms",
        "args" => [ $fields[0]["fields"] ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v1/verify/sms",
          "body" => $fields[0]["url_encoded_fields"]
        ]
      ]],
      [[
        "method" => "voice",
        "args" => [ $fields[0]["fields"] ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v1/verify/call",
          "body" => $fields[0]["url_encoded_fields"]
        ]
      ]],
      [[
        "method" => "smart",
        "args" => [ $fields[0]["fields"] ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v1/verify/smart",
          "body" => $fields[0]["url_encoded_fields"]
        ]
      ]],
      [[
        "method" => "push",
        "args" => [ $fields[0]["fields"] ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v2/verify/push",
          "body" => $fields[0]["url_encoded_fields"]
        ]
      ]],
      [[
        "method" => "status",
        "args" => [
          self::EXAMPLE_REFERENCE_ID,
          $fields[1]["fields"]
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST . "/v1/verify/". self::EXAMPLE_REFERENCE_ID . "?{$fields[1]["url_encoded_fields"]}",
          "body" => ""
        ]
      ]],
    ];
  }

}
