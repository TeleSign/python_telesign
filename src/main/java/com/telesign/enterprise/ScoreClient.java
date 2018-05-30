package com.telesign.enterprise;

import java.net.Proxy;

public class ScoreClient extends com.telesign.ScoreClient {

    public ScoreClient(String customerId, String apiKey) {

        super(customerId, apiKey, "https://rest-ww.telesign.com");
    }

    public ScoreClient(String customerId, String apiKey, String restEndpoint) {
        super(customerId, apiKey, restEndpoint);
    }

    public ScoreClient(String customerId,
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

}
