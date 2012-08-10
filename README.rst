========
TeleSign
========

:Info:
    For more information, visit the `TeleSign web site <http://www.TeleSign.com>`_.
    For the latest source code, visit the `TeleSign github repository <http://github.com/TeleSign/python_telesign/tree>`_.

:Author:
    Telesign Corp.

---------------------------------
TeleSign Web Services: Python SDK
---------------------------------

**TeleSign Web Services** conform to the `REST Web Service Design Model <http://en.wikipedia.org/wiki/Representational_state_transfer>`_. Services are exposed as URI-addressable resources through the set of *RESTful* procedures in our **TeleSign REST API**.

The **TeleSign Python SDK** is a set of software development tools—a *Python Library* that wraps the TeleSign REST API, and it simplifies TeleSign application development in the `Python programming language <http://pypi.python.org/pypi/>`_. The SDK software is listed in the `Python Package Index (PyPI) <http://pypi.python.org>`_ , as the **telesign** Python package.

The Python Classes
------------------

With just two classes, **telesign.api** abstracts much of the complexity of the TeleSign REST API.

+----------------------+--------------------------------------------------------------------------+ 
| Python Class         | Description                                                              | 
+======================+==========================================================================+ 
| telesign.api.PhoneId | The **PhoneId** class exposes three services that each provide           | 
|                      | information about a specified phone number.                              | 
|                      |                                                                          | 
|                      | *standard*                                                               | 
|                      |     Retrieves the standard set of details about the specified phone      | 
|                      |     number. This includes the type of phone (e.g., land line or mobile), | 
|                      |     and it's approximate geographic location.                            | 
|                      | *score*                                                                  | 
|                      |     Retrieves a score for the specified phone number. This ranks the     | 
|                      |     phone number's "risk level" on a scale from 0 to 1000, so you can    | 
|                      |     code your web application to handle particular use cases (e.g., to   | 
|                      |     stop things like chargebacks, identity theft, fraud, and spam).      | 
|                      | *contact*                                                                | 
|                      |     In addition to the information retrieved by *standard*, this service | 
|                      |     provides the Name & Address associated with the specified phone      | 
|                      |     number.                                                              | 
|                      |                                                                          | 
+----------------------+--------------------------------------------------------------------------+ 
| telesign.api.Verify  | The **Verify** class exposes two services for sending users a            | 
|                      | verification token (a three to five-digit number). You can use this      | 
|                      | mechanism to simply test whether you can reach users at the phone number | 
|                      | they supplied, or you can have them use the token to authenticate        | 
|                      | themselves with your web application. In addition, this class also       | 
|                      | exposes a service that allows you to confirm the result of the           | 
|                      | authentication.                                                          | 
|                      |                                                                          | 
|                      | You can use this verification factor in combination with *username*      | 
|                      | & *password* to provide *two-factor* authentication for higher           | 
|                      | security.                                                                | 
|                      |                                                                          | 
|                      | *call*                                                                   | 
|                      |     Calls the specified phone number, and using speech synthesis—speaks  | 
|                      |     the verification code to the user.                                   | 
|                      | *sms*                                                                    | 
|                      |     Send a text message containing the verification code to the          | 
|                      |     specified phone number (supported for mobile phones only).           | 
|                      | *status*                                                                 | 
|                      |     Retrieves the verification result. You make this call in your web    | 
|                      |     application after users complete the authentication transaction      | 
|                      |     (using either a *call* or *sms*).                                    | 
|                      |                                                                          | 
+----------------------+--------------------------------------------------------------------------+ 

Installation
------------

With `Easy
Install <http://packages.python.org/distribute/easy_install.html>`_
installed, simply type **easy\_install telesign** at the command prompt.
Alternatively, you can download the project source, and execute **python
setup.py install**.

Python Code Example: To Verify a Call
-------------------------------------

Here's a basic code example.

::

    >>> from telesign.api import Verify
    >>> phone_number = "13103409700"
    >>> cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
    >>> secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
    >>> verify = Verify(cust_id, secret_key)      # Instantiate a Verify instance object,
    >>> result = verify.call(phone_number, verify_code=1234)  # and use it to call the "call" method.
    >>> print result.data
    
    {u'status': {u'updated_on': u'2012-04-23T21:28:06.837153', u'code': 103, u'description': u'Call in progress'}, u'errors': [], u'verify': {u'code_state': u'UNKNOWN', u'code_entered': u''}, u'sub_resource': u'call', u'reference_id': u'DGFDF6E11AB86303ASDFD425BE00000657', u'resource_uri': u'/v1/verify/DGFDF6E11AB86303ASDFD425BE00000657'}

For more examples, see the Documentation section below.

Authentication
--------------

You will need a Customer ID and API Key in order to use TeleSign’s REST API.  If you are already a customer and need an API Key, you can generate one in the `Client Portal <https://portal.telesign.com>`_.  If you are not a customer and would like to get an API Key, please contact `support@telesign.com <mailto:support@telesign.com>`_

Documentation
-------------

You will need sphinx_ installed to generate the
documentation. Documentation can be generated by running **python
setup.py doc**. Generated documentation can be found in the
*doc/build/* directory.

Detailed documentation for TeleSign™ REST APIs is available in the
`Client Portal <https://portal.telesign.com>`_

Testing
-------

The easiest way to run the tests is to install `nose
<http://somethingaboutorange.com/mrl/projects/nose/>`_ (**easy_install
nose**) and run **nosetests** or **python setup.py test** in the root
of the distribution. Tests are located in the *test/* directory.


Support and Feedback
--------------------

For more information about the Phone Verify and PhoneID Standard services, please contact your TeleSign representative:

Email: `support@telesign.com <mailto:support@telesign.com>`_

.. _sphinx: http://sphinx.pocoo.org/
