require 'telesignenterprise'

customer_id = 'customer_id'
secret_key = 'secret_key'

phone_number = 'phone_number'
my_sender_id = "my_sender_id"  # Client Services must white list any custom sender_id for it to take effect

verify_client = TelesignEnterprise::VerifyClient.new(customer_id, secret_key)
response = verify_client.sms(phone_number, sender_id: sender_id)
