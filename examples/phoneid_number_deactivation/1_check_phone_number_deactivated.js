const TelesignSDK = require('../../src/telesign');
// NOTE: change this to the following if using npm package
// var TelesignSDK = require('telesignenterprisesdk');


console.log("## phoneid.numberDeactivation ##");

const customerId = "customer_id"; // Todo: find in portal.telesign.com
const apiKey = "dGVzdCBhcGkga2V5IGZvciBzZGsgZXhhbXBsZXM="; // Todo: find in portal.telesign.com
const phoneNumber = "phone_number";
const ucid = "ATCK";

const client = new TelesignSDK(customerId, apiKey);

function phoneidCallback(error, responseBody) {
    if (error === null) {

        if (responseBody.hasOwnProperty('number_deactivation')) {
            console.log(`PhoneID response for phone number: ${phoneNumber}` +
                ` => phone number: ${responseBody['number_deactivation']['number']}` +
                `, last deactivated: ${responseBody['number_deactivation']['last_deactivated']}`);
        } else {
            console.log(`Phone number ${phoneNumber} has not been deactivated.`);
            console.log(responseBody);
        }

    } else {
        console.error("Unable to send phoneID numberDeactivation. " + error);
    }
}

client.phoneid.numberDeactivation(phoneidCallback, phoneNumber, ucid);

