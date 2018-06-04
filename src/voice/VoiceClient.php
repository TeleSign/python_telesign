<?php

namespace telesign\enterprise\sdk\voice;

use telesign\sdk\voice\VoiceClient as _VoiceClient;

/**
 * TeleSign's Voice API allows you to easily send voice messages. You can send alerts, reminders, and notifications,
 * or you can send verification messages containing time-based, one-time passcodes (TOTP).
 */
class VoiceClient extends _VoiceClient {

  function __construct ($customer_id, $api_key, $rest_endpoint = "https://rest-ww.telesign.com", ...$other) {
    parent::__construct($customer_id, $api_key, $rest_endpoint, ...$other);
  }
}
