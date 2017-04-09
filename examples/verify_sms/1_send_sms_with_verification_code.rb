require 'telesign'
require 'telesignenterprise'

customer_id = 'customer_id'
secret_key = 'secret_key'

phone_number = 'phone_number'
verify_code = Telesign::Util.random_with_n_digits(5)

verify_client = TelesignEnterprise::VerifyClient.new(customer_id, secret_key)
response = verify_client.sms(phone_number, verify_code: verify_code)

print 'Please enter the verification code you were sent: '
user_entered_verify_code = gets.strip

if verify_code == user_entered_verify_code
  puts 'Your code is correct.'
else
  puts 'Your code is incorrect.'
end
