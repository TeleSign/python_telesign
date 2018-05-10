<?php

namespace telesign\sdk;

use PHPUnit\Framework\TestCase;
use telesign\sdk\Example;
use GuzzleHttp\Handler\MockHandler;
use GuzzleHttp\Psr7\Response;

use Psr\Http\Message\RequestInterface;

abstract class ClientTest extends TestCase {
  
  const EXAMPLE_CUSTOMER_ID = Example::CUSTOMER_ID;
  const EXAMPLE_API_KEY = Example::API_KEY;
  const EXAMPLE_REST_ENDPOINT = Example::REST_ENDPOINT;
  
  abstract function getRequestExamples();
  
  /**
  * @dataProvider getRequestExamples
  */
  function testRequestFormat ($client, $method, $args, $expected_url, $expected_fields) {
    $mock = new MockHandler([ new Response() ]);
    $client = new $client(
      self::EXAMPLE_CUSTOMER_ID, self::EXAMPLE_API_KEY, self::EXAMPLE_REST_ENDPOINT, 10, null, $mock
    );
    $client->$method(...$args);
    $request = $mock->getLastRequest();

    $this->assertInstanceOf(RequestInterface::class, $request);
    $this->assertEquals($expected_url, $request->getUri());

    if ($request->getHeaderLine('Content-Type') == "application/json") {
      $actual_fields = $request->getBody()->getContents();
    } else {
      parse_str($request->getBody()->getContents(), $actual_fields );
    }
    
    $this->assertEquals($expected_fields, $actual_fields);
  }
  
}