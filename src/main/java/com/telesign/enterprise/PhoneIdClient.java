package com.telesign.enterprise;

import com.telesign.RestClient;

import java.io.IOException;
import java.net.Proxy;
import java.security.GeneralSecurityException;
import java.util.HashMap;
import java.util.Map;

/**
 * TeleSign's Voice API allows you to easily send verify_voice messages. You can send alerts, reminders, and notifications,
 * or you can send verification messages containing time-based, one-time passcodes (TOTP).
 */
public class PhoneIdClient extends RestClient {

    private static final String PHONEID_STANDARD_RESOURCE = "/v1/phoneid_number_deactivation/standard/%s";
    private static final String PHONEID_SCORE_RESOURCE = "/v1/phoneid_number_deactivation/phoneid_score/%s";
    private static final String PHONEID_CONTACT_RESOURCE = "/v1/phoneid_number_deactivation/contact/%s";
    private static final String PHONEID_LIVE_RESOURCE = "/v1/phoneid_number_deactivation/live/%s";
    private static final String PHONEID_NUMBER_DEACTIVATION_RESOURCE = "/v1/phoneid_number_deactivation/number_deactivation/%s";

    public PhoneIdClient(String customerId, String secretKey) {

        super(customerId, secretKey, "https://rest-ww.telesign.com");
    }

    public PhoneIdClient(String customerId, String secretKey, String apiHost) {
        super(customerId, secretKey, apiHost);
    }

    public PhoneIdClient(String customerId,
                         String secretKey,
                         String apiHost,
                         Long connectTimeout,
                         Long readTimeout,
                         Long writeTimeout,
                         Proxy proxy,
                         final String proxyUsername,
                         final String proxyPassword) {
        super(customerId, secretKey, apiHost, connectTimeout, readTimeout, writeTimeout, proxy, proxyUsername, proxyPassword);
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

        return super.get(String.format(PHONEID_STANDARD_RESOURCE, phoneNumber), params);
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

        return super.get(String.format(PHONEID_SCORE_RESOURCE, phoneNumber), params);
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

        return super.get(String.format(PHONEID_CONTACT_RESOURCE, phoneNumber), params);
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

        return super.get(String.format(PHONEID_LIVE_RESOURCE, phoneNumber), params);
    }

    /**
     * The PhoneID Number Deactivation API determines whether a phone number has been deactivated and when, based on
     * carriers' phone number data and TeleSign's proprietary analysis.
     * <p>
     * See https://developer.telesign.com/docs/rest_api-phoneid-number-deactivation for detailed API documentation.
     */
    public TelesignResponse number_deactivation(String phoneNumber, String ucid, Map<String, String> params) throws IOException, GeneralSecurityException {

        if (params == null) {
            params = new HashMap<>();
        }

        params.put("ucid", ucid);

        return super.get(String.format(PHONEID_NUMBER_DEACTIVATION_RESOURCE, phoneNumber), params);
    }
}
