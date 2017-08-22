const Telesign = require('telesignsdk');

/***
 * The Verify API delivers phone-based verification and two-factor authentication using a time-based, one-time passcode
 * sent via SMS message, Voice call or Push Notification.
 */
class Telebureau {

    constructor(customerId,
                apiKey,
                restEndpoint="https://rest-ww.telesign.com",
                timeout=10000,
                userAgent=null) {

        this.rest = new Telesign(customerId, apiKey, restEndpoint, timeout, userAgent).rest;

        this.createResource = "/v1/telebureau/event"
        this.retrieveResource = "/v1/telebureau/event/${referenceID}"
        this.deleteResource = "/v1/telebureau/event/${referenceID}"
    }

    /***
     * Creates a telebureau event corresponding to supplied data.
     *
     * See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
     *
     * @param callback: Callback method to handle response.
     * @param phoneNumber: Phone number associated with the event.
     * @param fraudType: The type of fraud committed.
     * @param occuredAt: Datetime specifying when the fraud event occurred in RFC 3339 format
     * @param optionalParams: Dictionary of all optional parameters.
     * transaction.
     */
    createEvent(callback, phoneNumber, fraudType, occuredAt, optionalParams=null) {
        var params = {
            phone_number: phoneNumber,
            fraud_type: fraudType,
            occured_at: occuredAt
        };
        if (optionalParams != null) {
            params = Object.assign(params, optionalParams)
        }

        this.rest.execute(callback, "POST", this.create_resource, params);
    }

    /***
     * Retrieves the fraud event status. You make this call in your web application after completion of create
     * transaction for a telebureau event.
     *
     * See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
     *
     * @param callback: Callback method to handle response.
     * @param referenceID: reference_id for the transaction from Telesign's response on create.
     * @param optionalParams: Dictionary of all optional parameters.
     * transaction.
     */
    retrieveEvent(callback, referenceID, optionalParams=null) {
        this.rest.execute(callback, "GET", this.retrieve_resource, optionalParams);
    }

    /***
     * Deletes a previously submitted fraud event. You make this call in your web application after completion of the
     * create transaction for a telebureau event.
     *
     * See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
     *
     * @param callback: Callback method to handle response.
     * @param referenceID: reference_id for the transaction from Telesign's response on create.
     * @param optionalParams: Dictionary of all optional parameters.
     * transaction.
     */
    deleteEvent(callback, referenceID, optionalParams=null) {
        this.rest.execute(callback, "DELETE", this.delete_resource, optionalParams);
    }
}

module.exports = Telebureau;