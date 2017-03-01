========
TeleSign
========

TeleSign provides the world’s most comprehensive approach to account security for Web and mobile applications.

For more information about TeleSign, visit the `TeleSign website <http://www.TeleSign.com>`_.

TeleSign Web Services: Enterprise PHP SDK
-----------------------------------------

**TeleSign web services** conform to the `REST Web Service Design Model
<http://en.wikipedia.org/wiki/Representational_state_transfer>`_. Services are exposed as URI-addressable resources
through the set of *RESTful* procedures in our **TeleSign REST API**.

The **TeleSign PHP SDK** is a PHP library that provides an interface to `TeleSign web services
<https://developer.telesign.com/docs/getting-started-with-the-rest-api/>`_.

The **TeleSign Enterprise PHP SDK** is a PHP library that provides support for additional REST endpoints.

You can differentiate between the two easily by the *enterprise* label that you'll find in the documentation.

Documentation
-------------

Detailed documentation for TeleSign REST APIs is available in the `Developer Portal <https://developer.telesign.com/>`_.

Installation
------------

This library can be installed as a Composer package. You only have to update your project's `composer.json` with its containing repository because it's not Packagist.

.. code-block:: bash

  $ composer repositories.telesign/telesignenterprise vcs ssh://git@github.com/TeleSign/php_telesign_enterprise

Then you can run from your terminal the expected:

.. code-block:: bash

  $ composer require telesign/telesignenterprise

PHP Code Example: Verify SMS
-------------------------------------

Here's a basic code example with JSON response.

.. code-block:: php

  require __DIR__ . "/vendor/autoload.php";

  use telesign\enterprise\sdk\verify\VerifyClient;

  $customer_id = "customer_id";
  $secret_key = "secret_key";

  $phone_number = "phone_number";

  $verify = new VerifyClient($customer_id, $secret_key);
  $response = $verify->sms($phone_number);

  print_r($response->json);

.. code-block::

  Array
  (
    [resource_uri] => /v1/verify/356A273D5EFC08049043921C89E7872E
    [reference_id] => 356A273D5EFC08049043921C89E7872E
    [sub_resource] => sms
    [errors] => Array
        (
        )

    [verify] => Array
        (
            [code_state] => UNKNOWN
            [code_entered] =>
        )

    [status] => Array
        (
            [updated_on] => 2017-03-01T12:19:11.459049Z
            [code] => 290
            [description] => Message in progress
        )

  )

For more examples, see the examples folder or visit `TeleSign Developer Portal <https://developer.telesign.com/>`_.

Authentication
--------------

You will need a Customer ID and API Key in order to use TeleSign’s REST API. If you are already a customer and need an
API Key, you can generate one in `TelePortal <https://teleportal.telesign.com>`_. If you are not a customer and would
like to get an API Key, please contact `support@telesign.com <mailto:support@telesign.com>`_.

Testing
-------

.. code-block:: bash

  $ composer test
