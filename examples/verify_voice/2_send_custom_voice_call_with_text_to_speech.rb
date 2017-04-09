require 'telesign'
require 'telesignenterprise'

customer_id = 'customer_id'
secret_key = 'secret_key'

phone_number = 'phone_number'
verify_code = Telesign::Util.random_with_n_digits(5)
verify_code_with_commas = verify_code.chars.join(', ')
tts_message = "Hello, your code is #{verify_code_with_commas}. Once again, your code is #{verify_code_with_commas}. Goodbye."

verify_client = TelesignEnterprise::VerifyClient.new(customer_id, secret_key)
response = verify_client.voice(phone_number, tts_message: tts_message)

print 'Please enter the verification code you were sent: '
user_entered_verify_code = gets.strip

if verify_code == user_entered_verify_code
  puts 'Your code is correct.'
else
  puts 'Your code is incorrect.'
end
