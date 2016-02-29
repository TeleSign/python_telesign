#
# Copyright (c) 2016 TeleSign
#
# TeleSign Ruby SDK HMAC REST Auth.
#

require 'pp'
require 'json'
require 'time'
require 'base64'
require 'openssl'
require 'net/http'

module Telesign

  module API

    # == TeleSign Ruby SDK REST API Helper
    #
    # Telesign::API::Rest provides helper classes and functions
    # to handle the HMAC REST authentication.
    #
    # You can use these helper functions directly or via the Telesign::API::PhoneId
    # and Telesign::API::Verify classes. Please see the TeleSign REST API docs at
    # http://docs.telesign.com/rest/index.html for implementation details.
    #
    class Rest

      # Creates a new Telesign::API::Rest object with the specified credentials
      # and HTTP configuration.
      # The +api_host+ should be a DNS hostname or IP address.
      def initialize(customer_id,
                     secret_key,
                     ssl,
                     api_host,
                     timeout=nil)

        @customer_id = customer_id
        @secret_key = secret_key
        @ssl = ssl
        @base_uri = URI("http#{ssl ? 's' : ''}://#{api_host}")
        @timeout = timeout
        @user_agent = 'Net::HTTP TeleSignSDK/ruby-1.0.0'
      end

      # Executes the REST API request based on the given configuration.
      # See Telesign::API::PhoneId and Telesign::API::Verify for specific
      # usage.
      def execute(verb,
                  resource,
                  params=nil,
                  form_data=nil,
                  timeout=nil)

        # generate the headers
        headers = generate_auth_headers(
            @customer_id,
            @secret_key,
            resource,
            verb,
            form_data.nil? ? nil : URI.encode_www_form(form_data))

        uri = URI.join(@base_uri, resource)

        # set query params
        uri.query = URI.encode_www_form(params) unless params.nil?

        # configure HTTP object
        http = Net::HTTP.new(uri.host, uri.port)
        http.use_ssl = @ssl

        http.open_timeout = timeout.nil? ? @timeout : timeout
        http.read_timeout = http.open_timeout
        http.ssl_timeout = http.open_timeout
        http.continue_timeout = http.open_timeout

        #set headers
        request = verb.new uri.request_uri
        headers.each do |k, v|
          request[k] = v
        end

        # set post data
        request.set_form_data(form_data) unless form_data.nil?

        # do the request
        http_response = http.request(request)

        # check response
        unless http_response.is_a? Net::HTTPSuccess
          if http_response.is_a? Net::HTTPUnauthorized
            raise Telesign::API::AuthError.new(http_response)
          else
            raise Telesign::API::APIError.new(http_response)
          end
        end

        Telesign::API::APIResponse.new(http_response)
      end

      # Function to generate the REST API authentication headers. A signature is
      # computed based on the contents of the request and the client's secret key.
      def generate_auth_headers (customer_id,
                                 secret_key,
                                 resource,
                                 verb,
                                 form_data=nil,
                                 content_type='')

        datetime_stamp = Time.now.utc.to_datetime.rfc822
        nonce = rand.to_s

        content_type = 'application/x-www-form-urlencoded' if verb == Net::HTTP::Post or verb == Net::HTTP::Put

        string_to_sign = "#{verb.name.split('::').last.upcase}\n" +
            "#{content_type}\n\n" +
            "x-ts-auth-method:#{'HMAC-SHA256'}\n" +
            "x-ts-date:#{datetime_stamp}\n" +
            "x-ts-nonce:#{nonce}"

        string_to_sign = "#{string_to_sign}\n#{form_data}" unless form_data.nil?

        string_to_sign = string_to_sign + "\n#{resource}"

        signature = Base64.encode64(OpenSSL::HMAC.digest(OpenSSL::Digest.new('sha256'),
                                                         Base64.decode64(secret_key), string_to_sign)).chomp

        {
            'Authorization' => "TSA #{customer_id}:#{signature}",
            'x-ts-date' => datetime_stamp,
            'x-ts-auth-method' => 'HMAC-SHA256',
            'x-ts-nonce' => nonce,
            'User-Agent' => @user_agent
        }
      end
    end

    class APIResponse

      attr_accessor :body, :headers, :status, :verify_code

      def initialize(http_response,
                     verify_code=nil)

        @body = JSON.parse(http_response.body)
        @headers = http_response.to_hash
        @status = http_response.code
        @verify_code = verify_code
      end
    end

    class APIError < StandardError

      attr_accessor :errors, :headers, :status, :body

      def initialize(http_response)

        @errors = JSON.parse(http_response.body)['errors']
        @headers = http_response.to_hash
        @status = http_response.code
        @body = http_response.body
      end

      def to_s
        result = ''
        @errors.each do |error|
          result = "#{result}#{error['description']}\n"
        end

        result
      end
    end

    class AuthError < Telesign::API::APIError

      def initialize(http_response)
        super(http_response)
      end
    end
  end
end