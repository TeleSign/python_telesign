package com.telesign.enterprise.example.verify_sms;

import com.telesign.RestClient;
import com.telesign.Util;
import com.telesign.enterprise.VerifyClient;

import java.util.HashMap;

public class SendSMSWithVerificationCode {

    public static void main(String[] args) {

        String customerId = "customer_id";
        String secretKey = "secret_key";

        String phoneNumber = "phone_number";
        String verifyCode = Util.randomWithNDigits(5);

        HashMap<String, String> params = new HashMap<>();
        params.put("verify_code", verifyCode);

        try {
            VerifyClient verifyClient = new VerifyClient(customerId, secretKey);
            RestClient.TelesignResponse telesignResponse = verifyClient.sms(phoneNumber, params);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
