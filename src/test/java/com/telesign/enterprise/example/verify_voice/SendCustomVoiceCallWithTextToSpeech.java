package com.telesign.enterprise.example.verify_voice;

import com.telesign.RestClient;
import com.telesign.Util;
import com.telesign.enterprise.VerifyClient;

import java.util.HashMap;

public class SendCustomVoiceCallWithTextToSpeech {

    public static void main(String[] args) {

        String customerId = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
        String apiKey = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

        String phoneNumber = "phone_number";
        String verifyCode = Util.randomWithNDigits(5);
        String ttsMessage = String.format("Hello, your code is %s. Once again, your code is %s. Goodbye.", verifyCode, verifyCode);

        HashMap<String, String> params = new HashMap<>();
        params.put("tts_message", ttsMessage);

        try {
            VerifyClient verifyClient = new VerifyClient(customerId, apiKey);
            RestClient.TelesignResponse telesignResponse = verifyClient.voice(phoneNumber, params);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}