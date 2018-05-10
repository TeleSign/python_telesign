<?php

namespace telesign\sdk\phoneid;

use telesign\sdk\Example;
use telesign\sdk\ClientTest;

final class PhoneIdClientTest extends ClientTest {

  const EXAMPLE_REFERENCE_ID = Example::REFERENCE_ID;
  const EXAMPLE_PHONE_NUMBER = Example::PHONE_NUMBER;
  
  function getRequestExamples () {
    return [
      [
        PhoneIdClient::class,
        "phoneid",
        [
          self::EXAMPLE_PHONE_NUMBER,
          [ "optional_param" => "123" ]
        ],
        "uri" => self::EXAMPLE_REST_ENDPOINT . "/v1/phoneid/" . self::EXAMPLE_PHONE_NUMBER,
        '{"optional_param":"123"}'
      ],
      [
        PhoneIdClient::class,
        "phoneid",
        [
          self::EXAMPLE_PHONE_NUMBER,
        ],
        "uri" => self::EXAMPLE_REST_ENDPOINT . "/v1/phoneid/" . self::EXAMPLE_PHONE_NUMBER,
        "{}",
      ]
    ];
  }

}
