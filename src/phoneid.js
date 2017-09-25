const Telesign = require('telesignsdk');
const util = require('util')

/***
 * PhoneID is a set of REST APIs that deliver deep phone number data attributes that help optimize the end user
 * verification process and evaluate risk.
 *
 * TeleSign PhoneID provides a wide range of risk assessment indicators on the number to help confirm user identity,
 * delivering real-time decision making throughout the number lifecycle and ensuring only legitimate users are
 * creating accounts and accessing your applications.
 */
class PhoneID {

    constructor(customerId,
                apiKey,
                restEndpoint="https://rest-ww.telesign.com",
                timeout=10000,
                userAgent=null) {

        this.rest = new Telesign(customerId, apiKey, restEndpoint, timeout, userAgent).rest;

        this.standardResource = "/v1/phoneid/standard/%s"
        this.scoreResource = "/v1/phoneid/score/%s"
        this.contactResource = "/v1/phoneid/contact/%s"
        this.liveResource = "/v1/phoneid/live/%s"
        this.numberDeactivationResource = "/v1/phoneid/number_deactivation/%s"
    }

    /***
     * The PhoneID Standard API that provides phone type and telecom carrier information to identify which phone
     * numbers can receive SMS messages and/or a potential fraud risk.
     *
     * See https://developer.telesign.com/docs/rest_phoneid-standard for detailed API documentation.
     *
     * @param callback: Callback method to handle response.
     * @param phoneNumber: Phone number associated with the event.
     * @param optionalParams: Dictionary of all optional parameters.
     * transaction.
     */
    standard(callback, phoneNumber, optionalParams=null) {
        var params = {
            phone_number: phoneNumber
        };
        if (optionalParams != null) {
            params = Object.assign(params, optionalParams)
        }

        this.rest.execute(callback, "GET", util.format(this.standardResource, phoneNumber), params);
    }

    /***
     * Score is an API that delivers reputation scoring based on phone number intelligence, traffic patterns, machine
     * learning, and a global data consortium.
     *
     * See https://developer.telesign.com/docs/rest_api-phoneid-score for detailed API documentation.
     *
     * @param callback: Callback method to handle response.
     * @param phoneNumber: Phone number associated with the event.
     * @param ucid: A string that specifies one of the use case codes.
     * @param optionalParams: Dictionary of all optional parameters.
     * transaction.
     */
    score(callback, phoneNumber, ucid, optionalParams=null) {
        var params = {
            phone_number: phoneNumber,
            ucid: ucid
        };
        if (optionalParams != null) {
            params = Object.assign(params, optionalParams)
        }

        this.rest.execute(callback, "GET", util.format(this.scoreResource, phoneNumber), params);
    }

    /***
     * The PhoneID Contact API delivers contact information related to the subscriber's phone number to provide another
     * set of indicators for established risk engines.
     *
     * See https://developer.telesign.com/docs/rest_api-phoneid-contact for detailed API documentation.
     *
     * @param callback: Callback method to handle response.
     * @param phoneNumber: Phone number associated with the event.
     * @param ucid: A string that specifies one of the use case codes.
     * @param optionalParams: Dictionary of all optional parameters.
     * transaction.
     */
    contact(callback, phoneNumber, ucid, optionalParams=null) {
        var params = {
            phone_number: phoneNumber,
            ucid: ucid
        };
        if (optionalParams != null) {
            params = Object.assign(params, optionalParams)
        }

        this.rest.execute(callback, "GET", util.format(this.contactResource, phoneNumber), params);
    }

    /***
     * The PhoneID Live API delivers insights such as whether a phone is active or disconnected, a device is reachable
     * or unreachable and its roaming status.
     *
     * See https://developer.telesign.com/docs/rest_api-phoneid-live for detailed API documentation.
     *
     * @param callback: Callback method to handle response.
     * @param phoneNumber: Phone number associated with the event.
     * @param ucid: A string that specifies one of the use case codes.
     * @param optionalParams: Dictionary of all optional parameters.
     * transaction.
     */
    live(callback, phoneNumber, ucid, optionalParams=null) {
        var params = {
            phone_number: phoneNumber,
            ucid: ucid
        };
        if (optionalParams != null) {
            params = Object.assign(params, optionalParams)
        }

        this.rest.execute(callback, "GET", util.format(this.liveResource, phoneNumber), params);
    }

    /***
     * The PhoneID Number Deactivation API determines whether a phone number has been deactivated and when, based on
     * carriers' phone number data and TeleSign's proprietary analysis.
     *
     * See https://developer.telesign.com/docs/rest_api-phoneid-number-deactivation for detailed API documentation.
     *
     * @param callback: Callback method to handle response.
     * @param phoneNumber: Phone number associated with the event.
     * @param ucid: A string that specifies one of the use case codes.
     * @param optionalParams: Dictionary of all optional parameters.
     * transaction.
     */
    numberDeactivation(callback, phoneNumber, ucid, optionalParams=null) {
        var params = {
            phone_number: phoneNumber,
            ucid: ucid
        };
        if (optionalParams != null) {
            params = Object.assign(params, optionalParams)
        }

        this.rest.execute(callback, "GET", util.format(this.numberDeactivationResource, phoneNumber), params);
    }

}

module.exports = PhoneID;