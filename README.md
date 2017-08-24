[<img src="/node_enterprise.jpg">](https://developer.telesign.com)

TeleSign Node.js SDK
=================

TeleSign is a communications platform as a service (CPaaS) company, founded on security. Since 2005, TeleSign has
been a trusted partner to the world’s leading websites and mobile applications, helping secure billions of end-user
accounts. Today, TeleSign’s data-driven, cloud communications platform is changing the way businesses engage with
customers and prevent fraud.

For more information about TeleSign, visit our [website](http://www.TeleSign.com>).


Documentation
-------------

Code documentation is included in the SDK. Complete documentation, quick start guides and reference material
for the TeleSign API is available within the [TeleSign Developer Center](https://developer.telesign.com/).


Installation
------------

Once you have cloned this SDK, you can install it using the following command
```
npm install /path/to/sdk -save
```

Authentication
--------------

You will need a Customer ID and API Key in order to use TeleSign’s API. If you already have an account you can retrieve
them from [TelePortal](https://teleportal.telesign.com).


Dependencies
------------

We make use of popular, feature-rich and well-tested open-source libraries to perform the underlying functionality of
the SDK. These dependencies are managed by the community accepted package manager. If you are unable to add these
additional third party dependencies to your project we have ensured that the SDK code is easy to read and can serve as
sample code. We have also made sure that more complicated functions such as generate_telesign_headers can be easily
extracted from the SDK and used 'as is' in your project.


Examples
========

**How to Run**

1. Edit file and replace values for API Key, Customer ID, and mobile_number
2. Run the file via : node [example_filename].js

Example: You can run the 1_send_sms_with_verification_code.js with the following command

```
node examples/verify_sms/1_send_sms_with_verification_code.js
```

Sample code: Verify SMS
----------------------------------------

After installing the SDK, begin by including the telesign SDK and declaring customerId, apiKey, restEndpoint, and
timeout variables.

Setup Telesign Client

```javascript
    const TelesignSDK = require('telesignenterprisesdk');
    
    const customerId = "customer_id"; // Todo: find in portal.telesign.com
    const apiKey = "dGVzdCBhcGkga2V5IGZvciBzZGsgZXhhbXBsZXM="; // Todo: find in portal.telesign.com
    const client = new TelesignSDK(customerId, apiKey);
    
```

Send an SMS 
```javascript
    const phoneNumber = "phone_number";
    const optionalParams = {template: "Votre code de vérification Widgets 'n' More est $$CODE$$."};    
        
    // Callback handler for SMS
    function smsCallback(error, responseBody) {
        if (error === null) {
            console.log(`SMS response for phone number: ${phoneNumber}` +
                ` => code: ${responseBody['status']['code']}` +
                `, description: ${responseBody['status']['description']}`);
        } else {
            console.error("Unable to send sms. " + error);
        }
    }
    
    // Send SMS request
    client.verify.sms(smsCallback, phoneNumber, optionalParams);

```


Further reading
---------------

* The definitions of the parameters are best documented in the REST API documentation 
located [here](https://developer.telesign.com/docs/api-docs).
* Code examples can be found [here](/examples).
