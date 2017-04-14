<?php

namespace telesign\sdk\messaging;

use telesign\sdk\rest\RestClient;

/**
 * TeleSign's Messaging API allows you to easily send SMS messages. You can send alerts, reminders, and notifications,
 * or you can send verification messages containing one-time passcodes (OTP).
 */
class MessagingClient extends RestClient {

  const MESSAGING_RESOURCE = "/v1/messaging";
  const MESSAGING_STATUS_RESOURCE = "/v1/messaging/%s";

  /**
   * Send a message to the target phone_number.
   *
   * See https://developer.telesign.com/docs/messaging-api for detailed API documentation.
   */
  function message ($phone_number, $message, $message_type, array $other = []) {
    return $this->post(self::MESSAGING_RESOURCE, array_merge($other, [
      "phone_number" => $phone_number,
      "message" => $message,
      "message_type" => $message_type
    ]));
  }

  /**
   * Retrieves the current status of the message.
   *
   * See https://developer.telesign.com/docs/messaging-api for detailed API documentation.
   */
  function status ($reference_id, array $params = []) {
    return $this->get(sprintf(self::MESSAGING_STATUS_RESOURCE, $reference_id), $params);
  }

}
