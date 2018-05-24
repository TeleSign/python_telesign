<?php

namespace telesign\enterprise\sdk\score;

use telesign\sdk\score\ScoreClient as _ScoreClient;

/**
 * Score provides risk information about a specified phone number,
 */
class ScoreClient extends _ScoreClient {

  function __construct ($customer_id, $api_key, $rest_endpoint = "https://rest-ww.telesign.com", ...$other) {
    parent::__construct($customer_id, $api_key, $rest_endpoint, ...$other);
  }

}