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
const message = "N'oubliez pas d'appeler votre mère pour son anniversaire demain.";
const messageType = "ARN";
const languageCode = "f-FR-fr";

console.log("## VoiceClient.call ##");

function voiceCallback(error, responseBody) {
    if (error === null) {
        console.log(`Messaging response for messaging phone number: ${phoneNumber}` +
            ` => code: ${responseBody['status']['code']}` +
            `, description: ${responseBody['status']['description']}`);
    } else {
        console.error("Unable to send message. " + error);
    }
}

client.voice.call(voiceCallback, phoneNumber, message, messageType, voice=languageCode);
