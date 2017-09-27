const TelesignSDK = require('../../src/telesign');
// NOTE: change this to the following if using npm package
// var TelesignSDK = require('telesignenterprisesdk');


console.log("## verify.voice ##");

const customerId = "78747D92-1F7E-11E1-A71A-111111111111";
const apiKey = "4gS8tDHBSFB22V7suwhMPhb5QQL/9xTQcLOry9GQtodziGZF4WiP5xzEB5IMgjTuYIghWlTskkmb8sj0y+aOgg==";
const phoneNumber = "13235564074";
const verifyCode = "27364"
const optionalParams = {tts_message: `Hello, your code is ${verifyCode}. Once again, your code is ${verifyCode}. Goodbye.`};

const client = new TelesignSDK(customerId, apiKey);

// Callback handler for verify voice
function voiceCallback(error, responseBody) {
    if (error === null) {
        console.log(`Voice call response for phone number: ${phoneNumber}` +
            ` => code: ${responseBody['status']['code']}` +
            `, description: ${responseBody['status']['description']}`);

        // Ask for user input
        prompt('Enter the verification code received:\n', function (input) {
            if (input === verifyCode) {
                console.log('Your code is correct.');
            } else {
                console.log('Your code is incorrect. input: ' + input + ", code: " + verifyCode);
            }
            process.exit();
        });

    } else {
        console.error("Unable to send voice. " + error);
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

// Send voice request
client.verify.voice(voiceCallback, phoneNumber, optionalParams);
