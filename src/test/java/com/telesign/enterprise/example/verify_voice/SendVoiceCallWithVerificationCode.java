package com.telesign.enterprise.example.verify_voice;

import com.telesign.RestClient;
import com.telesign.Util;
import com.telesign.enterprise.VerifyClient;

import java.util.HashMap;
import java.util.Scanner;

public class SendVoiceCallWithVerificationCode {

    public static void main(String[] args) {

        String customerId = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890";
        String apiKey = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==";

        String phoneNumber = "phone_number";
        String verifyCode = Util.randomWithNDigits(5);

        HashMap<String, String> params = new HashMap<>();
        params.put("verify_code", verifyCode);

        try {
            VerifyClient verifyClient = new VerifyClient(customerId, apiKey);
            RestClient.TelesignResponse telesignResponse = verifyClient.voice(phoneNumber, params);

            Scanner s = new Scanner(System.in);
            System.out.println("Please enter your verification code:");
            String code = s.next();

            if (verifyCode.equalsIgnoreCase(code)) {
                System.out.println("Your code is correct.");
            } else {
                System.out.println("Your code is incorrect.");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}