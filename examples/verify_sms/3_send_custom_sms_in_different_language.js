const TeleSignSDK = require('../../src/Telesign');
// NOTE: change this to the following if using npm package
// var TeleSignSDK = require('telesignenterprisesdk');


console.log("## verify.sms ##");

const customerId = "customer_id"; // Todo: find in portal.telesign.com
const apiKey = "dGVzdCBhcGkga2V5IGZvciBzZGsgZXhhbXBsZXM="; // Todo: find in portal.telesign.com
const phoneNumber = "phone_number";
const optionalParams = {template: "Votre code de vérification Widgets 'n' More est $$CODE$$."};

const client = new TeleSignSDK(customerId, apiKey);

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
