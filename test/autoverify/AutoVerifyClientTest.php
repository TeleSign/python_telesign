<?php

namespace telesign\sdk\autoverify;

use telesign\sdk\Example;
use PHPUnit\Framework\TestCase;
use GuzzleHttp\Handler\MockHandler;
use GuzzleHttp\Psr7\Response;

use Psr\Http\Message\RequestInterface;

final class AutoVerifyClientTest extends TestCase {

  const EXAMPLE_CUSTOMER_ID = Example::CUSTOMER_ID;
  const EXAMPLE_SECRET_KEY = Example::SECRET_KEY;
  const EXAMPLE_API_HOST = Example::API_HOST;
  const EXAMPLE_XID = "d01c6dbb-99d3-4335-8e22-11a50a2868f2";

  function testRequestFormat () {
    $mock = new MockHandler([ new Response() ]);
    $client = new AutoVerifyClient(
      self::EXAMPLE_CUSTOMER_ID, self::EXAMPLE_SECRET_KEY, self::EXAMPLE_API_HOST, 10, null, $mock
    );
    $client->status(self::EXAMPLE_XID);
    $request = $mock->getLastRequest();

    $this->assertInstanceOf(RequestInterface::class, $request);
    $this->assertEquals(self::EXAMPLE_API_HOST . "/v1/mobile/verification/status/" . self::EXAMPLE_XID, $request->getUri());
    $this->assertEquals("", $request->getBody());
  }

}
