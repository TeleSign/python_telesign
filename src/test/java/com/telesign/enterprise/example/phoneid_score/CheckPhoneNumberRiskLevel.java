package com.telesign.enterprise.example.phoneid_score;

import com.telesign.RestClient;
import com.telesign.enterprise.PhoneIdClient;

public class CheckPhoneNumberRiskLevel {

    public static void main(String[] args) {

        String customerId = "customer_id";
        String secretKey = "secret_key";

        String phoneNumber = "phone_number";
        String ucid = "BACF";

        try {
            PhoneIdClient phoneIdClient = new PhoneIdClient(customerId, secretKey);
            RestClient.TelesignResponse telesignResponse = phoneIdClient.score(phoneNumber, ucid, null);

            if (telesignResponse.ok) {
                System.out.println(String.format("Phone number %s has a '%s' risk level and the recommendation is to '%s' the transaction.",
                        phoneNumber,
                        telesignResponse.json.getAsJsonObject("risk").get("level").getAsString(),
                        telesignResponse.json.getAsJsonObject("risk").get("recommendation").getAsString()));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}