.. image:: https://raw.github.com/TeleSign/php_telesign/master/php_banner_enterprise.jpg
    :target: https://developer.telesign.com

===========================
TeleSign Enterprise PHP SDK
===========================

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

This library can be installed as a Composer package. You only have to add its containing repository to your project's `composer.json`.

.. code-block:: bash

  $ composer config repositories.telesign/telesignenterprise vcs ssh://git@github.com/TeleSign/php_telesign_enterprise

Then you can require it as usual.

.. code-block:: bash

  $ composer require telesign/telesignenterprise

Authentication
--------------

You will need a Customer ID and API Key in order to use TeleSign’s REST API. If you are already a customer and need an
API Key, you can retrieve it from `TelePortal <https://teleportal.telesign.com>`_.

Dependencies
------------

We make use of popular, feature-rich and well-tested open-source libraries to perform the underlying functionality of
the SDK. These dependencies are managed by the community accepted package manager. If you are unable to add these
additional third party dependencies to your project we have ensured that the SDK code is easy to read and can serve as
sample code. We have also made sure that more complicated functions such as generateTelesignHeaders can be easily
extracted from the SDK and used 'as is' in your project.

PHP Code Example: Verify SMS
----------------------------

Here is a basic code example with JSON response.

.. code-block:: php

  require __DIR__ . "/vendor/autoload.php";

  use telesign\enterprise\sdk\verify\VerifyClient;

  $customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
  $api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

  $phone_number = "phone_number";

  $verify_client = new VerifyClient($customer_id, $api_key);
  $response = $verify_client->sms($phone_number);

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

For more examples, see the `examples <https://github.com/TeleSign/php_telesign_enterprise/tree/master/examples>`_ folder or
visit the `TeleSign Developer Center <https://developer.telesign.com/>`_.
