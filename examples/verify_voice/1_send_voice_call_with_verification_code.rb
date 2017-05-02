require 'telesign'
require 'telesignenterprise'

customer_id = 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890'
api_key = 'EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=='

phone_number = 'phone_number'
verify_code = Telesign::Util.random_with_n_digits(5)

verify_client = TelesignEnterprise::VerifyClient.new(customer_id, api_key)
response = verify_client.voice(phone_number, verify_code: verify_code)

print 'Please enter the verification code you were sent: '
user_entered_verify_code = gets.strip

if verify_code == user_entered_verify_code
  puts 'Your code is correct.'
else
  puts 'Your code is incorrect.'
end
