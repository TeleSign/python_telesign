.. image:: https://raw.github.com/TeleSign/python_telesign/master/python_banner.jpg
       :target: https://standard.telesign.com

.. image:: https://img.shields.io/travis/TeleSign/python_telesign.svg
       :target: https://travis-ci.org/TeleSign/python_telesign

.. image:: https://img.shields.io/codecov/c/github/TeleSign/python_telesign.svg
       :target: https://codecov.io/gh/TeleSign/python_telesign

.. image:: https://img.shields.io/pypi/v/telesign.svg
       :target: https://pypi.python.org/pypi/telesign

.. image:: https://img.shields.io/pypi/l/telesign.svg
       :target: https://github.com/TeleSign/python_telesign/blob/master/LICENSE

===================
TeleSign Python SDK
===================

TeleSign is a communications platform as a service (CPaaS) company, founded on security. Since 2005, TeleSign has
been a trusted partner to the world’s leading websites and mobile applications, helping secure billions of end-user
accounts. Today, TeleSign’s data-driven, cloud communications platform is changing the way businesses engage with
customers and prevent fraud.

For more information about TeleSign, visit our `website <http://www.TeleSign.com>`_.

Documentation
-------------

Code documentation is included in the SDK. Complete documentation, quick start guides and reference material
for the TeleSign API is available within the `TeleSign Standard Documentation <https://standard.telesign.com/>`_.

Installation
------------

To install the TeleSign Python SDK:

.. code-block:: bash

    $ pip install telesign

Python **2.7+** is required for the TeleSign Python SDK.

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
sample code. We have also made sure that more complicated functions such as generate_telesign_headers can be easily
extracted from the SDK and used 'as is' in your project.

Python Code Example: Messaging
------------------------------

Here is a basic code example with the JSON response.

.. code-block:: python

    from __future__ import print_function
    from telesign.messaging import MessagingClient

    customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
    api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

    phone_number = "phone_number"
    message = "You're scheduled for a dentist appointment at 2:30PM."
    message_type = "ARN"

    messaging_client = MessagingClient(customer_id, api_key)
    response = messaging_client.message(phone_number, message, message_type)

    print(response.json)

.. code-block:: javascript
       
    {'reference_id': 'DGFDF6E11AB86303ASDFD425BE00000657',
     'status': {'code': 103,
        'description': 'Call in progress',
        'updated_on': '2016-12-12T00:39:58.325559Z'}}

For more examples, see the `examples <https://github.com/TeleSign/python_telesign/tree/master/examples>`_ folder or
visit the `TeleSign Standard Documentation <https://standard.telesign.com/>`_.
