package com.telesign.enterprise.example.verify_voice;

import com.telesign.RestClient;
import com.telesign.Util;
import com.telesign.enterprise.VerifyClient;

import java.util.HashMap;

public class SendCustomVoiceCallWithTextToSpeech {

    public static void main(String[] args) {

        String customerId = "customer_id";
        String secretKey = "secret_key";

        String phoneNumber = "phone_number";
        String verifyCode = Util.randomWithNDigits(5);
        String ttsMessage = String.format("Hello, your code is %s. Once again, your code is %s. Goodbye.", verifyCode, verifyCode);

        HashMap<String, String> params = new HashMap<>();
        params.put("tts_message", ttsMessage);

        try {
            VerifyClient verifyClient = new VerifyClient(customerId, secretKey);
            RestClient.TelesignResponse telesignResponse = verifyClient.voice(phoneNumber, params);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}