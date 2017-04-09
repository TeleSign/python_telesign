# encoding: UTF-8
require 'telesignenterprise'

customer_id = 'customer_id'
secret_key = 'secret_key'

phone_number = 'phone_number'
language = 'fr-FR'
tts_message = 'Votre code de vérification Widgets \'n\' More est $$CODE$$.'

verify_client = TelesignEnterprise::VerifyClient.new(customer_id, secret_key)
response = verify_client.voice(phone_number, language: language, tts_message: tts_message)
