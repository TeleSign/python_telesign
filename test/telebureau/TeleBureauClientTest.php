<?php

namespace telesign\enterprise\sdk\telebureau;

use telesign\sdk\Example;
use telesign\sdk\ClientTest;

final class TelebureauClientTest extends ClientTest {

  const EXAMPLE_PHONE_NUMBER = Example::PHONE_NUMBER;
  const EXAMPLE_UCID = Example::UCID;
  const EXAMPLE_REFERENCE_ID = Example::REFERENCE_ID;
  const EXAMPLE_FRAUD_TYPE = "chargeback";

  function getRequestExamples () {
    return [
      [
        TelebureauClient::class,
        "createEvent",
        [
          [
            "phone_number" => self::EXAMPLE_PHONE_NUMBER,
            "fraud_type" => self::EXAMPLE_FRAUD_TYPE,
            "optional_param" => "123"
          ]
        ],
        self::EXAMPLE_REST_ENDPOINT. "/v1/telebureau/event",
        [
          "phone_number" => self::EXAMPLE_PHONE_NUMBER,
          "fraud_type" => self::EXAMPLE_FRAUD_TYPE,
          "optional_param" => "123"
        ]
      ],
      [
        TelebureauClient::class,
        "retrieveEvent",
        [
          self::EXAMPLE_REFERENCE_ID,
          [
            "optional_param" => "123"
          ]
        ],
        self::EXAMPLE_REST_ENDPOINT . "/v1/telebureau/event/". self::EXAMPLE_REFERENCE_ID . "?optional_param=123",
        []
      ],
      [
        TelebureauClient::class,
        "deleteEvent",
        [
          self::EXAMPLE_REFERENCE_ID,
          [
            "optional_param" => "123"
          ]
        ],
        self::EXAMPLE_REST_ENDPOINT . "/v1/telebureau/event/". self::EXAMPLE_REFERENCE_ID . "?optional_param=123",
        []
      ],
    ];
  }

}
