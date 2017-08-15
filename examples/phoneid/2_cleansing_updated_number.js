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

console.log("## PhoneIDClient.phoneID ##");

function messageCallback(error, responseBody) {
    if (error === null) {
        console.log(`PhoneID response for phone number: ${phoneNumber} ` +
            `=> code: ${responseBody['status']['code']}, ` +
            `description: ${responseBody['status']['description']}`);

        if (responseBody['status']['code'] === 200) {
            const cc = responseBody['numbering']['cleansing']['call']['country_code'];
            const pn = responseBody['numbering']['cleansing']['call']['phone_number'];
            console.log("Cleansed phone number has country code $cc and phone number is $pn.")
        }
    } else {
        console.error("Unable to get PhoneID. $error");
    }
}

client.phoneid.phoneID(messageCallback, phoneNumber);
