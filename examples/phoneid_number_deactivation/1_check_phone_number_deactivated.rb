require 'telesignenterprise'

customer_id = 'customer_id'
secret_key = 'secret_key'

phone_number = 'phone_number'
ucid = 'ATCK'

phoneid_client = TelesignEnterprise::PhoneIdClient.new(customer_id, secret_key)
response = phoneid_client.number_deactivation(phone_number, ucid)

if response.ok
  if response.json['number_deactivation']['last_deactivated']
    puts 'Phone number %s was last deactivated %s.' %
             [response.json['number_deactivation']['number'],
              response.json['number_deactivation']['last_deactivated']]
  else
    puts 'Phone number %s has not been deactivated.' %
             response.json['number_deactivation']['number']
  end
end
