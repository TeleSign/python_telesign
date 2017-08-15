// note change this to the following if using npm package: require('telesignsdk);
const TeleSignSDK = require('../../src/TeleSign');
//var TeleSignSDK = require('telesignsdk');

const customerId = "customer_id"; // Todo: find in portal.telesign.com
const apiKey = "dGVzdCBhcGkga2V5IGZvciBzZGsgZXhhbXBsZXM="; // Todo: find in portal.telesign.com
const rest_endpoint = "https://rest-api.telesign.com"; // Todo: Enterprise customer, change this!
const timeout = 10*1000; // 10 secs

const client = new TeleSignSDK( customerId,
    apiKey,
    rest_endpoint,
    timeout // optional
    // userAgent
);

const phoneNumber = "phone_number";
const phoneTypeVOIP = "5";

console.log("## PhoneIDClient.phoneID ##");

function messageCallback(error, responseBody) {
    if (error === null) {
        console.log(`PhoneID response for phone number: ${phoneNumber}`
            + ` => code: ${responseBody['status']['code']}`
            + `, description: ${responseBody['status']['description']}`);

        if (responseBody['status']['code'] === 200) {
            if (responseBody['phone_type']['code'] === phoneTypeVOIP) {
                console.log("Phone type in request is VOIP");
            } else {
                console.log("Phone type in request is not VOIP");
            }
        }
    } else {
        console.error("Unable to get PhoneID. " + error);
    }
}

client.phoneid.phoneID(messageCallback, phoneNumber);
