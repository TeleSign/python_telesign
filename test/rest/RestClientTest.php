<?php

namespace telesign\sdk\rest;

use telesign\sdk\Example;
use PHPUnit\Framework\TestCase;
use telesign\sdk\rest\Response as TelesignSdkRestResponse;
use GuzzleHttp\Handler\MockHandler;
use GuzzleHttp\Psr7\Response;
use GuzzleHttp\Client;

use Psr\Http\Message\RequestInterface;

final class RestClientTest extends TestCase {

  const EXAMPLE_CUSTOMER_ID = Example::CUSTOMER_ID;
  const EXAMPLE_API_KEY = Example::API_KEY;
  const EXAMPLE_REST_ENDPOINT = Example::REST_ENDPOINT;
  const EXAMPLE_RESOURCE = "/v1/resource";
  const EXAMPLE_FIELDS = [ "test" => "param" ];
  const EXAMPLE_URL_ENCODED_FIELDS = "test=param";
  const EXAMPLE_DATE = "Mon, 27 Jan 2017 23:59:59 GMT";
  const EXAMPLE_NONCE = "5ffb243e-8e2a-4a7b-bf22-2b3925b3d6ef";

  /**
   * @dataProvider getRequestExamples
   */
  function testTelesignHeadersMatchExample ($data) {
    $actual_headers = RestClient::generateTelesignHeaders(
      self::EXAMPLE_CUSTOMER_ID,
      self::EXAMPLE_API_KEY,
      $data["method_name"],
      self::EXAMPLE_RESOURCE,
      self::EXAMPLE_URL_ENCODED_FIELDS,
      self::EXAMPLE_DATE,
      self::EXAMPLE_NONCE
    );

    $expected_headers = [
      "Authorization" => $data["request"]["headers"]["authorization"],
      "Date" => self::EXAMPLE_DATE,
      "Content-Type" => $data["request"]["headers"]["content-type"],
      "x-ts-auth-method" => "HMAC-SHA256",
      "x-ts-nonce" => self::EXAMPLE_NONCE
    ];

    $this->assertEquals($expected_headers, $actual_headers);
  }

  function getRequestExamples () {
    return [
      [[
        "method_name" => "POST",
        "request" => [
          "uri" => self::EXAMPLE_REST_ENDPOINT . self::EXAMPLE_RESOURCE,
          "body" => self::EXAMPLE_URL_ENCODED_FIELDS,
          "headers" => [
            "authorization" => "TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:smUGWEeXtN+WT1s/y1Ssp4Q2Acm/ultPxkgl/GjqSsA=",
            "content-type" => "application/x-www-form-urlencoded",
          ]
        ]
      ]],
      [[
        "method_name" => "GET",
        "request" => [
          "uri" => self::EXAMPLE_REST_ENDPOINT . self::EXAMPLE_RESOURCE . "?" . self::EXAMPLE_URL_ENCODED_FIELDS,
          "body" => "",
          "headers" => [
            "authorization" => "TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:YgzQt6LcuBDSUeTpE4SASXcSAKAm1eL5TWetbxhXJxg=",
            "content-type" => ""
          ]
        ]
      ]],
      [[
        "method_name" => "PUT",
        "request" => [
          "uri" => self::EXAMPLE_REST_ENDPOINT . self::EXAMPLE_RESOURCE,
          "body" => self::EXAMPLE_URL_ENCODED_FIELDS,
          "headers" => [
            "authorization" => "TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:ccNQP7Tdwsfqx/Sdz/MmZuhFh+z0z/Bj+OcwDhbTT0s=",
            "content-type" => "application/x-www-form-urlencoded"
          ]
        ]
      ]],
      [[
        "method_name" => "DELETE",
        "request" => [
          "uri" => self::EXAMPLE_REST_ENDPOINT . self::EXAMPLE_RESOURCE . "?" . self::EXAMPLE_URL_ENCODED_FIELDS,
          "body" => "",
          "headers" => [
            "authorization" => "TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:ODT8s51qSdrS2pKbtrKIu76gQJf2h0hDz8nJ5ho0/6w=",
            "content-type" => ""
          ]
        ]
      ]]
    ];
  }

  /**
   * @dataProvider getTelesignHeadersAffectedByOptionalArguments
   */
  function testGeneratesTelesignHeadersAffectedByOptionalArguments ($header_name) {
    $headers = RestClient::generateTelesignHeaders(
      self::EXAMPLE_CUSTOMER_ID,
      self::EXAMPLE_API_KEY,
      "POST",
      self::EXAMPLE_RESOURCE,
      self::EXAMPLE_URL_ENCODED_FIELDS
    );

    $this->assertArrayHasKey($header_name, $headers);
    $this->assertNotEmpty($headers[$header_name]);
  }

  function getTelesignHeadersAffectedByOptionalArguments () {
    return [ [ "Date" ], [ "x-ts-nonce" ] ];
  }

  function testUserAgentMatchesFormat () {
    $mock = new MockHandler([ new Response() ]);

    $client = new RestClient(
      self::EXAMPLE_CUSTOMER_ID, self::EXAMPLE_API_KEY, self::EXAMPLE_REST_ENDPOINT, 10, null, $mock
    );
    $client->get(self::EXAMPLE_RESOURCE);

    $user_agent = $mock->getLastRequest()->getHeader("user-agent")[0];
    $php_version = PHP_VERSION;
    $guzzle_version = Client::VERSION;
    $pattern = "`^TeleSignSDK/php-v?\d.+ PHP/$php_version Guzzle/$guzzle_version$`";

    $this->assertRegExp($pattern, $user_agent);
  }

  /**
   * @dataProvider getRequestExamples
   */
  function testSendsRequest ($data) {
    $mock = new MockHandler([ new Response() ]);

    $client = new RestClient(
      self::EXAMPLE_CUSTOMER_ID, self::EXAMPLE_API_KEY, self::EXAMPLE_REST_ENDPOINT, 10, null, $mock
    );
    $client->{$data["method_name"]}(
      self::EXAMPLE_RESOURCE, self::EXAMPLE_FIELDS, self::EXAMPLE_DATE, self::EXAMPLE_NONCE
    );

    $request = $mock->getLastRequest();

    $this->assertInstanceOf(RequestInterface::class, $request);
    $this->assertEquals($data["request"]["uri"], $request->getUri());
    $this->assertTrue($request->hasHeader("authorization"));
    $this->assertEquals($data["request"]["headers"]["authorization"], $request->getHeader("authorization")[0]);
    $this->assertEquals($data["request"]["body"], $request->getBody());
  }

  /**
   * @dataProvider getRequestExamples
   */
  function testReturnsResponse ($data) {
    $mock = new MockHandler([ new Response() ]);

    $client = new RestClient(
      self::EXAMPLE_CUSTOMER_ID, self::EXAMPLE_API_KEY, self::EXAMPLE_REST_ENDPOINT, 10, null, $mock
    );
    $response = $client->{$data["method_name"]}(
      self::EXAMPLE_RESOURCE, self::EXAMPLE_FIELDS, self::EXAMPLE_DATE, self::EXAMPLE_NONCE
    );

    $this->assertInstanceOf(TelesignSdkRestResponse::class, $response);
  }

}
