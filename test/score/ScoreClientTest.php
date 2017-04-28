<?php

namespace telesign\sdk\score;

use telesign\sdk\Example;
use telesign\sdk\ClientTest;

final class ScoreClientTest extends ClientTest {

  const EXAMPLE_PHONE_NUMBER = Example::PHONE_NUMBER;
  const EXAMPLE_ACCOUNT_LIFECYCLE_EVENT = Example::ACCOUNT_LIFECYCLE_EVENT;

  function getRequestExamples () {
    return [
      [
        ScoreClient::class,
        "score",
        [
          self::EXAMPLE_PHONE_NUMBER,
          self::EXAMPLE_ACCOUNT_LIFECYCLE_EVENT,
          [ "optional_param" => "123" ]
        ],
        self::EXAMPLE_REST_ENDPOINT . "/v1/score/" . self::EXAMPLE_PHONE_NUMBER,
        [
          "account_lifecycle_event" => self::EXAMPLE_ACCOUNT_LIFECYCLE_EVENT,
          "optional_param" => "123"
        ]
      ]
    ];
  }

}
