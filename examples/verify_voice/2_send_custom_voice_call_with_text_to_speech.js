const TeleSignSDK = require('../../src/Telesign');
// NOTE: change this to the following if using npm package
// var TeleSignSDK = require('telesignenterprisesdk');


console.log("## verify.voice ##");

const customerId = "customer_id"; // Todo: find in portal.telesign.com
const apiKey = "dGVzdCBhcGkga2V5IGZvciBzZGsgZXhhbXBsZXM="; // Todo: find in portal.telesign.com
const phoneNumber = "phone_number";
const verifyCode = "1, 2, 3, 4, 5"
const optionalParams = {tts_message: "Hello, your code is ${verifyCode}. Once again, your code is ${verifyCode}. Goodbye."};

const client = new TeleSignSDK(customerId, apiKey);

// Callback handler for verify voice
function voiceCallback(error, responseBody) {
    if (error === null) {
        console.log(`Voice call response for phone number: ${phoneNumber}` +
            ` => code: ${responseBody['status']['code']}` +
            `, description: ${responseBody['status']['description']}`);
    } else {
        console.error("Unable to send voice. " + error);
    }
}

// Send voice request
client.verify.voice(voiceCallback, phoneNumber, optionalParams);

// Method to handle user input
function prompt(question, callback) {
    const stdin = process.stdin,
        stdout = process.stdout;

    stdin.resume();
    stdout.write(question);

    stdin.once('data', function (data) {
        callback(data.toString().trim());
    });
}

// Ask user for input
prompt('Enter the verification code received:\n', function (input) {
    if (input === optionalParams['verify_code']) {
        console.log('Your code is correct.');
    } else {
        console.log('Your code is incorrect. input: ' + input + ", code: " + optionalParams['verify_code']);
    }
    process.exit();
