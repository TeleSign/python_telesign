<?php

namespace telesign\enterprise\sdk\telebureau;

use telesign\sdk\rest\RestClient;

/**
 * TeleBureau is a service is based on TeleSign's watchlist, which is a proprietary database containing verified phone
 * numbers of users known to have committed online fraud. TeleSign crowd-sources this information from its customers.
 * Participation is voluntary, but you have to contribute in order to benefit.
 */
class TelebureauClient extends RestClient {

  const TELEBUREAU_CREATE_RESOURCE = "/v1/telebureau/event";
  const TELEBUREAU_RETRIEVE_RESOURCE = "/v1/telebureau/event/%s";
  const TELEBUREAU_DELETE_RESOURCE = "/v1/telebureau/event/%s";

  function __construct ($customer_id, $secret_key, $api_host = "https://rest-ww.telesign.com", ...$other) {
    parent::__construct($customer_id, $secret_key, $api_host, ...$other);
  }

  /**
   * Creates a telebureau event corresponding to supplied data.
   *
   * See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
   */
  function create (array $fields) {
    return $this->post(self::TELEBUREAU_CREATE_RESOURCE, $fields);
  }

  /**
   * Retrieves the fraud event status. You make this call in your web application after completion of create
   * transaction for a telebureau event.
   *
   * See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
   */
  function retrieve ($reference_id, array $fields = []) {
    return $this->get(sprintf(self::TELEBUREAU_RETRIEVE_RESOURCE, $reference_id), $fields);
  }

  /**
   * Deletes a previously submitted fraud event. You make this call in your web application after completion of the
   * create transaction for a telebureau event.
   *
   * See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
   */
  function delete ($reference_id, array $fields = []) {
    return parent::delete(sprintf(self::TELEBUREAU_DELETE_RESOURCE, $reference_id), $fields);
  }

}
