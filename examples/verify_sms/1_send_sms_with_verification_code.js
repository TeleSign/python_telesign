const readline = require('readline');
const TelesignSDK = require('../../src/telesign');
// NOTE: change this to the following if using npm package
// var TelesignSDK = require('telesignenterprisesdk');


console.log("## verify.sms ##");

const customerId = "customer_id";
const apiKey = "dGVzdCBhcGkga2V5IGZvciBzZGsgZXhhbXBsZXM=";
const phoneNumber = "phone_number";
const optionalParams = {verify_code: "32658"};

const client = new TelesignSDK(customerId, apiKey);

// Callback for SMS request
function smsCallback(error, responseBody) {
    if (error === null) {
        console.log(`Messaging response for messaging phone number: ${phoneNumber}` +
            ` => code: ${responseBody['status']['code']}` +
            `, description: ${responseBody['status']['description']}`);

        // Ask for user input
        prompt('Enter the verification code received:\n', function (input) {
            if (input === optionalParams['verify_code']) {
                console.log('Your code is correct.');
            } else {
                console.log('Your code is incorrect. input: ' + input + ", code: " + optionalParams['verify_code']);
            }
            process.exit();
        });

    } else {
        console.error("Unable to send SMS. " + error);
    }
}

// Method to handler user input
function prompt(question, callback) {
    const stdin = process.stdin,
        stdout = process.stdout;

    stdin.resume();
    stdout.write(question);

    stdin.once('data', function (data) {
        callback(data.toString().trim());
    });
}

// Send SMS request
client.verify.sms(smsCallback, phoneNumber, optionalParams);
