<?php

/*
  Copyright (c) TeleSign Corporation 2012.
  License: MIT
  Support email address "support@telesign.com"
  Author: lqm1010
 */

/**
 * This file defines the the API SDK for Telesign
 * 
 * Copyright (c) TeleSign Corporation 2012.
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 *
 * @author lqm1010 <lqm1010@gmail.com>
 */

/**
* Telesign Class is common class for PhoneId and Verify class to extends
*
* @package  Telesign_PHP_SDK
* @access   public
*/
class Telesign {

	protected $curl;
	protected $method;
	protected $content_type;
	protected $timestamp;
	protected $curl_headers;
	protected $post_variables;
	protected $raw_response;
	protected $curl_error_num;
	protected $curl_error_desc;

	/**
	 * Implementation of the TeleSign api 
	 * 
	 * @param string $customer_id The TeleSign customer id. 
	 * @param string $secret_key The TeleSign secret key 
	 * @param string $auth_method [optional] Authentication Method
	 * @param string $api_url [optional] API url
	 * @param string $request_timeout [optional] Request timeout 
	 * @param string $headers [optional] Headers
	 * @param string $curl_options [optional] Curl (optional)options
	 */
	function __construct(
	$customer_id, $secret_key, // required
		$auth_method = "hmac-sha1", // also accepted: "hmac-sha256"
		$api_url = "https://rest.telesign.com", $request_timeout = 5, // seconds
		$headers = array(), $curl_options = array()
	) {

		// the encoding key is actually the base64 decoded form of the secret key
		$this->customer_id = $customer_id;
		$this->key = base64_decode($secret_key);
		$this->auth_method = $auth_method;
		$this->api_url = $api_url;

		// note that we're initializing the timestamp at instantiation time, so we can have
		//   a const reference to it during the lifetime of the object; this means, however, 
		//   that once we create the object, we do want to use it pretty soon after, so we
		//   dont run out of the Telesign time window restriction (currently 15min)
		// if your use case is to instantiate an object and then submit multiple requests 
		//   with it, feel free to use the time() function instead of the $timestamp variable
		//   in the _sign() function below
		$this->timestamp = time();

		// get a curl object and set its options
		$this->curl = curl_init();
		curl_setopt($this->curl, CURLOPT_TIMEOUT, $request_timeout);
		curl_setopt($this->curl, CURLOPT_RETURNTRANSFER, TRUE);
		curl_setopt($this->curl, CURLOPT_USERAGENT, "TelesignSDK/php1.0");

		foreach ($curl_options as $opt => $val) {
			curl_setopt($this->curl, $opt, $val);
		}

		$this->curl_headers = $headers;
		$this->post_variables = array();
		$this->raw_response = "";
		$this->curl_error_num = -1;
		$this->curl_error_desc = "";
	}

	/**
	 * Create API signature per Telesign recipe
	 * 
	 * @param string $resource The TeleSign service. 
	 * @param string $post_data Data pass to the service
	 */
	protected function _sign($resource, $post_data = "") {
		// take care of the X-TS- custom headers
		$nonce = uniqid();
		$x_ts_date = date("D, j M Y H:i:s O", $this->timestamp);
		$x_ts_headers =
			"x-ts-auth-method:" . $this->auth_method . "\n" .
			"x-ts-date:" . $x_ts_date . "\n" .
			"x-ts-nonce:" . $nonce
		;

		$this->curl_headers['X-TS-Auth-Method'] = $this->auth_method;
		$this->curl_headers['X-TS-Date'] = $x_ts_date;
		$this->curl_headers['X-TS-Nonce'] = $nonce;

		// put it all together and create the Authorization header
		$signature =
			$this->method . "\n" .
			$this->content_type . "\n" .
			"\n" .
			$x_ts_headers . "\n" .
			(strlen($post_data) ? ($post_data . "\n") : "") .
			$resource
		;
		$this->curl_headers['Authorization'] = "TSA " . $this->customer_id . ":" . base64_encode(hash_hmac(substr($this->auth_method, 5), $signature, $this->key, TRUE));
	}

	/**
	 * Submit post data to service url and get response
	 * 
	 * @param string $post_data Data pass to the service
	 * @return string Raw data receive from service
	 */
	protected function _submit_and_get_response($post_data = "") {

		// apply all http headers (curl wants them in a flat array)
		$headers = array();
		$this->curl_headers['Content-Type'] = $this->content_type;
		foreach ($this->curl_headers as $hname => $hval) {
			$headers[] = $hname . ": " . $hval;
		}
		curl_setopt($this->curl, CURLOPT_HTTPHEADER, $headers);

		// curl settings for POST
		if (strlen($post_data)) {
			curl_setopt($this->curl, CURLOPT_POST, TRUE);
			curl_setopt($this->curl, CURLOPT_POSTFIELDS, $post_data);
		} else {
			curl_setopt($this->curl, CURLOPT_POST, FALSE);
		}

		// run the curl and get information
		$this->raw_response = curl_exec($this->curl);
		$this->curl_error_num = curl_errno($this->curl);
		$this->curl_error_desc = curl_error($this->curl);

		// if there is error then return empty string
		if ($this->curl_error_num) {
			return "";
		}

		return $this->raw_response;
	}

	/**
	 * General verify function that support for child function
	 * 
	 * @param string $phone_number The phone number to send to service
	 * @param string $verify_code The code to send to service. Set to null to let Telesign generate the code
	 * @param string $service Service that this function use
	 * @param string $more More data to send to service
	 * 
	 * @return string The fully formed response object repersentation of the JSON reply
	 */
	public function verify($phone_number, $verify_code, $service = "call", $more = array()) {

		// build the POST contents string
		$post_data = "phone_number=" . $phone_number . "&" . (strlen($verify_code) ? ("verify_code=" . $verify_code . "&") : "");
		foreach ($more as $arg_name => $arg_value) {
			$post_data .= $arg_name . "=" . urlencode($arg_value) . "&";
		}
		$post_data = substr($post_data, 0, -1);

		// build verify url
		$resource = "/v1/verify/" . $service;
		$url = $this->api_url . $resource;
		curl_setopt($this->curl, CURLOPT_URL, $url);

		$this->method = "POST";
		$this->content_type = "application/x-www-form-urlencoded";

		$this->_sign($resource, $post_data);
		return json_decode($this->_submit_and_get_response($post_data), TRUE);
	}

	/**
	 * General phondid function that support for child function
	 * 
	 * @param string $phone_number The phone number to send to service
	 * @param string $service Service that this function use
	 * @param string $more More data to send to service
	 * 
	 * @return string The fully formed response object repersentation of the JSON reply
	 */
	public function phoneid($phone_number, $service = "standard", $more = array()) {

		// build phoneid url
		$resource = "/v1/phoneid/" . $service . "/" . $phone_number;
		$url = $this->api_url . $resource;
		if (count($more)) {
			$url .= "?";
			foreach ($more as $arg_name => $arg_value) {
				$url .= $arg_name . "=" . urlencode($arg_value) . "&";
			}
			$url = substr($url, 0, -1);
		}
		curl_setopt($this->curl, CURLOPT_URL, $url);

		$this->method = "GET";
		$this->content_type = "text/plain";

		$this->_sign($resource);
		return json_decode($this->_submit_and_get_response(), TRUE);
	}

	/**
	 * Return a reference to the curl object
	 * 
	 * @return object The curl object
	 */
	public function get_curl_handle() {
		return $this->curl;
	}

	/**
	 * Return curl execution error; it would return -1 if curl request is not initiated or is in progress, but once done it will return the codes from here: http://curl.haxx.se/libcurl/c/libcurl-errors.html
	 * 
	 * @return int 
	 */
	public function get_curl_error_number() {
		return $this->curl_error_num;
	}

	/**
	 * Return curl error message 
	 * 
	 * @return string
	 */
	public function get_curl_error_message() {
		return $this->curl_error_desc;
	}

	/**
	 * Return http status after execution, 0 if not obtained (yet)
	 * 
	 * @return string
	 */
	public function get_http_status() {
		if ($this->curl_error_num) {
			return 0;
		}
		return curl_getinfo($this->curl, CURLINFO_HTTP_CODE);
	}

}

/**
* The Verify class exposes two services for sending users a verification token (a three to five-digit number). 
* You can use this mechanism to simply test whether you can reach users at the phone number they supplied, or you can have them use the token to authenticate themselves with your web application. In addition, this class also exposes a service that allows you to confirm the result of the authentication.
*
* @package  Telesign_PHP_SDK
* @access   public
*/
class Verify extends Telesign {

	/**
	 * Make a Verify API call to TeleSigns phone service. Calling this method 
	 * results in an automated phone call made to the given identifier. The language
	 * is specified as a string. Extensions and delays are programmable using the
	 * extension_type and extension template. 
	 * 
	 * @link https://portal.telesign.com/docs/content/verify-call.html
	 * 
	 * @param string $phone_number The phone number of the person to dial
	 * @param string $verify_code [optional] if null, verify code will be generated by telesign
	 * @param string $language [optional] The language code of the call 
	 * @param string $verify_method [optional] Only available option is currently null (dictated code) or "keypress"
	 * @param string $extension_type [optional] If 0, no extension. if 1, DTMF extension. If 2, voice extension
	 * @param string $extension_template [optional] If null not used. Otherwise the extension to reach 
	 * @param string $redial [optional]
	 * 
	 * @return string The fully formed response object repersentation of the JSON reply
	 */
	public function call($phone_number, $verify_code = "", $language = "", $verify_method = "", $extension_type = "", $extension_template = "", $redial = "", $more = array()) {
		if (!empty($language)) {
			$more['language'] = $language;
		}
		if (!empty($verify_method)) {
			$more['verify_method'] = $verify_method;
		}
		if (!empty($extension_type)) {
			$more['extension_type'] = $extension_type;
		}
		if (!empty($extension_template)) {
			$more['extension_template'] = $extension_template;
		}
		if (!empty($redial)) {
			$more['redial'] = $redial;
		}
		return $this->verify($phone_number, $verify_code, 'call', $more);
	}

	/**
	 * Make a Verify SMS request to TeleSign's API. This method allows 
	 * the language, verification code and template of the message to be set. 
	 * 
	 * @link https://portal.telesign.com/docs/content/verify-sms.html
	 * 
	 * @param string $phone_number The phone number to send the sms message
	 * @param string $verify_code [optional] The code to send via sms. Set to null to let Telesign generate the code
	 * @param string $language [optional] The String representation of the language to send the sms message
	 * @param string $template [optional] The template of the message that is being sent. Set to null for default, otherwise must include $$CODE$$ as a variable placeholder
	 * 
	 * @return string The fully formed response object repersentation of the JSON reply
	 */
	public function sms($phone_number, $verify_code = "", $language = "", $template = "") {
		$more = array();
		if (!empty($language)) {
			$more['language'] = $language;
		}
		if (!empty($template)) {
			$more['template'] = $template;
		}
		return $this->verify($phone_number, $verify_code, 'sms', $more);
	}

	/**
	 * Return the results of the post referenced by the reference_id. After a verify 
	 * SMS or Call has been made, the status of that verification request can be retrieved
	 * with this method. 
	 * 
	 * @param string $reference The id returned from either requestsSMS or requestCall
	 * @param string $verify_code [optional] The verification code received from the user
	 * 
	 * @return string The fully formed response object repersentation of the JSON reply
	 */
	public function status($reference, $verify_code = "") {
		// build verify url
		$resource = "/v1/verify/" . $reference;
		$url = $this->api_url . $resource . (strlen($verify_code) ? ("?verify_code=" . $verify_code) : "");
		curl_setopt($this->curl, CURLOPT_URL, $url);

		$this->method = "GET";
		$this->content_type = "text/plain";

		$this->_sign($resource);
		return json_decode($this->_submit_and_get_response(), TRUE);
	}

}

/**
* The PhoneId class exposes three services that each provide information about a specified phone number.
*
* @package  Telesign_PHP_SDK
* @access   public
*/
class PhoneId extends Telesign {

	/**
	 * Make a phoneid standard request to Telesign's public API. Requires the 
	 * phone number. The method creates a @see TeleSignRequest for the standard
	 * api, signs it using the standard SHA1 hash, and performs a GET request. 
	 * 
	 * @link https://portal.telesign.com/docs/content/phoneid-standard.html
	 * 
	 * @param string a US phone number to make the standard request against.
	 * 
	 * @return string The fully formed response object repersentation of the JSON reply
	 */
	public function standard($phone_number) {
		return $this->phoneid($phone_number, "standard");
	}

	/**
	 * Make a phoneid score request to TeleSign's public API. Requires the 
	 * phone number and a string representing the use case code. The method 
	 * creates a request for the score api, signs it using 
	 * the standard SHA1 hash, and performs a GET request.
	 * 
	 * @link https://portal.telesign.com/docs/content/phoneid-score.html
	 * @link https://portal.telesign.com/docs/content/xt/xt-use-case-codes.html#xref-use-case-codes
	 * 
	 * @param string a US phone number to make the standard request against.
	 * @param string ucid a TeleSign Use Case Code 
	 * 
	 * @return string The fully formed response object repersentation of the JSON reply
	 */
	public function score($phone_number, $ucid) {
		return $this->phoneid($phone_number, "score", array("ucid" => $ucid));
	}

	/**
	 * Make a phoneid score request to TeleSign's public API. Requires the 
	 * phone number and a string representing the use case code. The method 
	 * creates a request for the score api, signs it using 
	 * the standard SHA1 hash, and performs a GET request.
	 * 
	 * @link https://portal.telesign.com/docs/content/phoneid-contact.html
	 * @link https://portal.telesign.com/docs/content/xt/xt-use-case-codes.html#xref-use-case-codes
	 * 
	 * @param string a US phone number to make the standard request against.
	 * @param string ucid a TeleSign Use Case Code 
	 * 
	 * @return string The fully formed response object repersentation of the JSON reply
	 */
	public function contact($phone_number, $ucid) {
		return $this->phoneid($phone_number, "contact", array("ucid" => $ucid));
	}

	/**
	 * Make a phoneid score request to TeleSign's public API. Requires the 
	 * phone number and a string representing the use case code. The method 
	 * creates a request for the score api, signs it using 
	 * the standard SHA1 hash, and performs a GET request.
	 * 
	 * @link https://portal.telesign.com/docs/content/phoneid-live.html
	 * @link https://portal.telesign.com/docs/content/xt/xt-use-case-codes.html#xref-use-case-codes
	 * 
	 * @param string a US phone number to make the standard request against.
	 * @param string ucid a TeleSign Use Case Code 
	 * 
	 * @return string The fully formed response object repersentation of the JSON reply
	 */
	public function live($phone_number, $ucid) {
		return $this->phoneid($phone_number, "live", array("ucid" => $ucid));
	}

}

