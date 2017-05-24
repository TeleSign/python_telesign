package com.telesign.enterprise;

import com.telesign.RestClient;

import java.io.IOException;
import java.net.Proxy;
import java.security.GeneralSecurityException;
import java.util.HashMap;
import java.util.Map;

/**
 * The Verify API delivers phone-based verification and two-factor authentication using a time-based, one-time passcode
 * sent via SMS message, Voice call or Push Notification.
 */
public class VerifyClient extends RestClient {

    private static final String VERIFY_SMS_RESOURCE = "/v1/verify/sms";
    private static final String VERIFY_VOICE_RESOURCE = "/v1/verify/call";
    private static final String VERIFY_SMART_RESOURCE = "/v1/verify/smart";
    private static final String VERIFY_PUSH_RESOURCE = "/v2/verify/push";
    private static final String VERIFY_STATUS_RESOURCE = "/v1/verify/%s";
    private static final String VERIFY_COMPLETION_RESOURCE = "/v1/verify/completion/%s";

    public VerifyClient(String customerId, String apiKey) {

        super(customerId, apiKey, "https://rest-ww.telesign.com");
    }

    public VerifyClient(String customerId, String apiKey, String restEndpoint) {
        super(customerId, apiKey, restEndpoint);
    }

    public VerifyClient(String customerId,
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
     * The SMS Verify API delivers phone-based verification and two-factor authentication using a time-based,
     * one-time passcode sent over SMS.
     * <p>
     * See https://developer.telesign.com/docs/rest_api-verify-sms for detailed API documentation.
     */
    public TelesignResponse sms(String phoneNumber, Map<String, String> params) throws IOException, GeneralSecurityException {

        if (params == null) {
            params = new HashMap<>();
        }

        params.put("phone_number", phoneNumber);

        return this.post(VERIFY_SMS_RESOURCE, params);
    }

    /**
     * The Voice Verify API delivers patented phone-based verification and two-factor authentication using a one-time
     * passcode sent over verify_voice message.
     * <p>
     * See https://developer.telesign.com/docs/rest_api-verify-call for detailed API documentation.
     */
    public TelesignResponse voice(String phoneNumber, Map<String, String> params) throws IOException, GeneralSecurityException {

        if (params == null) {
            params = new HashMap<>();
        }

        params.put("phone_number", phoneNumber);

        return this.post(VERIFY_VOICE_RESOURCE, params);
    }

    /**
     * The Smart Verify web service simplifies the process of verifying user identity by integrating several TeleSign
     * web services into a single API call. This eliminates the need for you to make multiple calls to the TeleSign
     * Verify resource.
     * <p>
     * See https://developer.telesign.com/docs/rest_api-smart-verify for detailed API documentation.
     */
    public TelesignResponse smart(String phoneNumber, String ucid, Map<String, String> params) throws IOException, GeneralSecurityException {

        if (params == null) {
            params = new HashMap<>();
        }

        params.put("phone_number", phoneNumber);
        params.put("ucid", ucid);

        return this.post(VERIFY_SMART_RESOURCE, params);
    }

    /**
     * The Push Verify web service allows you to provide on-device transaction authorization for your end users. It
     * works by delivering authorization requests to your end users via push notification, and then by receiving their
     * permission responses via their mobile device's wireless Internet connection.
     * <p>
     * See https://developer.telesign.com/docs/rest_api-verify-push for detailed API documentation.
     */
    public TelesignResponse push(String phoneNumber, String ucid, Map<String, String> params) throws IOException, GeneralSecurityException {

        if (params == null) {
            params = new HashMap<>();
        }

        params.put("phone_number", phoneNumber);
        params.put("ucid", ucid);

        return this.post(VERIFY_PUSH_RESOURCE, params);
    }

    /**
     * Retrieves the verification result for any verify resource.
     * <p>
     * See https://developer.telesign.com/docs/rest_api-verify-transaction-callback for detailed API documentation.
     */
    public TelesignResponse status(String referenceId, Map<String, String> params) throws IOException, GeneralSecurityException {

        return this.get(String.format(VERIFY_STATUS_RESOURCE, referenceId), params);
    }

    /**
     * Notifies TeleSign that a verification was successfully delivered to the user in order to help improve the
     * quality of message delivery routes.
     * <p>
     * See https://developer.telesign.com/docs/completion-service-for-verify-products for detailed API documentation.
     */
    public TelesignResponse completion(String referenceId, Map<String, String> params) throws IOException, GeneralSecurityException {
        return this.put(String.format(VERIFY_COMPLETION_RESOURCE, referenceId), params);
    }
}
