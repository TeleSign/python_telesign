========
TeleSign
========

:Info:
    For more information, visit the `TeleSign web site <http://www.TeleSign.com>`_.
    For the latest source code, visit the `TeleSign github repository <http://github.com/TeleSign/ruby_telesign/tree>`_.

:Author:
    Telesign Corp.

---------------------------------
TeleSign Web Services: Ruby SDK
---------------------------------

**TeleSign Web Services** conform to the `REST Web Service Design Model <http://en.wikipedia.org/wiki/Representational_state_transfer>`_. Services are exposed as URI-addressable resources through the set of *RESTful* procedures in our **TeleSign REST API**.

The **TeleSign Ruby SDK** is a set of software development tools—a *Ruby Library* that wraps the TeleSign REST API, and it simplifies TeleSign application development in the `Ruby programming language <https://www.ruby-lang.org/>`_. The SDK software is packaged as a Ruby gem called **telesign**, and is distributed using `Ruby Gems <https://rubygems.org/>`_.

The Ruby Classes
------------------

With just two classes, **Telesign::API** abstracts much of the complexity of the TeleSign REST API.

+------------------------+--------------------------------------------------------------------------+
| Python Class           | Description                                                              |
+========================+==========================================================================+
| Telesign::API::PhoneId | The **PhoneId** class exposes four services that each provide            |
|                        | information about a specified phone number.                              |
|                        |                                                                          |
|                        | *standard*                                                               |
|                        |     Retrieves the standard set of details about the specified phone      |
|                        |     number. This includes the type of phone (e.g., land line or mobile), |
|                        |     and it's approximate geographic location.                            |
|                        | *score*                                                                  |
|                        |     Retrieves a score for the specified phone number. This ranks the     |
|                        |     phone number's "risk level" on a scale from 0 to 1000, so you can    |
|                        |     code your web application to handle particular use cases (e.g., to   |
|                        |     stop things like chargebacks, identity theft, fraud, and spam).      |
|                        | *contact*                                                                |
|                        |     In addition to the information retrieved by *standard*, this service |
|                        |     provides the Name & Address associated with the specified phone      |
|                        |     number.                                                              |
|                        | *live*                                                                   |
|                        |     In addition to the information retrieved by standard, this service   |
|                        |     provides actionable data associated with the specified phone number. |
|                        |                                                                          |
+------------------------+--------------------------------------------------------------------------+
| Telesign::API::Verify  | The **Verify** class exposes four services for sending users a           |
|                        | verification token (a three to five-digit number). You can use this      |
|                        | mechanism to simply test whether you can reach users at the phone number |
|                        | they supplied, or you can have them use the token to authenticate        |
|                        | themselves with your web application. In addition, this class also       |
|                        | exposes a service that allows you to confirm the result of the           |
|                        | authentication.                                                          |
|                        |                                                                          |
|                        | You can use this verification factor in combination with *username*      |
|                        | & *password* to provide *two-factor* authentication for higher           |
|                        | security.                                                                |
|                        |                                                                          |
|                        | *call*                                                                   |
|                        |     Calls the specified phone number, and using speech synthesis—speaks  |
|                        |     the verification code to the user.                                   |
|                        | *sms*                                                                    |
|                        |     Send a text message containing the verification code to the          |
|                        |     specified phone number (supported for mobile phones only).           |
|                        | *smart*                                                                  |
|                        |     Smart will intelligently determines the best service to use based on |
|                        |     the end user device and then attempts to place a call, send an SMS,  |
|                        |     or send a push request.                                              |
|                        | *push*                                                                   |
|                        |     Send a push notification containing the verification code to the     |
|                        |     specified phone number (supported for registered devices only).      |
|                        | *status*                                                                 |
|                        |     Retrieves the verification result. You make this call in your web    |
|                        |     application after users complete the authentication transaction      |
|                        |     (using either a *call* or *sms*).                                    |
|                        |                                                                          |
+------------------------+--------------------------------------------------------------------------+

Installation
------------

With `Ruby Gems <https://github.com/rubygems/rubygems>`_
installed, simply type **gem install telesign** at the command prompt.

Python Code Example: To Verify a Call
-------------------------------------

Here's a basic code example.

::

    require 'telesign'
    phone_number = "13103409700"
    cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
    secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
    verify = Telesign::API::Verify(cust_id, secret_key) # Instantiate a Verify instance object,
    result = verify.call(phone_number) # and use it to call the "call" method.
    p result.body

    {"reference_id"=>"254CADA5F1D40E0090405467DE244D05", "resource_uri"=>"/v1/verify/254CADA5F1D40E0090405467DE244D05", "sub_resource"=>"call", "errors"=>[], "verify"=>{"code_state"=>"UNKNOWN", "code_entered"=>""}, "status"=>{"updated_on"=>"2016-02-29T05:04:06.814381Z", "code"=>103, "description"=>"Call in progress"}}

For more examples, see the Documentation section below.

Authentication
-------------

You will need a Customer ID and API Key in order to use TeleSign’s REST API.  If you are already a customer and need an API Key, you can generate one in the `Client Portal <https://portal.telesign.com>`_.  If you are not a customer and would like to get an API Key, please contact `support@telesign.com <mailto:support@telesign.com>`_


Support and Feedback
--------------------

For more information about the Phone Verify and PhoneID Standard services, please contact your TeleSign representative:

Email: `support@telesign.com <mailto:support@telesign.com>`_

Phone: +1 310 740 9700
