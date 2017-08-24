const TeleSignSDK = require('../../src/Telesign');
// NOTE: change this to the following if using npm package
// var TeleSignSDK = require('telesignenterprisesdk');


console.log("## phoneid.score ##");

const customerId = "customer_id"; // Todo: find in portal.telesign.com
const apiKey = "dGVzdCBhcGkga2V5IGZvciBzZGsgZXhhbXBsZXM="; // Todo: find in portal.telesign.com
const phoneNumber = "phone_number";
const ucid = "BACF";

const client = new TeleSignSDK(customerId, apiKey);

function phoneidCallback(error, responseBody) {
    if (error === null) {
        if (responseBody.hasOwnProperty('risk')) {
            console.log(`PhoneID response for phone number: ${phoneNumber}` +
                ` => risk level: ${responseBody['risk']['level']}` +
                `, recommendation: ${responseBody['risk']['recommendation']}`);
        } else {
            console.log(`Phone number score could not be retrieved.`);
            console.log(responseBody);
        }

    } else {
        console.error("Unable to send phoneID. " + error);
    }
}

client.phoneid.score(phoneidCallback, phoneNumber, ucid);

