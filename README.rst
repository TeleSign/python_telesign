.. image:: https://img.shields.io/travis/TeleSign/php_telesign.svg?branch=master
    :target: https://travis-ci.org/TeleSign/php_telesign

.. image:: https://img.shields.io/packagist/v/telesign/telesign.svg
    :target: https://packagist.org/packages/telesign/telesign

.. image:: https://img.shields.io/github/license/TeleSign/php_telesign.svg
    :target: https://github.com/TeleSign/php_telesign/blob/master/LICENSE

========
TeleSign
========

TeleSign provides the world’s most comprehensive approach to account security for Web and mobile applications.

For more information about TeleSign, visit the `TeleSign website <http://www.TeleSign.com>`_.

TeleSign Web Services: PHP SDK
---------------------------------

**TeleSign web services** conform to the `REST Web Service Design Model
<http://en.wikipedia.org/wiki/Representational_state_transfer>`_. Services are exposed as URI-addressable resources
through the set of *RESTful* procedures in our **TeleSign REST API**.

The **TeleSign PHP SDK** is a PHP library that provides an interface to `TeleSign web services
<https://developer.telesign.com/docs/getting-started-with-the-rest-api/>`_.

Documentation
-------------

Detailed documentation for TeleSign REST APIs is available in the `Developer Portal <https://developer.telesign.com/>`_.

Installation
------------

.. code-block:: bash

  $ composer require telesign/telesign

PHP Code Example: Messaging
-------------------------------------

Here's a basic code example with JSON response.

.. code-block:: php

  require __DIR__ . "/vendor/autoload.php";

  use telesign\sdk\messaging\MessagingClient;

  $customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
  $api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

  $phone_number = "phone_number";
  $message = "You're scheduled for a dentist appointment at 2:30PM.";
  $message_type = "ARN";

  $messaging_client = new MessagingClient($customer_id, $api_key);
  $response = $messaging_client->message($phone_number, $message, $message_type);

  print_r($response->json);

.. code-block::

  Array
  (
    [reference_id] => B56A272B0784016889544CB4E6E70011
    [status] => Array
        (
            [code] => 290
            [description] => Message in progress
        )

    [external_id] =>
  )

For more examples, see the examples folder or visit `TeleSign Developer Portal <https://developer.telesign.com/>`_.

Authentication
--------------

You will need a Customer ID and API Key in order to use TeleSign’s REST API. If you are already a customer and need an
API Key, you can generate one in the `Portal <https://portal.telesign.com>`_.

Testing
-------

.. code-block:: bash

  $ composer test
