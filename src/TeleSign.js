const Verify = require('./Verify.js');
const PhoneID = require('./PhoneID.js');
const TeleBureau = require('./TeleBureau.js');

module.exports = class TeleSign {
    constructor(customerId,
                apiKey,
                restEndpoint = "https://rest-ww.telesign.com",
                timeout = 10000,
                useragent = null) {

        this.verify = new Verify(customerId, apiKey, restEndpoint, timeout, useragent);
        this.phoneid = new PhoneID(customerId, apiKey, restEndpoint, timeout, useragent);
        this.telebureau = new TeleBureau(customerId, apiKey, restEndpoint, timeout, useragent);
    }
};