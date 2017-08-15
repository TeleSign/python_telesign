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
const accountLifeCycleEvent = "create";

console.log("## ScoreClient.score ##");

function score_callback(error, response_body) {
    if (error === null) {
        console.log(`Score response for phone number: ${phoneNumber}` +
            ` => code: ${response_body['status']['code']}` +
            `, description: ${response_body['status']['description']}`);
    } else {
        console.error("Unable to get score. " + error);
    }
}

client.score.score(score_callback, phoneNumber, accountLifeCycleEvent);
