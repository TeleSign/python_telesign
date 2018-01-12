.. image:: https://raw.github.com/TeleSign/php_telesign/master/php_banner.jpg
    :target: https://developer.telesign.com

.. raw:: html

    <br>

.. image:: https://img.shields.io/travis/TeleSign/php_telesign/master.svg
    :target: https://travis-ci.org/TeleSign/php_telesign

.. image:: https://img.shields.io/codecov/c/github/TeleSign/php_telesign.svg
    :target: https://codecov.io/gh/TeleSign/php_telesign

.. image:: https://img.shields.io/packagist/v/telesign/telesign.svg
    :target: https://packagist.org/packages/telesign/telesign

.. image:: https://img.shields.io/github/license/TeleSign/php_telesign.svg
    :target: https://github.com/TeleSign/php_telesign/blob/master/LICENSE

================
TeleSign PHP SDK
================

TeleSign is a communications platform as a service (CPaaS) company, founded on security. Since 2005, TeleSign has
been a trusted partner to the world’s leading websites and mobile applications, helping secure billions of end-user
accounts. Today, TeleSign’s data-driven, cloud communications platform is changing the way businesses engage with
customers and prevent fraud.

For more information about TeleSign, visit our `website <http://www.TeleSign.com>`_.

Documentation
-------------

Code documentation is included in the SDK. Complete documentation, quick start guides and reference material
for the TeleSign API is available within the `TeleSign Developer Center <https://developer.telesign.com/>`_.

Installation
------------

.. code-block:: bash

  $ composer require telesign/telesign

PHP **5.6+** is required for the TeleSign PHP SDK.

Authentication
--------------

You will need a Customer ID and API Key in order to use TeleSign’s API. If you already have an account you can retrieve
them from your account dashboard within the `Portal <https://portal.telesign.com/login>`_. If you have not signed up
yet, sign up `here <https://portal.telesign.com/signup>`_.

Dependencies
------------

We make use of popular, feature-rich and well-tested open-source libraries to perform the underlying functionality of
the SDK. These dependencies are managed by the community accepted package manager. If you are unable to add these
additional third party dependencies to your project we have ensured that the SDK code is easy to read and can serve as
sample code. We have also made sure that more complicated functions such as generateTelesignHeaders can be easily
extracted from the SDK and used 'as is' in your project.

PHP Code Example: Messaging
---------------------------

Here is a basic code example with the JSON response.

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

For more examples, see the `examples <https://github.com/TeleSign/php_telesign/tree/master/examples>`_ folder or
visit the `TeleSign Developer Center <https://developer.telesign.com/>`_.
