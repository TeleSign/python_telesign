# encoding: UTF-8
require 'telesignenterprise'

customer_id = 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890'
api_key = 'EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=='

phone_number = 'phone_number'
language = 'fr-FR'
tts_message = 'Votre code de vérification Widgets \'n\' More est $$CODE$$.'

verify_client = TelesignEnterprise::VerifyClient.new(customer_id, api_key)
response = verify_client.voice(phone_number, language: language, tts_message: tts_message)
