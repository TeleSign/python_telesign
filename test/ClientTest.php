<?php

namespace telesign\sdk;

use PHPUnit\Framework\TestCase;
use telesign\sdk\Example;
use GuzzleHttp\Handler\MockHandler;
use GuzzleHttp\Psr7\Response;

use Psr\Http\Message\RequestInterface;

abstract class ClientTest extends TestCase {
  
  const EXAMPLE_CUSTOMER_ID = Example::CUSTOMER_ID;
  const EXAMPLE_SECRET_KEY = Example::SECRET_KEY;
  const EXAMPLE_API_HOST = Example::API_HOST;
  
  abstract function getRequestExamples();
  
  /**
  * @dataProvider getRequestExamples
  */
  function testRequestFormat ($client, $method, $args, $expected_url, $expected_fields) {
    $mock = new MockHandler([ new Response() ]);
    $client = new $client(
      self::EXAMPLE_CUSTOMER_ID, self::EXAMPLE_SECRET_KEY, self::EXAMPLE_API_HOST, 10, null, $mock
    );
    $client->$method(...$args);
    $request = $mock->getLastRequest();

    $this->assertInstanceOf(RequestInterface::class, $request);
    $this->assertEquals($expected_url, $request->getUri());

    parse_str($request->getBody()->getContents(), $actual_fields);

    $this->assertEquals($expected_fields, $actual_fields);
  }
  
}