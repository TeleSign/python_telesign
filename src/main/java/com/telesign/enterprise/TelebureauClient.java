package com.telesign.enterprise;

import com.telesign.RestClient;

import java.io.IOException;
import java.net.Proxy;
import java.security.GeneralSecurityException;
import java.util.HashMap;
import java.util.Map;

/**
 * TeleBureau is a service is based on TeleSign's watchlist, which is a proprietary database containing verified phone
 * numbers of users known to have committed online fraud. TeleSign crowd-sources this information from its customers.
 * Participation is voluntary, but you have to contribute in order to benefit.
 */
public class TelebureauClient extends RestClient {

    private static final String TELEBUREAU_CREATE_RESOURCE = "/v1/telebureau/event";
    private static final String TELEBUREAU_RETRIEVE_RESOURCE = "/v1/telebureau/event/%s";
    private static final String TELEBUREAU_DELETE_RESOURCE = "/v1/telebureau/event/%s";

    public TelebureauClient(String customerId, String apiKey) {

        super(customerId, apiKey, "https://rest-ww.telesign.com");
    }

    public TelebureauClient(String customerId, String apiKey, String restEndpoint) {
        super(customerId, apiKey, restEndpoint);
    }

    public TelebureauClient(String customerId,
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
     * Creates a telebureau event corresponding to supplied data.
     * <p>
     * See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
     */
    public TelesignResponse createEvent(String phoneNumber, String fraudType, String occurredAt, Map<String, String> params) throws IOException, GeneralSecurityException {

        if (params == null) {
            params = new HashMap<>();
        }

        params.put("phone_number", phoneNumber);
        params.put("fraud_type", fraudType);
        params.put("occurred_at", occurredAt);

        return this.post(TELEBUREAU_CREATE_RESOURCE, params);
    }

    /**
     * Creates a telebureau event corresponding to supplied data.
     * <p>
     * See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
     */
    public TelesignResponse retrieveEvent(String referenceId, Map<String, String> params) throws IOException, GeneralSecurityException {

        return this.get(String.format(TELEBUREAU_RETRIEVE_RESOURCE, referenceId), params);
    }

    /**
     * Deletes a previously submitted fraud event. You make this call in your web application after completion of the
     * create transaction for a telebureau event.
     * <p>
     * See https://developer.telesign.com/docs/telebureau-api for detailed API documentation.
     */
    public TelesignResponse deleteEvent(String referenceId, Map<String, String> params) throws IOException, GeneralSecurityException {

        return this.delete(String.format(TELEBUREAU_DELETE_RESOURCE, referenceId), params);
    }
}
