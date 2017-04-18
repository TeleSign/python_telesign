.. image:: https://img.shields.io/travis/TeleSign/python_telesign.svg
    :target: https://travis-ci.org/TeleSign/python_telesign

.. image:: https://img.shields.io/pypi/v/telesign.svg
    :target: https://pypi.python.org/pypi/telesign

.. image:: https://img.shields.io/pypi/l/telesign.svg
    :target: https://github.com/TeleSign/python_telesign/blob/master/LICENSE

========
TeleSign
========

TeleSign provides the world’s most comprehensive approach to account security for Web and mobile applications.

For more information about TeleSign, visit the `TeleSign website <http://www.TeleSign.com>`_.

TeleSign REST API: Python SDK
-----------------------------

**TeleSign web services** conform to the `REST Web Service Design Model
<http://en.wikipedia.org/wiki/Representational_state_transfer>`_. Services are exposed as URI-addressable resources
through the set of *RESTful* procedures in our **TeleSign REST API**.

The **TeleSign Python SDK** is a set modules and functions — a *Python Library* that wraps the
TeleSign REST API, and it simplifies TeleSign application development in the `Python programming language
<https://www.python.org>`_. The SDK software is distributed on
`GitHub <https://github.com/TeleSign/python_telesign>`_ and also as a Python Software Package using the
`Python Package Index (PyPI) <http://pypi.python.org/pypi/>`_.

Documentation
-------------

Detailed documentation for TeleSign REST APIs is available in the `Developer Portal <https://developer.telesign.com/>`_.

Installation
------------

To install the TeleSign Python SDK:

.. code-block:: bash

    $ pip install telesign

Alternatively, you can download the project source, and execute **python setup.py install**.

Python Code Example: Messaging
------------------------------

Here's a basic code example with JSON response.

.. code-block:: python

    from __future__ import print_function
    from telesign.messaging import MessagingClient

    customer_id = "customer_id"
    secret_key = "secret_key"

    phone_number = "phone_number"
    message = "You're scheduled for a dentist appointment at 2:30PM."
    message_type = "ARN"

    messaging_client = MessagingClient(customer_id, secret_key)
    response = messaging_client.message(phone_number, message, message_type)

.. code-block:: javascript
    
    {'reference_id': 'DGFDF6E11AB86303ASDFD425BE00000657',
     'status': {'code': 103,
        'description': 'Call in progress',
        'updated_on': '2016-12-12T00:39:58.325559Z'}}

For more examples, see the examples folder or visit `TeleSign Developer Portal <https://developer.telesign.com/>`_.

Authentication
--------------

You will need a Customer ID and API Key in order to use TeleSign’s REST API. If you are already a customer and need an
API Key, you can generate one in the  `Portal <https://portal.telesign.com>`_.

Testing
-------

The easiest way to run the tests is to install `nose <https://pypi.python.org/pypi/nose>`_ (**pip install nose**) and
run **nosetests** in the root of the distribution. Tests are located in the *test/* directory.