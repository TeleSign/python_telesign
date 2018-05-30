package com.telesign.enterprise;

import java.net.Proxy;

public class MessagingClient extends com.telesign.MessagingClient {

    public MessagingClient(String customerId, String apiKey) {

        super(customerId, apiKey, "https://rest-ww.telesign.com");
    }

    public MessagingClient(String customerId, String apiKey, String restEndpoint) {
        super(customerId, apiKey, restEndpoint);
    }

    public MessagingClient(String customerId,
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
