<?php

namespace telesign\enterprise\sdk\phoneid;

use telesign\enterprise\sdk\Example;
use PHPUnit\Framework\TestCase;
use GuzzleHttp\Handler\MockHandler;
use GuzzleHttp\Psr7\Response;

use Psr\Http\Message\RequestInterface;

final class PhoneIdClientTest extends TestCase {

  const EXAMPLE_CUSTOMER_ID = Example::CUSTOMER_ID;
  const EXAMPLE_SECRET_KEY = Example::SECRET_KEY;
  const EXAMPLE_API_HOST = Example::API_HOST;
  const EXAMPLE_PHONE_NUMBER = Example::PHONE_NUMBER;
  const EXAMPLE_UCID = Example::UCID;

  /**
  * @dataProvider getRequestExamples
  */
  function testRequestFormat ($data) {
    $mock = new MockHandler([ new Response() ]);
    $client = new PhoneIdClient(
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
        "method" => "score",
        "args" => [
          self::EXAMPLE_PHONE_NUMBER,
          self::EXAMPLE_UCID
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST . "/v1/phoneid/score/" . self::EXAMPLE_PHONE_NUMBER . "?ucid=" . self::EXAMPLE_UCID,
          "fields" => []
        ]
      ]],
      [[
        "method" => "contact",
        "args" => [
          self::EXAMPLE_PHONE_NUMBER,
          self::EXAMPLE_UCID
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v1/phoneid/contact/" . self::EXAMPLE_PHONE_NUMBER . "?ucid=" . self::EXAMPLE_UCID,
          "fields" => []
        ]
      ]],
      [[
        "method" => "live",
        "args" => [
          self::EXAMPLE_PHONE_NUMBER,
          self::EXAMPLE_UCID
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v1/phoneid/live/" . self::EXAMPLE_PHONE_NUMBER . "?ucid=" . self::EXAMPLE_UCID,
          "fields" => []
        ]
      ]],
      [[
        "method" => "numberDeactivation",
        "args" => [
          self::EXAMPLE_PHONE_NUMBER,
          self::EXAMPLE_UCID
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v1/phoneid/number_deactivation/" . self::EXAMPLE_PHONE_NUMBER . "?ucid=" . self::EXAMPLE_UCID,
          "fields" => []
        ]
      ]],
      [[
        "method" => "standard",
        "args" => [
          self::EXAMPLE_PHONE_NUMBER,
          [ "ucid" => self::EXAMPLE_UCID ]
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v1/phoneid/standard/" . self::EXAMPLE_PHONE_NUMBER . "?ucid=" . self::EXAMPLE_UCID,
          "fields" => []
        ]
      ]]
    ];
  }

}
