#
# Copyright (c) 2016 TeleSign
#
# TeleSign Ruby SDK sample usage.
#

require 'telesign'
require 'pp'

# update this with your credentials
customer_id = 'your customer_id'
secret_key = 'your secret_key'

# update with target phone number
phone_number = 'target phone_number'

use_case_code = 'OTHR'

verify = Telesign::API::Verify.new(customer_id, secret_key)
phoneid = Telesign::API::PhoneId.new(customer_id, secret_key)

# sample sms
verify_response = verify.sms(phone_number)
pp verify_response.body

# sample status
verify_response = verify.status(verify_response.body['reference_id'])
pp verify_response.body

# sample voice
verify_response = verify.call(phone_number)
p verify_response.body

# sample smart
verify_response = verify.smart(phone_number, use_case_code)
pp verify_response.body

# sample push
verify_response = verify.push(phone_number, use_case_code)
pp verify_response.body

# sample phoneid standard
phoneid_response = phoneid.standard(phone_number)
pp phoneid_response.body

# sample phoneid contact
phoneid_response = phoneid.contact(phone_number, use_case_code)
pp phoneid_response.body

# sample phoneid score
phoneid_response = phoneid.score(phone_number, use_case_code)
pp phoneid_response.body

# sample phoneid live
phoneid_response = phoneid.live(phone_number, use_case_code)
pp phoneid_response.body

# sample phoneid sim_swap
phoneid_response = phoneid.sim_swap(phone_number, use_case_code)
pp phoneid_response.body

# sample phoneid call_forward
phoneid_response = phoneid.call_forward(phone_number, use_case_code)
pp phoneid_response.body
