require 'telesignenterprise'

customer_id = 'customer_id'
secret_key = 'secret_key'

phone_number = 'phone_number'
ucid = 'BACF'

phoneid_client = TelesignEnterprise::PhoneIdClient.new(customer_id, secret_key)
response = phoneid_client.score(phone_number, ucid)

if response.ok
  puts "Phone number %s has a '%s' risk level and the recommendation is to '%s' the transaction." %
           [phone_number,
            response.json['risk']['level'],
            response.json['risk']['recommendation']]
end
