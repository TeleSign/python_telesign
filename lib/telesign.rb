#
# Copyright (c) 2016 TeleSign
#
# TeleSign Ruby SDK REST API endpoints.
#
# The api module contains Python classes and methods that allow you to
# use the Ruby programming language to programmatically access the
# Verify and PhoneId TeleSign web services.
#

require 'telesign/rest'

module Telesign

  module API

    # The PhoneId class exposes services that each provide detailed
    # information about a specified phone number.
    class PhoneId < Telesign::API::Rest

      def initialize(customer_id,
                     secret_key,
                     ssl=true,
                     api_host='rest.telesign.com',
                     timeout=nil)

        super(customer_id,
              secret_key,
              ssl,
              api_host,
              timeout)
      end

      # Retrieves the standard set of details about the specified phone number.
      # This includes the type of phone (e.g., land line or mobile), and it's
      # approximate geographic location.
      def standard(phone_number,
                   use_case_code=nil,
                   extra=nil,
                   timeout=nil)

        params = {}

        unless use_case_code.nil?
          params[:ucid] = use_case_code
        end

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Get,
                "/v1/phoneid/standard/#{phone_number}",
                params,
                nil,
                timeout)
      end

      # Retrieves a score for the specified phone number. This ranks the phone number's
      # "risk level" on a scale from 0 to 1000, so you can code your web application to
      # handle particular use cases (e.g., to stop things like chargebacks, identity
      # theft, fraud, and spam).
      def score(phone_number,
                use_case_code,
                extra=nil,
                timeout=nil)

        params = {:ucid => use_case_code}

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Get,
                "/v1/phoneid/score/#{phone_number}",
                params,
                nil,
                timeout)
      end

      # In addition to the information retrieved by standard, this service provides the
      # Name & Address associated with the specified phone number.
      def contact(phone_number,
                  use_case_code,
                  extra=nil,
                  timeout=nil)

        params = {:ucid => use_case_code}

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Get,
                "/v1/phoneid/contact/#{phone_number}",
                params,
                nil,
                timeout)
      end

      # In addition to the information retrieved by standard, this service provides
      # actionable data associated with the specified phone number.
      def live(phone_number,
               use_case_code,
               extra=nil,
               timeout=nil)

        params = {:ucid => use_case_code}

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Get,
                "/v1/phoneid/live/#{phone_number}",
                params,
                nil,
                timeout)
      end

      # In addition to the information retrieved by standard, this service provides
      # data about potential sim_swaps associated with the specified phone number.
      def sim_swap(phone_number,
                   use_case_code,
                   extra=nil,
                   timeout=nil)

        params = {:ucid => use_case_code}

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Get,
                "/v1/phoneid/sim_swap/check/#{phone_number}",
                params,
                nil,
                timeout)
      end

      # In addition to the information retrieved by standard, this service provides
      # information on call forwarding for the phone number provided.
      def call_forward(phone_number,
                       use_case_code,
                       extra=nil,
                       timeout=nil)

        params = {:ucid => use_case_code}

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Get,
                "/v1/phoneid/call_forward/#{phone_number}",
                params,
                nil,
                timeout)
      end

      # In addition to the information retrieved by standard, this service provides
      # information on call forwarding for the phone number provided.
      def number_deactivation(phone_number,
                              use_case_code,
                              extra=nil,
                              timeout=nil)

        params = {:ucid => use_case_code}

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Get,
                "/v1/phoneid/number_deactivation/#{phone_number}",
                params,
                nil,
                timeout)
      end

    end

    # The Verify class exposes several services for sending users a verification
    # token. You can use this mechanism to simply test whether you can reach users
    # at the phone number they supplied, or you can have them use the token to
    # authenticate themselves with your web application.
    #
    # This class also exposes a service that is used in conjunction with the first
    # two services, in that it allows you to confirm the result of the authentication.
    #
    # You can use this verification factor in combination with username & password to
    # provide two-factor authentication for higher security.
    class Verify < Telesign::API::Rest

      def initialize(customer_id,
                     secret_key,
                     ssl=true,
                     api_host='rest.telesign.com',
                     timeout=nil)

        super(customer_id,
              secret_key,
              ssl,
              api_host,
              timeout)
      end

      # Sends a text message containing the verification code, to the specified
      # phone number (supported for mobile phones only).
      def sms(phone_number,
              use_case_code=nil,
              extra=nil,
              timeout=nil)

        params = {:phone_number => phone_number}

        unless use_case_code.nil?
          params[:use_case_code] = use_case_code
        end

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Post,
                "/v1/verify/sms",
                nil,
                params,
                timeout)
      end

      # Calls the specified phone number, and using speech synthesis, speaks the
      # verification code to the user.
      def call(phone_number,
               use_case_code=nil,
               extra=nil,
               timeout=nil)

        params = {:phone_number => phone_number}

        unless use_case_code.nil?
          params[:use_case_code] = use_case_code
        end

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Post,
                "/v1/verify/call",
                nil,
                params,
                timeout)
      end

      # Calls the specified phone number, and using speech synthesis, speaks the
      # verification code to the user.
      def smart(phone_number,
                use_case_code,
                extra=nil,
                timeout=nil)

        params = {:phone_number => phone_number,
                  :ucid => use_case_code}

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Post,
                "/v1/verify/smart",
                nil,
                params,
                timeout)

      end

      # The **push** method sends a push notification containing the verification
      # code to the specified phone number (supported for mobile phones only).
      def push(phone_number,
               use_case_code,
               extra=nil,
               timeout=nil)

        params = {:phone_number => phone_number,
                  :ucid => use_case_code}

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Post,
                "/v2/verify/push",
                nil,
                params,
                timeout)

      end

      # Retrieves the verification result. You make this call in your web application
      # after users complete the authentication transaction (using either a call or sms).
      def status(reference_id,
                 verify_code=nil,
                 extra=nil,
                 timeout=nil)

        params = {}

        unless verify_code.nil?
          params[:verify_code] = verify_code
        end

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Get,
                "/v1/verify/#{reference_id}",
                params,
                nil,
                timeout)
      end
    end


    # The **Telebureau** class exposes services for creating, retrieving, updating and
    # deleting telebureau fraud events. You can use this mechanism to simply test whether
    # you can reach telebureau services.
    class TeleBureau < Telesign::API::Rest

      def initialize(customer_id,
                     secret_key,
                     ssl=true,
                     api_host='rest.telesign.com',
                     timeout=nil)

        super(customer_id,
              secret_key,
              ssl,
              api_host,
              timeout)
      end

      # Creates a telebureau event corresponding to supplied data.
      def create(phone_number,
                 fraud_type,
                 occurred_at,
                 extra=nil,
                 timeout=nil)

        params = {:phone_number => phone_number,
                  :fraud_type => fraud_type,
                  :occurred_at => occurred_at}

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Post,
                "/v1/telebureau/event",
                nil,
                params,
                timeout)
      end

      # Retrieves the fraud event status. You make this call in your web application after
      # completion of create transaction for a telebureau event.
      def retrieve(reference_id,
                   extra=nil,
                   timeout=nil)

        params = {}

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Get,
                "/v1/telebureau/event/#{reference_id}",
                params,
                nil,
                timeout)
      end

      # Deletes a previously submitted fraud event. You make this call in your web application
      # after completion of the create transaction for a telebureau event.
      def delete(reference_id,
                 extra=nil,
                 timeout=nil)

        params = {}

        unless extra.nil?
          params.merge!(extra)
        end

        execute(Net::HTTP::Delete,
                "/v1/telebureau/event/#{reference_id}",
                params,
                nil,
                timeout)
      end
    end
  end
end