<?php

namespace telesign\enterprise\sdk\telebureau;

use telesign\enterprise\sdk\Example;
use PHPUnit\Framework\TestCase;
use GuzzleHttp\Handler\MockHandler;
use GuzzleHttp\Psr7\Response;

use Psr\Http\Message\RequestInterface;

final class TeleBureauClientTest extends TestCase {

  const EXAMPLE_CUSTOMER_ID = Example::CUSTOMER_ID;
  const EXAMPLE_SECRET_KEY = Example::SECRET_KEY;
  const EXAMPLE_API_HOST = Example::API_HOST;
  const EXAMPLE_PHONE_NUMBER = Example::PHONE_NUMBER;
  const EXAMPLE_UCID = Example::UCID;
  const EXAMPLE_REFERENCE_ID = Example::REFERENCE_ID;
  const EXAMPLE_LABEL = "bad";

  /**
   * @dataProvider getRequestExamples
   */
  function testRequestFormat ($data) {
    $mock = new MockHandler([ new Response() ]);
    $client = new TeleBureauClient(
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
        "method" => "create",
        "args" => [
          [
            "phone_number" => self::EXAMPLE_PHONE_NUMBER,
            "label" => self::EXAMPLE_LABEL,
            "ucid" => self::EXAMPLE_UCID
          ]
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST. "/v1/telebureau/event",
          "fields" => [
            "phone_number" => self::EXAMPLE_PHONE_NUMBER,
            "label" => self::EXAMPLE_LABEL,
            "ucid" => self::EXAMPLE_UCID
          ]
        ]
      ]],
      [[
        "method" => "retrieve",
        "args" => [
          self::EXAMPLE_REFERENCE_ID,
          [
            "phone_number" => self::EXAMPLE_PHONE_NUMBER,
            "label" => self::EXAMPLE_LABEL,
            "ucid" => self::EXAMPLE_UCID
          ]
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST . "/v1/telebureau/event/". self::EXAMPLE_REFERENCE_ID . "?" . http_build_query([
            "phone_number" => self::EXAMPLE_PHONE_NUMBER,
            "label" => self::EXAMPLE_LABEL,
            "ucid" => self::EXAMPLE_UCID
          ], '', '&'),
          "fields" => []
        ]
      ]],
      [[
        "method" => "delete",
        "args" => [
          self::EXAMPLE_REFERENCE_ID,
          [
            "phone_number" => self::EXAMPLE_PHONE_NUMBER,
            "label" => self::EXAMPLE_LABEL,
            "ucid" => self::EXAMPLE_UCID
          ]
        ],
        "request" => [
          "uri" => self::EXAMPLE_API_HOST . "/v1/telebureau/event/". self::EXAMPLE_REFERENCE_ID . "?" . http_build_query([
            "phone_number" => self::EXAMPLE_PHONE_NUMBER,
            "label" => self::EXAMPLE_LABEL,
            "ucid" => self::EXAMPLE_UCID
          ], '', '&'),
          "fields" => []
        ]
      ]],
    ];
  }

}
