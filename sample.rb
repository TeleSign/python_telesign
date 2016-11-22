#
# Copyright (c) 2016 TeleSign
#
# TeleSign Ruby SDK sample usage.
#

require 'telesign'
require 'date'
require 'pp'

# update this with your credentials
customer_id = 'your customer_id'
secret_key = 'your secret_key'

# update with target phone number
phone_number = 'target phone_number'

use_case_code = 'OTHR'

verify = Telesign::API::Verify.new(customer_id, secret_key)
phoneid = Telesign::API::PhoneId.new(customer_id, secret_key)
telebureau = Telesign::API::TeleBureau.new(customer_id, secret_key)

# sample sms
verify_sms_response = verify.sms(phone_number)
pp verify_sms_response.body

# sample status
verify_status_response = verify.status(verify_sms_response.body['reference_id'])
pp verify_status_response.body

# sample voice
verify_voice_response = verify.call(phone_number)
p verify_voice_response.body

# sample smart
verify_smart_response = verify.smart(phone_number, use_case_code)
pp verify_smart_response.body

# sample push
verify_push_response = verify.push(phone_number, use_case_code)
pp verify_push_response.body

# sample phoneid standard
phoneid_standard_response = phoneid.standard(phone_number)
pp phoneid_standard_response.body

# sample phoneid contact
phoneid_contact_response = phoneid.contact(phone_number, use_case_code)
pp phoneid_contact_response.body

# sample phoneid score
phoneid_score_response = phoneid.score(phone_number, use_case_code)
pp phoneid_score_response.body

# sample phoneid live
phoneid_live_response = phoneid.live(phone_number, use_case_code)
pp phoneid_live_response.body

# sample phoneid sim_swap
phoneid_sim_swap_response = phoneid.sim_swap(phone_number, use_case_code)
pp phoneid_sim_swap_response.body

# sample phoneid call_forward
phoneid_call_forward_response = phoneid.call_forward(phone_number, use_case_code)
pp phoneid_call_forward_response.body

# sample phoneid number_deactivation
phoneid_number_deactivation_response = phoneid.number_deactivation(phone_number, use_case_code)
pp phoneid_number_deactivation_response.body

# sample telebureau create
fraud_type = 'takeover'
occurred_at = '2016-11-22T00:43:44Z'
telebureau_create_response = telebureau.create(phone_number, fraud_type, occurred_at)
pp telebureau_create_response.body

# sample telebureau retrieve
telebureau_retrieve_response = telebureau.retrieve(telebureau_create_response.body['reference_id'])
pp telebureau_retrieve_response.body

# sample telebureau delete
telebureau_delete_response = telebureau.delete(telebureau_create_response.body['reference_id'])
pp telebureau_delete_response.body
