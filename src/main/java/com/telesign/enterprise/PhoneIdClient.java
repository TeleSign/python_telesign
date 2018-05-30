package com.telesign.enterprise;

import java.io.IOException;
import java.net.Proxy;
import java.security.GeneralSecurityException;
import java.util.HashMap;
import java.util.Map;

/**
 * PhoneID is a set of REST APIs that deliver deep phone number data attributes that help optimize the end user
 * verification process and evaluate risk.
 * <p>
 * TeleSign PhoneID provides a wide range of risk assessment indicators on the number to help confirm user identity,
 * delivering real-time decision making throughout the number lifecycle and ensuring only legitimate users are
 * creating accounts and accessing your applications.
 */
public class PhoneIdClient extends com.telesign.PhoneIdClient {

    private static final String PHONEID_STANDARD_RESOURCE = "/v1/phoneid/standard/%s";
    private static final String PHONEID_SCORE_RESOURCE = "/v1/phoneid/score/%s";
    private static final String PHONEID_CONTACT_RESOURCE = "/v1/phoneid/contact/%s";
    private static final String PHONEID_LIVE_RESOURCE = "/v1/phoneid/live/%s";
    private static final String PHONEID_NUMBER_DEACTIVATION_RESOURCE = "/v1/phoneid/number_deactivation/%s";

    public PhoneIdClient(String customerId, String apiKey) {

        super(customerId, apiKey, "https://rest-ww.telesign.com");
    }

    public PhoneIdClient(String customerId, String apiKey, String restEndpoint) {
        super(customerId, apiKey, restEndpoint);
    }

    public PhoneIdClient(String customerId,
                         String apiKey,
                         String restEndpoint,
                         Integer connectTimeout,
                         Integer readTimeout,
                         Integer writeTimeout,
                         Proxy proxy,
                         final String proxyUsername,
                         final String proxyPassword) {
        super(customerId, apiKey, restEndpoint, connectTimeout, readTimeout, writeTimeout, proxy, proxyUsername, proxyPassword);
    }

    /**
     * PhoneID is a set of REST APIs that deliver deep phone number data attributes that help optimize the end user
     * verification process and evaluate risk.
     * <p>
     * TeleSign PhoneID provides a wide range of risk assessment indicators on the number to help confirm user identity,
     * delivering real-time decision making throughout the number lifecycle and ensuring only legitimate users are
     * creating accounts and accessing your applications.
     */
    public TelesignResponse standard(String phoneNumber, Map<String, String> params) throws IOException, GeneralSecurityException {

        return this.get(String.format(PHONEID_STANDARD_RESOURCE, phoneNumber), params);
    }

    /**
     * Score is an API that delivers reputation scoring based on phone number intelligence, traffic patterns, machine
     * learning, and a global data consortium.
     * <p>
     * See https://developer.telesign.com/docs/rest_api-phoneid-score for detailed API documentation.
     */
    public TelesignResponse score(String phoneNumber, String ucid, Map<String, String> params) throws IOException, GeneralSecurityException {

        if (params == null) {
            params = new HashMap<>();
        }

        params.put("ucid", ucid);

        return this.get(String.format(PHONEID_SCORE_RESOURCE, phoneNumber), params);
    }

    /**
     * The PhoneID Contact API delivers contact information related to the subscriber's phone number to provide another
     * set of indicators for established risk engines.
     * <p>
     * See https://developer.telesign.com/docs/rest_api-phoneid-contact for detailed API documentation.
     */
    public TelesignResponse contact(String phoneNumber, String ucid, Map<String, String> params) throws IOException, GeneralSecurityException {

        if (params == null) {
            params = new HashMap<>();
        }

        params.put("ucid", ucid);

        return this.get(String.format(PHONEID_CONTACT_RESOURCE, phoneNumber), params);
    }

    /**
     * The PhoneID Live API delivers insights such as whether a phone is active or disconnected, a device is reachable
     * or unreachable and its roaming status.
     * <p>
     * See https://developer.telesign.com/docs/rest_api-phoneid-live for detailed API documentation.
     */
    public TelesignResponse live(String phoneNumber, String ucid, Map<String, String> params) throws IOException, GeneralSecurityException {

        if (params == null) {
            params = new HashMap<>();
        }

        params.put("ucid", ucid);

        return this.get(String.format(PHONEID_LIVE_RESOURCE, phoneNumber), params);
    }

    /**
     * The PhoneID Number Deactivation API determines whether a phone number has been deactivated and when, based on
     * carriers' phone number data and TeleSign's proprietary analysis.
     * <p>
     * See https://developer.telesign.com/docs/rest_api-phoneid-number-deactivation for detailed API documentation.
     */
    public TelesignResponse numberDeactivation(String phoneNumber, String ucid, Map<String, String> params) throws IOException, GeneralSecurityException {

        if (params == null) {
            params = new HashMap<>();
        }

        params.put("ucid", ucid);

        return this.get(String.format(PHONEID_NUMBER_DEACTIVATION_RESOURCE, phoneNumber), params);
    }
}
