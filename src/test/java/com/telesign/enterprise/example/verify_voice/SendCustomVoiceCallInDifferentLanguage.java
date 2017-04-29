package com.telesign.enterprise.example.verify_voice;

import com.telesign.RestClient;
import com.telesign.enterprise.VerifyClient;

import java.util.HashMap;

public class SendCustomVoiceCallInDifferentLanguage {

    public static void main(String[] args) {

        String customerId = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
        String apiKey = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

        String phoneNumber = "phone_number";
        String language = "fr-FR";
        String ttsMessage = "Votre code de vérification Widgets 'n' More est $$CODE$$.";

        HashMap<String, String> params = new HashMap<>();
        params.put("language", language);
        params.put("tts_message", ttsMessage);

        try {
            VerifyClient verifyClient = new VerifyClient(customerId, apiKey);
            RestClient.TelesignResponse telesignResponse = verifyClient.voice(phoneNumber, params);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}