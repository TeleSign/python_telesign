const readline = require('readline');
const TelesignSDK = require('../../src/telesign');
// NOTE: change this to the following if using npm package
// var TelesignSDK = require('telesignenterprisesdk');


console.log("## verify.voice ##");

const customerId = "customer_id";
const apiKey = "dGVzdCBhcGkga2V5IGZvciBzZGsgZXhhbXBsZXM=";
const phoneNumber = "phone_number";
const optionalParams = {verify_code: "32658"};
var referenceID = "";

const client = new TelesignSDK(customerId, apiKey);

// Callback for voice request
function voiceCallback(error, responseBody) {
    if (error === null) {
        console.log(`Voice response for phone number: ${phoneNumber}` +
            ` => code: ${responseBody['status']['code']}` +
            `, description: ${responseBody['status']['description']}`);

        if (responseBody['status']['code'] < 300) {
            console.log(`ReferenceID for voice call request: ${responseBody['reference_id']}.`)
            referenceID = responseBody['reference_id'];

            // Ask user for input and send completion report
            if (referenceID !== "") {
                prompt('Enter the verification code received:\n', function (input) {
                    if (input === optionalParams['verify_code']) {
                        console.log('Your code is correct.');

                        // Send completion report for correct code entered
                        client.verify.completion()
                    } else {
                        console.log('Your code is incorrect. input: ' + input + ", code: " + optionalParams['verify_code']);
                    }
                    process.exit();
                });
            }

        } else {
            console.log(`Failed to send voice call.`)
            console.log(responseBody);
            process.exit();
        }

    } else {
        console.error("Unable to send Voice. " + error);
    }
}

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

// Callback for completion report
function completionCallback(error, responseBody) {
    if (error === null) {
        if (responseBody['status']['code'] == 1900) {
            console.log(`Successful completion response for phone number: ${phoneNumber}` +
                ` => code: ${responseBody['status']['code']}` +
                `, description: ${responseBody['status']['description']}`);
        } else {
            console.log(`Error during reporting completion.`);
        }

    } else {
        console.error("Unable to send completion report. " + error);
    }
}

// Send Voice request 
client.verify.voice(voiceCallback, phoneNumber, optionalParams);
