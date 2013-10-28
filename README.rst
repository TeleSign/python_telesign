========
TeleSign
========

:Info:
    For more information, visit the `TeleSign web site <http://www.TeleSign.com>`_.
    For the latest source code, visit the `TeleSign github repository <http://github.com/TeleSign/csharp_telesign/tree>`_.

:Author:
    Telesign Corp.

---------------------------------
TeleSign Web Services: .NET SDK
---------------------------------

**TeleSign Web Services** conform to the `REST Web Service Design Model <http://en.wikipedia.org/wiki/Representational_state_transfer>`_. Services are exposed as URI-addressable resources through the set of *RESTful* procedures in our **TeleSign REST API**.

The **TeleSign .NET SDK** is a Microsoft .NET component that provides an interface to `TeleSign Web Services <http://www.telesign.com/products-demos/>`_. 

It contains a .NET Framework class library that presents our web services in an intuitive, hierarchical object model, so you can create and manipulate them in the way you're accustomed to. You can use this SDK to build TeleSign‑based .NET applications.

Authentication
--------------

**You will need a Customer ID and API Key in order to use TeleSign’s REST API**.  If you are already a customer and need an API Key, you can generate one in the `Client Portal <https://teleportal.telesign.com>`_.  If you are not a customer and would like to get an API Key, please contact `support@telesign.com <mailto:support@telesign.com>`_

You supply your credentials to the API either by editing the TeleSign.config.xml file and filling in the CustomerId and
SecretKey values or you can create the credentials in code. Passing null to the service constructors uses the file.

**Option 1. Supply TeleSign.config.xml**

>>>
  <?xml version="1.0" encoding="utf-8" ?>
  <TeleSignConfig>
  <ServiceUri>https://rest.telesign.com</ServiceUri>
  <Accounts>
    <Account name="default">
      <!-- Enter your customer id and secret key here. -->
      <CustomerId>99999999-9999-9999-9999-000000000000</CustomerId>
      <SecretKey>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==</SecretKey>
    </Account>
  </Accounts>
 </TeleSignConfig>


**Option 2. Supply the credential with code**

>>>
  Guid customerId = Guid.Parse("*** Customer ID goes here ***");
  string secretKey = "*** Secret Key goes here ***";
  TeleSignCredential credential = new TeleSignCredential(
              customerId,
              secretKey);
  TeleSignServiceConfiguration config = new TeleSignServiceConfiguration(credential);
  // For Verify Sms or Call Service
  VerifyService verify = new VerifyService(config);
  // For PhoneId products
  PhoneIdServer phoneId = PhoneIdService(config);

Operating Modes
---------------

You can use the TeleSign .NET SDK in either of two modes. The rich mode is recommended and handles all aspects of authentication and response parsing, providing a high level object model.

+----------------------+--------------------------------------------------------------------------+ 
| Mode                 | Description                                                              | 
+======================+==========================================================================+ 
| Rich                 | Provides an object-oriented framework that models web services as        |
|                      | high-level actors, and low-level processes as mediator objects.          |
|                      | Automatically parses the JSON data from server responses, and creates    |
|                      | Response objects from it.                                                | 
|                      |                                                                          | 
+----------------------+--------------------------------------------------------------------------+ 
| Raw                  | Abstracts the interaction with only the web services. Method calls       |
|                      | return the web service's JSON response bodies verbatim. This gives you   |
|                      | the flexibility of handling the response processing any way you want.    | 
|                      |                                                                          | 
+----------------------+--------------------------------------------------------------------------+ 

Documentation
-------------

All classes and functions are documented with XML comments. Installing `Sandcastle Help File Builder 
<http://shfb.codeplex.com/>`_ will allow you to build the HTML version of the documentation locally.

Rich Mode Classes
-----------------

+----------------------+--------------------------------------------------------------------------+ 
| Mode                 | Description                                                              | 
+======================+==========================================================================+ 
| PhoneIdService.cs    | The **PhoneIdService** class exposes four services that each provide     | 
|                      | information about a specified phone number.                              | 
|                      |                                                                          | 
|                      | ``public PhoneIdStandardResponse StandardLookup(string phoneNumber)``    | 
|                      |     Retrieves the standard set of details about the specified phone      | 
|                      |     number. This includes the type of phone (e.g., land line or mobile), | 
|                      |     and it's approximate geographic location.                            | 
|                      | ``public PhoneIdScoreResponse ScoreLookup(string phoneNumber)``          | 
|                      |     Retrieves a score for the specified phone number. This ranks the     | 
|                      |     phone number's "risk level" on a scale from 0 to 1000, so you can    | 
|                      |     code your web application to handle particular use cases (e.g., to   | 
|                      |     stop things like chargebacks, identity theft, fraud, and spam).      | 
|                      | ``public PhoneIdContactResponse ContactLookup(string phoneNumber)``      | 
|                      |     In addition to the information retrieved by *standard*, this service | 
|                      |     provides the Name & Address associated with the specified phone      | 
|                      |     number.                                                              |
|                      |                                                                          | 
|                      | ``public PhoneIdLiveResponse LiveLookup(string phoneNumber)``            | 
|                      |     In addition to the information retrieved by *standard*, this service | 
|                      |     provides information about the subscriber status, device status,     | 
|                      |     roaming status and roaming country.                                  | 
|                      |                                                                          | 
|                      |                                                                          | 
+----------------------+--------------------------------------------------------------------------+ 
| VerifyService.cs     | The **VerifyService** class exposes two services for sending users a     | 
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
|                      | ``public VerifyResponse SendSms(string phoneNumber)``                    | 
|                      |     Send a text message containing the verification code to the          | 
|                      |     specified phone number (supported for mobile phones only).           | 
|                      |                                                                          | 
|                      | ``public VerifyResponse InitiateCall(string phoneNumber)``               | 
|                      |     Calls the specified phone number, and using a recorded message speaks| 
|                      |     the verification code to the user.                                   | 
|                      |                                                                          | 
|                      | ``public VerifyResponse ValidateCode(``                                  |
|                      |               ``string referenceId,``                                    |
|                      |               ``string verifyCode)``                                     |
|                      |                                                                          | 
|                      |     Checks the code supplied is correct. You make this call in your      |
|                      |     application after users complete the authentication transaction.     |
|                      |                                                                          | 
|                      | ``public VerifyResponse CheckStatus(string referenceId)``                |
|                      |                                                                          | 
|                      |                                                                          | 
+----------------------+--------------------------------------------------------------------------+ 

Code Example: PhoneId Contact Lookup
------------------------------------
These example assume you are using the file for authentication/configuration described above.

>>>
string phoneNumber = "+1 555-555-5555";
PhoneIdService service = new PhoneIdService();
PhoneIdContactResponse response = service.ContactLookup(phoneNumber);
Console.WriteLine("Phone Number: {0}", phoneNumber);
Console.WriteLine("Name        : {0}", response.Contact.FullName);
Console.WriteLine("Address     :\r\n{0}", response.Contact.GetFullAddress());

Code Example: Initiate Sms Verify
---------------------------------
>>>
string code = "1234";
string phoneNumber = "+1 555-555-5555";
string language = "en";
VerifyService verify = new VerifyService();
VerifyResponse verifyResponse = verify.SendSms(phoneNumber, code, string.Empty, language);


For more examples, see the documentation or browse the example command line app source code in 
**Commands.cs** in the **TeleSign.TeleSignCmd** project.


Support and Feedback
--------------------

For more information about the Phone Verify and PhoneID Standard services, please contact your TeleSign representative:

Email: `support@telesign.com <mailto:support@telesign.com>`_

