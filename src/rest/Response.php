<?php

namespace telesign\sdk\rest;

use Psr\Http\Message\ResponseInterface;

/**
 * A simple HTTP Response object to abstract the underlying library response
 *
 * @param \Psr\Http\Message\ResponseInterface $response A PSR-7 response object
 */
class Response {

  public $status_code;
  public $headers;
  public $body;
  public $ok;
  public $json;

  function __construct (ResponseInterface $response) {
    $this->status_code = $response->getStatusCode();
    $this->headers = $response->getHeaders();
    $this->body = $response->getBody()->getContents();
    $this->ok = $this->status_code < 400;
    $this->json = json_decode($this->body, true);
  }

}
