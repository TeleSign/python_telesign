<?php

namespace telesign\sdk\score;

use telesign\sdk\rest\RestClient;

/**
 * Score provides risk information about a specified phone number.
 */
class ScoreClient extends RestClient {

  const SCORE_RESOURCE = "/v1/score/%s";

  /**
   * Score is an API that delivers reputation scoring based on phone number intelligence, traffic patterns, machine
   * learning, and a global data consortium.
   *
   * See https://developer.telesign.com/docs/score-api for detailed API documentation.
   */
  function score ($phone_number, $account_lifecycle_event, array $other = []) {
    return $this->post(sprintf(self::SCORE_RESOURCE, $phone_number), array_merge($other, [
      "account_lifecycle_event" => $account_lifecycle_event
    ]));
  }

}
