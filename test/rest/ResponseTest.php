<?php

namespace telesign\sdk\rest;

use PHPUnit\Framework\TestCase;
use GuzzleHttp\Psr7\Response as Psr7Response;
use telesign\sdk\rest\Response;

class ResponseTest extends TestCase {

  function testInvalidJsonResolvesToNull () {
    $response = new Response(new Psr7Response(200, [], "{"));
    $this->assertEquals('{', $response->body);
    $this->assertNull($response->json);
  }

  function testValidJsonResolvesArray () {
    $response = new Response(new Psr7Response(200, [], "{}"));
    $this->assertEquals("{}", $response->body);
    $this->assertInternalType("array", $response->json);
  }

}
