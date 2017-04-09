require 'telesignenterprise'

customer_id = 'customer_id'
secret_key = 'secret_key'

phone_number = 'phone_number'
template = 'Your Widgets \'n\' More verification code is $$CODE$$.'

verify_client = TelesignEnterprise::VerifyClient.new(customer_id, secret_key)
response = verify_client.sms(phone_number, template: template)
