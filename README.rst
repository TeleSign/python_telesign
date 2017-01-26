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

PHP Code Example: Verify Voice
-------------------------------------

Here's a basic code example with JSON response.

.. code-block:: php

  require __DIR__ . "/vendor/autoload.php";

  use telesign\verify\VerifyClient;

  $phone_number = "13103409700";
  $ucid = "OTHR";
  $verify_code = "1234";
  $customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
  $secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";
  $verify = new VerifyClient($customer_id, $secret_key);
  $result = $verify->voice($phone_number, $ucid, $verify_code);
  print_r($result->json);

.. code-block:: javascript

  {'errors': [],
   'reference_id': 'DGFDF6E11AB86303ASDFD425BE00000657',
   'resource_uri': '/v1/verify/DGFDF6E11AB86303ASDFD425BE00000657',
   'status': {'code': 103,
      'description': 'Call in progress',
      'updated_on': '2016-12-12T00:39:58.325559Z'},
   'sub_resource': 'call',
   'verify': {'code_state': 'UNKNOWN', 'code_entered': ''}}

Authentication
--------------

You will need a Customer ID and API Key in order to use TeleSign’s REST API. If you are already a customer and need an
API Key, you can generate one in `TelePortal <https://teleportal.telesign.com>`_. If you are not a customer and would
like to get an API Key, please contact `support@telesign.com <mailto:support@telesign.com>`_.

Testing
-------

.. code-block:: bash

  $ composer test
