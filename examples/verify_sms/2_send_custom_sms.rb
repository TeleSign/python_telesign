require 'telesignenterprise'

customer_id = 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890'
api_key = 'EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=='

phone_number = 'phone_number'
template = 'Your Widgets \'n\' More verification code is $$CODE$$.'

verify_client = TelesignEnterprise::VerifyClient.new(customer_id, api_key)
response = verify_client.sms(phone_number, template: template)
