<?php

namespace telesign\enterprise\sdk\phoneid;

use telesign\sdk\Example;
use telesign\sdk\ClientTest;

final class PhoneIdClientTest extends ClientTest {

  const EXAMPLE_PHONE_NUMBER = Example::PHONE_NUMBER;
  const EXAMPLE_UCID = Example::UCID;

  function getRequestExamples () {
    return [
      [
        PhoneIdClient::class,
        "score",
        [
          self::EXAMPLE_PHONE_NUMBER,
          self::EXAMPLE_UCID,
          [ "optional_param" => "123" ]
        ],
        "uri" => self::EXAMPLE_REST_ENDPOINT . "/v1/phoneid/score/" . self::EXAMPLE_PHONE_NUMBER . "?optional_param=123&ucid=" . self::EXAMPLE_UCID,
        []
      ],
      [
        PhoneIdClient::class,
        "contact",
        [
          self::EXAMPLE_PHONE_NUMBER,
          self::EXAMPLE_UCID,
          [ "optional_param" => "123" ]
        ],
        self::EXAMPLE_REST_ENDPOINT. "/v1/phoneid/contact/" . self::EXAMPLE_PHONE_NUMBER . "?optional_param=123&ucid=" . self::EXAMPLE_UCID,
        []
      ],
      [
        PhoneIdClient::class,
        "live",
        [
          self::EXAMPLE_PHONE_NUMBER,
          self::EXAMPLE_UCID,
          [ "optional_param" => "123" ]
        ],
        self::EXAMPLE_REST_ENDPOINT. "/v1/phoneid/live/" . self::EXAMPLE_PHONE_NUMBER . "?optional_param=123&ucid=" . self::EXAMPLE_UCID,
        []
      ],
      [
        PhoneIdCLient::class,
        "numberDeactivation",
        [
          self::EXAMPLE_PHONE_NUMBER,
          self::EXAMPLE_UCID,
          [ "optional_param" => "123" ]
        ],
        self::EXAMPLE_REST_ENDPOINT. "/v1/phoneid/number_deactivation/" . self::EXAMPLE_PHONE_NUMBER . "?optional_param=123&ucid=" . self::EXAMPLE_UCID,
        []
      ],
      [
        PhoneIdClient::class,
        "standard",
        [
          self::EXAMPLE_PHONE_NUMBER,
          [ "optional_param" => "123" ]
        ],
        self::EXAMPLE_REST_ENDPOINT. "/v1/phoneid/standard/" . self::EXAMPLE_PHONE_NUMBER . "?optional_param=123",
        []
      ],
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
