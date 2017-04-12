package com.telesign.enterprise.example.verify_sms;

import com.telesign.RestClient;
import com.telesign.enterprise.VerifyClient;

import java.util.HashMap;

public class SendCustomSMS {

    public static void main(String[] args) {

        String customerId = "customer_id";
        String secretKey = "secret_key";

        String phoneNumber = "phone_number";
        String template = "Your Widgets 'n' More verification code is $$CODE$$.";

        HashMap<String, String> params = new HashMap<>();
        params.put("template", template);

        try {
            VerifyClient verifyClient = new VerifyClient(customerId, secretKey);
            RestClient.TelesignResponse telesignResponse = verifyClient.sms(phoneNumber, params);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}