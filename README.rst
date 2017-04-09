========
TeleSign
========

TeleSign provides the world’s most comprehensive approach to account security for Web and mobile applications.

For more information about TeleSign, visit the `TeleSign website <http://www.TeleSign.com>`_.

TeleSign REST API: Ruby SDK
---------------------------

**TeleSign web services** conform to the `REST Web Service Design Model
<http://en.wikipedia.org/wiki/Representational_state_transfer>`_. Services are exposed as URI-addressable resources
through the set of *RESTful* procedures in our **TeleSign REST API**.

The **TeleSign Ruby SDK** is a set modules and functions — a *Ruby Library* that wraps the
TeleSign REST API, and it simplifies TeleSign application development in the `Ruby programming language
<https://www.ruby-lang.org>`_. The SDK software is distributed on
`GitHub <https://github.com/TeleSign/ruby_telesign>`_ and also as a Ruby Gem using `Ruby Gems <https://rubygems.org>`_.

Documentation
-------------

Detailed documentation for TeleSign REST APIs is available in the `Developer Portal <https://developer.telesign.com/>`_.

Installation
------------

To install the TeleSign Enterprise Ruby SDK:

.. code-block:: bash

    $ gem build telesignenterprise.gemspec && gem install telesignenterprise-[version].gem

Alternatively, you can download the project source, and execute **gem build telesign.gemspec && gem install telesign-[version].gem**.

Ruby Code Example: Verify SMS
-----------------------------

Here's a basic code example with JSON response.

.. code-block:: ruby

    require 'telesignenterprise'

    customer_id = 'customer_id'
    secret_key = 'secret_key'

    phone_number = 'phone_number'

    verify_client = TelesignEnterprise::VerifyClient.new(customer_id, secret_key)
    response = verify_client.sms(phone_number)

.. code-block:: javascript

    {"errors"=>[],
     "reference_id"=>"B56A497C9A74016489525132F8840634",
     "resource_uri"=>"/v1/verify/B56A497C9A74016489525132F8840634",
     "status"=> {"code"=>290,
       "description"=>"Message in progress",
       "updated_on"=>"2017-03-03T04:13:14.028347Z"}
     "sub_resource"=>"sms",
     "verify"=>{"code_entered"=>"", "code_state"=>"UNKNOWN"}}

For more examples, see the examples folder or visit `TeleSign Developer Portal <https://developer.telesign.com/>`_.

Authentication
--------------

You will need a Customer ID and API Key in order to use TeleSign’s REST API. If you are already a customer and need an
API Key, you can generate one in `TelePortal <https://teleportal.telesign.com>`_.

Testing
-------

To run the Ruby SDK test suite, execute **rake test**.
