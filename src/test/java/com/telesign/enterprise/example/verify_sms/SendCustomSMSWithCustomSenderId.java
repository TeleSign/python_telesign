package com.telesign.enterprise.example.verify_sms;

import com.telesign.RestClient;
import com.telesign.enterprise.VerifyClient;

import java.util.HashMap;

public class SendCustomSMSWithCustomSenderId {

    public static void main(String[] args) {

        String customerId = "customer_id";
        String secretKey = "secret_key";

        String phoneNumber = "phone_number";
        String mySenderId = "my_sender_id";

        HashMap<String, String> params = new HashMap<>();
        params.put("sender_id", mySenderId);

        try {
            VerifyClient verifyClient = new VerifyClient(customerId, secretKey);
            RestClient.TelesignResponse telesignResponse = verifyClient.sms(phoneNumber, params);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}