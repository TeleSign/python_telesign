const TeleSignSDK = require('../../src/Telesign');
// NOTE: change this to the following if using npm package
// var TeleSignSDK = require('telesignenterprisesdk');


console.log("## phoneid.numberDeactivation ##");

const customerId = "customer_id"; // Todo: find in portal.telesign.com
const apiKey = "dGVzdCBhcGkga2V5IGZvciBzZGsgZXhhbXBsZXM="; // Todo: find in portal.telesign.com
const phoneNumber = "phone_number";
const optionalParams = {ucid: "ATCK"};

const client = new TeleSignSDK(customerId, apiKey);

function phoneidCallback(error, responseBody) {
    if (error === null) {

        if (responseBody.hasOwnProperty['number_deactivation']['last_deactivated']) {
            console.log(`PhoneID response for phone number: ${phoneNumber}` +
                ` => phone number: ${responseBody['number_deactivation']['number']}` +
                `, last deactivated: ${responseBody['number_deactivation']['last_deactivated']}`);
        } else {
            console.log(`Phone number ${responseBody['number_deactivation']['number']} has not been deactivated.`);
        }

    } else {
        console.error("Unable to send phoneID numberDeactivation. " + error);
    }
}

client.phoneid.numberDeactivation(phoneidCallback, phoneNumber, optionalParams);

