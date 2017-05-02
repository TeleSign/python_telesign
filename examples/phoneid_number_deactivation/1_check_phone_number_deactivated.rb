require 'telesignenterprise'

customer_id = 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890'
api_key = 'EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=='

phone_number = 'phone_number'
ucid = 'ATCK'

phoneid_client = TelesignEnterprise::PhoneIdClient.new(customer_id, api_key)
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
