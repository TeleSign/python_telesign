"""

.. module:: telesign.api
    :synopsis: The **api** module contains Python classes and methods that allow you to use the Python programming language to programmatically access the **Verify** and **PhoneId** TeleSign web services.

"""
from __future__ import print_function 
from __future__ import unicode_literals

import json
from random import SystemRandom
import requests

from telesign import __version__

from telesign.auth import generate_auth_headers
from telesign.exceptions import TelesignError, AuthorizationError

__author__ = "TeleSign"
__copyright__ = "Copyright 2016, TeleSign Corp."
__credits__ = [
    "Jeremy Cunningham",
    "Radu Maierean",
    "Michael Fox",
    "Nancy Vitug",
    "Humberto Morales",
    "Jeff Putnam",
    "Jarrad Lee"]
__license__ = "MIT"
__maintainer__ = "TeleSign Corp."
__email__ = "support@telesign.com"
__status__ = "Production"


def to_utc_rfc3339(a_datetime):
    """
    Helper function to format a timezone unaware datetime in rfc3339 utc timestamp the easy way.

    :param a_datetime: timezone unaware datetime object
    :return: rfc3339 timestamp
    """
    return "{}Z".format(a_datetime.replace(microsecond=0).isoformat())


def random_with_n_digits(n):
    """
    Helper function to generate a random number n digits in length using a system random.

    :param n: n length digit code to generate
    :return: a digit code of n length
    """
    return "".join(SystemRandom().choice('0123456789') for _ in range(n))


class Response(object):
    def __init__(self, data, http_response, verify_code=None):
        self.data = data
        self.headers = http_response.headers
        self.status = http_response.status_code
        self.raw_data = http_response.text
        self.verify_code = verify_code


class ServiceBase(object):
    def __init__(self, api_host, customer_id, secret_key, ssl=True, proxy_host=None, timeout=None):
        self._customer_id = customer_id
        self._secret_key = secret_key
        self._api_host = api_host

        http_root = "https" if ssl else "http"
        self._proxy = {"{}".format(http_root): "{}://{}".format(http_root, proxy_host)} if proxy_host else None
        self._url = "{}://{}".format(http_root, api_host)
        self._timeout = timeout

        self._user_agent = "{} TeleSignSDK/python-{}".format(requests.utils.default_headers()['User-Agent'], __version__)


    def _validate_response(self, response):
        resp_obj = json.loads(response.text)
        if response.status_code != requests.codes.ok:
            if response.status_code == requests.codes.unauthorized:
                raise AuthorizationError(resp_obj, response)
            else:
                raise TelesignError(resp_obj, response)

        return resp_obj


class PhoneId(ServiceBase):
    """
    The **PhoneId** class exposes three services that each provide detailed information about a specified phone number.

    .. list-table::
       :widths: 5 30
       :header-rows: 1

       * - Attributes
         -
       * - `customer_id`
         - A string value that identifies your TeleSign account.
       * - `secret_key`
         - A base64-encoded string value that validates your access to the TeleSign web services.
       * - `ssl`
         - (optional) Specifies whether to use a secure connection with the TeleSign server. Defaults to *True*.
       * - `api_host`
         - (optional) The Internet host used in the base URI for REST web services. The default is *rest.telesign.com* (and the base URI is https://rest.telesign.com/).
       * - `proxy_host`
         - (optional) The host and port when going through a proxy server. ex: "localhost:8080. The default to no proxy.
       * - `timeout`
         - (optional) A timeout value to use in requests - float or tuple (see requests documentation for details).  Defaults to None.

    .. note::
       You can obtain both your Customer ID and Secret Key from the `TeleSign Customer Portal <https://portal.telesign.com/account_profile_api_auth.php>`_.

    .. rubric:: Methods

    .. autosummary::
       :nosignatures:

       standard
       score
       contact
       sim_swap
    """

    def __init__(self, customer_id, secret_key, ssl=True, api_host="rest.telesign.com", proxy_host=None, timeout=None):
        super(PhoneId, self).__init__(api_host, customer_id, secret_key, ssl, proxy_host, timeout)

    def standard(self,
                 phone_number,
                 use_case_code=None,
                 extra=None,
                 timeout=None):
        """
        Retrieves the standard set of details about the specified phone number. This includes the type of phone (e.g., land line or mobile), and it's approximate geographic location.

        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number you want details about. You must specify the phone number in its entirety. That is, it must begin with the country code, followed by the area code, and then by the local number. For example, you would specify the phone number (310) 555-1212 as 13105551212.
           * - `use_case_code`
             - (optional, recommended) A four letter code (use case code) used to specify a particular usage scenario for the web service.
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        .. rubric:: Use-case Codes

        The following table list the available use-case codes, and includes a description of each.

        ========  =====================================
        Code      Description
        ========  =====================================
        **BACS**  Prevent bulk account creation + spam.
        **BACF**  Prevent bulk account creation + fraud.
        **CHBK**  Prevent chargebacks.
        **ATCK**  Prevent account takeover/compromise.
        **LEAD**  Prevent false lead entry.
        **RESV**  Prevent fake/missed reservations.
        **PWRT**  Password reset.
        **THEF**  Prevent identity theft.
        **TELF**  Prevent telecom fraud.
        **RXPF**  Prevent prescription fraud.
        **OTHR**  Other.
        **UNKN**  Unknown/prefer not to say.
        ========  =====================================

        **Example**::

            from telesign.api import PhoneId
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"

            phoneid = PhoneId(cust_id, secret_key) # Instantiate a PhoneId object.

            try:
                phone_info = phoneid.standard(phone_number, use_case_code="ATCK")

            except AuthorizationError as ex:
                # API authorization failed. Check the API response for details.
                ...

            except TelesignError as ex:
                # Failed to completely execute the PhoneID service. Check the API response
                # for details. Data returned might be incomplete or invalid.
                ...

        """

        resource = "/v1/phoneid/standard/%s" % phone_number
        method = "GET"

        fields = {}

        if use_case_code:
            fields["ucid"] = use_case_code

        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method)

        headers['User-Agent'] = self._user_agent

        req = requests.get(url="{}{}".format(self._url, resource),
                           params=fields,
                           headers=headers,
                           proxies=self._proxy,
                           timeout=timeout or self._timeout)  # use timeout passed in or session timeout in that order

        return Response(self._validate_response(req), req)

    def score(self,
              phone_number,
              use_case_code,
              extra=None,
              timeout=None):
        """
        Retrieves a score for the specified phone number. This ranks the phone number's "risk level" on a scale from 0 to 1000, so you can code your web application to handle particular use cases (e.g., to stop things like chargebacks, identity theft, fraud, and spam).

        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number you want details about. You must specify the phone number in its entirety. That is, it must begin with the country code, followed by the area code, and then by the local number. For example, you would specify the phone number (310) 555-1212 as 13105551212.
           * - `use_case_code`
             - A four letter code used to specify a particular usage scenario for the web service.
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        .. rubric:: Use-case Codes

        The following table list the available use-case codes (use_case_code), and includes a description of each.

        ========  =====================================
        Code      Description
        ========  =====================================
        **BACS**  Prevent bulk account creation + spam.
        **BACF**  Prevent bulk account creation + fraud.
        **CHBK**  Prevent chargebacks.
        **ATCK**  Prevent account takeover/compromise.
        **LEAD**  Prevent false lead entry.
        **RESV**  Prevent fake/missed reservations.
        **PWRT**  Password reset.
        **THEF**  Prevent identity theft.
        **TELF**  Prevent telecom fraud.
        **RXPF**  Prevent prescription fraud.
        **OTHR**  Other.
        **UNKN**  Unknown/prefer not to say.
        ========  =====================================

        **Example**::

            from telesign.api import PhoneId
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"
            use_case_code = "ATCK"

            phoneid = PhoneId(cust_id, secret_key) # Instantiate a PhoneId object.

            try:
                score_info = phoneid.score(phone_number, use_case_code)
            except AuthorizationError as ex:
                ...
            except TelesignError as ex:
                ...

        """
        resource = "/v1/phoneid/score/%s" % phone_number
        method = "GET"

        fields = {
            "ucid": use_case_code,
        }

        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method)

        headers['User-Agent'] = self._user_agent

        req = requests.get(url="{}{}".format(self._url, resource),
                           params=fields,
                           headers=headers,
                           proxies=self._proxy,
                           timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req)

    def contact(self,
                phone_number,
                use_case_code,
                extra=None,
                timeout=None):
        """
        In addition to the information retrieved by **standard**, this service provides the Name & Address associated with the specified phone number.

        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number you want details about. You must specify the phone number in its entirety. That is, it must begin with the country code, followed by the area code, and then by the local number. For example, you would specify the phone number (310) 555-1212 as 13105551212.
           * - `use_case_code`
             - A four letter use case code used to specify a particular usage scenario for the web service.
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        .. rubric:: Use-case Codes

        The following table list the available use-case codes (use_case_code), and includes a description of each.

        ========  =====================================
        Code      Description
        ========  =====================================
        **BACS**  Prevent bulk account creation + spam.
        **BACF**  Prevent bulk account creation + fraud.
        **CHBK**  Prevent chargebacks.
        **ATCK**  Prevent account takeover/compromise.
        **LEAD**  Prevent false lead entry.
        **RESV**  Prevent fake/missed reservations.
        **PWRT**  Password reset.
        **THEF**  Prevent identity theft.
        **TELF**  Prevent telecom fraud.
        **RXPF**  Prevent prescription fraud.
        **OTHR**  Other.
        **UNKN**  Unknown/prefer not to say.
        ========  =====================================

        **Example**::

            from telesign.api import PhoneId
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"
            use_case_code = "LEAD"

            phoneid = PhoneId(cust_id, secret_key) # Instantiate a PhoneId object.

            try:
                phone_info = phoneid.contact(phone_number, use_case_code)
            except AuthorizationError as ex:
                # API authorization failed, the API response should tell you the reason
                ...
            except TelesignError as ex:
                # failed to completely execute the PhoneID service, check the API response
                #    for details; data returned may be incomplete or not be valid
                ...

        """
        resource = "/v1/phoneid/contact/%s" % phone_number
        method = "GET"

        fields = {
            "ucid": use_case_code,
        }

        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method)

        headers['User-Agent'] = self._user_agent

        req = requests.get(url="{}{}".format(self._url, resource),
                           params=fields,
                           headers=headers,
                           proxies=self._proxy,
                           timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req)

    def live(self,
             phone_number,
             use_case_code,
             extra=None,
             timeout=None):
        """
        In addition to the information retrieved by **standard**, this service provides actionable data associated with the specified phone number.

        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number you want details about. You must specify the phone number in its entirety. That is, it must begin with the country code, followed by the area code, and then by the local number. For example, you would specify the phone number (310) 555-1212 as 13105551212.
           * - `use_case_code`
             - A four letter use case code used to specify a particular usage scenario for the web service.
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        .. rubric:: Use-case Codes

        The following table list the available use-case codes, and includes a description of each.

        ========  =====================================
        Code      Description
        ========  =====================================
        **BACS**  Prevent bulk account creation + spam.
        **BACF**  Prevent bulk account creation + fraud.
        **CHBK**  Prevent chargebacks.
        **ATCK**  Prevent account takeover/compromise.
        **LEAD**  Prevent false lead entry.
        **RESV**  Prevent fake/missed reservations.
        **PWRT**  Password reset.
        **THEF**  Prevent identity theft.
        **TELF**  Prevent telecom fraud.
        **RXPF**  Prevent prescription fraud.
        **OTHR**  Other.
        **UNKN**  Unknown/prefer not to say.
        ========  =====================================

        **Example**::

            from telesign.api import PhoneId
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"
            use_case_code = "RXPF"

            phoneid = PhoneId(cust_id, secret_key) # Instantiate a PhoneId object.

            try:
                phone_info = phoneid.live(phone_number, use_case_code)
            except AuthorizationError as ex:
                # API authorization failed, the API response should tell you the reason
                ...
            except TelesignError as ex:
                # failed to completely execute the PhoneID service, check the API response
                #    for details; data returned may be incomplete or not be valid
                ...

        """
        resource = "/v1/phoneid/live/%s" % phone_number
        method = "GET"

        fields = {
            "ucid": use_case_code,
        }

        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method)

        headers['User-Agent'] = self._user_agent

        req = requests.get(url="{}{}".format(self._url, resource),
                           params=fields,
                           headers=headers,
                           proxies=self._proxy,
                           timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req)

    def sim_swap(self,
                 phone_number,
                 use_case_code,
                 extra=None,
                 timeout=None):
        """
        In addition to the information retrieved by **standard**, this service provides data about potential sim_swaps associated with the specified phone number.  
        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number you want details about. You must specify the phone number in its entirety. That is, it must begin with the country code, followed by the area code, and then by the local number. For example, you would specify the phone number (310) 555-1212 as 13105551212.
           * - `use_case_code`
             - A four letter use case code used to specify a particular usage scenario for the web service.
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        .. rubric:: Use-case Codes

        The following table list the available use-case codes, and includes a description of each.

        ========  =====================================
        Code      Description
        ========  =====================================
        **BACS**  Prevent bulk account creation + spam.
        **BACF**  Prevent bulk account creation + fraud.
        **CHBK**  Prevent chargebacks.
        **ATCK**  Prevent account takeover/compromise.
        **LEAD**  Prevent false lead entry.
        **RESV**  Prevent fake/missed reservations.
        **PWRT**  Password reset.
        **THEF**  Prevent identity theft.
        **TELF**  Prevent telecom fraud.
        **RXPF**  Prevent prescription fraud.
        **OTHR**  Other.
        **UNKN**  Unknown/prefer not to say.
        ========  =====================================

        **Example**::

            from telesign.api import PhoneId
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"
            use_case_code = "RXPF"

            phoneid = PhoneId(cust_id, secret_key) # Instantiate a PhoneId object.

            try:
                phone_info = phoneid.sim_swap(phone_number, use_case_code)
            except AuthorizationError as ex:
                # API authorization failed, the API response should tell you the reason
                ...
            except TelesignError as ex:
                # failed to completely execute the PhoneID service, check the API response
                #    for details; data returned may be incomplete or not be valid
                ...

        """

        resource = "/v1/phoneid/sim_swap/check/%s" % phone_number

        method = "GET"

        fields = {
            "ucid": use_case_code,
        }

        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method)

        headers['User-Agent'] = self._user_agent

        req = requests.get(url="{}{}".format(self._url, resource),
                           params=fields,
                           headers=headers,
                           proxies=self._proxy,
                           timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req)

    def call_forward(self,
                     phone_number,
                     use_case_code,
                     extra=None,
                     timeout=None):
        """
        In addition to the information retrieved by **standard**, this service provides information on call forwarding for the phone number provided.
       .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number you want details about. You must specify the phone number in its entirety. That is, it must begin with the country code, followed by the area code, and then by the local number. For example, you would specify the phone number (310) 555-1212 as 13105551212.
           * - `use_case_code`
             - A four letter use case code used to specify a particular usage scenario for the web service.
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        .. rubric:: Use-case Codes

        The following table list the available use-case codes, and includes a description of each.

        ========  =====================================
        Code      Description
        ========  =====================================
        **BACS**  Prevent bulk account creation + spam.
        **BACF**  Prevent bulk account creation + fraud.
        **CHBK**  Prevent chargebacks.
        **ATCK**  Prevent account takeover/compromise.
        **LEAD**  Prevent false lead entry.
        **RESV**  Prevent fake/missed reservations.
        **PWRT**  Password reset.
        **THEF**  Prevent identity theft.
        **TELF**  Prevent telecom fraud.
        **RXPF**  Prevent prescription fraud.
        **OTHR**  Other.
        **UNKN**  Unknown/prefer not to say.
        ========  =====================================

        **Example**::

            from telesign.api import PhoneId
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"
            use_case_code = "RXPF"

            phoneid = PhoneId(cust_id, secret_key) # Instantiate a PhoneId object.

            try:
                phone_info = phoneid.call_forward(phone_number, use_case_code)
            except AuthorizationError as ex:
                # API authorization failed, the API response should tell you the reason
                ...
            except TelesignError as ex:
                # failed to completely execute the PhoneID service, check the API response
                #    for details; data returned may be incomplete or not be valid
                ...

        """
        resource = "/v1/phoneid/call_forward/%s" % phone_number
        method = "GET"

        fields = {
            "ucid": use_case_code,
        }

        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method)

        headers['User-Agent'] = self._user_agent

        req = requests.get(url="{}{}".format(self._url, resource),
                           params=fields,
                           headers=headers,
                           proxies=self._proxy,
                           timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req)

class Verify(ServiceBase):
    """
    The **Verify** class exposes several services for sending users a verification token. You can use this mechanism to simply test whether you can reach users at the phone number they supplied, or you can have them use the token to authenticate themselves with your web application.

    This class also exposes a service that is used in conjunction with the first two services, in that it allows you to confirm the result of the authentication.

    You can use this verification factor in combination with username & password to provide two-factor authentication for higher security.

    .. list-table::
       :widths: 5 30
       :header-rows: 1

       * - Attributes
         -
       * - `customer_id`
         - A string value that identifies your TeleSign account.
       * - `secret_key`
         - A base64-encoded string value that validates your access to the TeleSign web services.
       * - `ssl`
         - (optional) Specifies whether to use a secure connection with the TeleSign server. Defaults to *True*.
       * - `api_host`
         - (optional) The Internet host used in the base URI for REST web services. The default is *rest.telesign.com* (and the base URI is https://rest.telesign.com/).
       * - `proxy_host`
         - (optional) The host and port when going through a proxy server. ex: "localhost:8080. The default to no proxy.
       * - `timeout`
         - (optional) A timeout value to use in requests - float or tuple (see requests documentation for details).  Defaults to None.

    .. note::
       You can obtain both your Customer ID and Secret Key from the `TeleSign Customer Portal <https://portal.telesign.com/account_profile_api_auth.php>`_.

    """

    def __init__(self, customer_id, secret_key, ssl=True, api_host="rest.telesign.com", proxy_host=None, timeout=None):
        super(Verify, self).__init__(api_host, customer_id, secret_key, ssl, proxy_host, timeout)

    def sms(self,
            phone_number,
            verify_code=None,
            language="en",
            template="",
            use_case_code=None,
            originating_ip=None,
            extra=None,
            timeout=None):
        """
        Sends a text message containing the verification code, to the specified phone number (supported for mobile phones only).

        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number to receive the text message. You must specify the phone number in its entirety. That is, it must begin with the country code, followed by the area code, and then by the local number. For example, you would specify the phone number (310) 555-1212 as 13105551212.
           * - `verify_code`
             - (optional) The verification code to send to the user. If omitted, TeleSign will automatically generate a random value for you.
           * - `language`
             - (optional) The written language used in the message. The default is English.
           * - `template`
             - (optional) A standard form for the text message. It must contain the token ``$$CODE$$``, which TeleSign auto-populates with the verification code.
           * - `use_case_code`
             - (optional, recommended) A four letter code (use case code) used to specify a particular usage scenario for the web service.
           * - `originating_ip`
             - (optional) An IP (v4 or v6) address, possibly detected by the customer's website, that is considered related to the user verification request
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        .. rubric:: Use-case Codes

        The following table list the available use-case codes, and includes a description of each.

        ========  =====================================
        Code      Description
        ========  =====================================
        **BACS**  Prevent bulk account creation + spam.
        **BACF**  Prevent bulk account creation + fraud.
        **CHBK**  Prevent chargebacks.
        **ATCK**  Prevent account takeover/compromise.
        **LEAD**  Prevent false lead entry.
        **RESV**  Prevent fake/missed reservations.
        **PWRT**  Password reset.
        **THEF**  Prevent identity theft.
        **TELF**  Prevent telecom fraud.
        **RXPF**  Prevent prescription fraud.
        **OTHR**  Other.
        **UNKN**  Unknown/prefer not to say.
        ========  =====================================

        **Example**::

            from telesign.api import Verify
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"

            verify = Verify(cust_id, secret_key) # Instantiate a Verify object.

            try:
                phone_info = verify.sms(phone_number, use_case_code="ATCK")
            except AuthorizationError as ex:
                # API authorization failed, the API response should tell you the reason
                ...
            except TelesignError as ex:
                # failed to execute the Verify service, check the API response for details
                ...

            # When the user inputs the validation code, you can verify that it matches the one that you sent.
            if (phone_info != None):
                try:
                    status_info = verify.status(phone_info.data["reference_id"], verify_code=phone_info.verify_code)
                except AuthorizationError as ex:
                    ...
                except TelesignError as ex:
                    ...

        """

        resource = "/v1/verify/sms"
        method = "POST"

        fields = {
            "phone_number": phone_number,
            "language": language,
            "template": template,
        }

        if verify_code:
            fields['verify_code'] = verify_code

        if use_case_code:
            fields['ucid'] = use_case_code

        if originating_ip is not None:
            fields['originating_ip'] = originating_ip

        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method,
            fields=fields)

        headers['User-Agent'] = self._user_agent

        req = requests.post(url="{}{}".format(self._url, resource),
                            data=fields,
                            headers=headers,
                            proxies=self._proxy,
                            timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req, verify_code=verify_code)

    def call(self,
             phone_number,
             verify_code=None,
             use_case_code=None,
             verify_method="",
             language="en",
             extension_type="",
             redial="",
             originating_ip=None,
             pressx=None,
             extra=None,
             timeout=None):
        """
        Calls the specified phone number, and using speech synthesis, speaks the verification code to the user.

        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number to receive the text message. You must specify the phone number in its entirety. That is, it must begin with the country code, followed by the area code, and then by the local number. For example, you would specify the phone number (310) 555-1212 as 13105551212.
           * - `verify_code`
             - (optional) The verification code to send to the user. If omitted, TeleSign will automatically generate a random value for you.
           * - `language`
             - (optional) The written language used in the message. The default is English.
           * - `verify_method`
             - (optional)
           * - `extension_type`
             - (optional)
           * - `redial`
             - (optional)
           * - `use_case_code`
             - (optional, recommended) A four letter code (use case code) used to specify a particular usage scenario for the web service.
           * - `originating_ip`
             - (optional) An IP (v4 or v6) address, possibly detected by the customer's website, that is considered related to the user verification request
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation). Will override any timeout set in the initialization.

        .. rubric:: Use-case Codes

        The following table list the available use-case codes, and includes a description of each.

        ========  =====================================
        Code      Description
        ========  =====================================
        **BACS**  Prevent bulk account creation + spam.
        **BACF**  Prevent bulk account creation + fraud.
        **CHBK**  Prevent chargebacks.
        **ATCK**  Prevent account takeover/compromise.
        **LEAD**  Prevent false lead entry.
        **RESV**  Prevent fake/missed reservations.
        **PWRT**  Password reset.
        **THEF**  Prevent identity theft.
        **TELF**  Prevent telecom fraud.
        **RXPF**  Prevent prescription fraud.
        **OTHR**  Other.
        **UNKN**  Unknown/prefer not to say.
        ========  =====================================

        **Example**::

            from telesign.api import Verify
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

            verify = Verify(cust_id, secret_key) # Instantiate a Verify object.

            phone_number = "13107409700"

            try:
                phone_info = verify.call(phone_number, use_case_code="ATCK")
            except AuthorizationError as ex:
                # API authorization failed, the API response should tell you the reason
                ...
            except TelesignError as ex:
                # failed to execute the Verify service, check the API response for details
                ...

            # When the user inputs the validation code, you can verify that it matches the one that you sent.
            if (phone_info != None):
                try:
                    status_info = verify.status(phone_info.data["reference_id"], verify_code=phone_info.verify_code)
                except AuthorizationError as ex:
                    ...
                except TelesignError as ex:
                    ...
        """

        resource = "/v1/verify/call"
        method = "POST"

        fields = {
            "phone_number": phone_number,
            "language": language,
            "verify_method": verify_method,
            "extension_type": extension_type,
            "redial": redial,
        }

        if verify_code:
            fields['verify_code'] = verify_code

        if pressx:
            fields['pressx'] = pressx

        if use_case_code:
            fields['ucid'] = use_case_code

        if originating_ip is not None:
            fields['originating_ip'] = originating_ip

        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method,
            fields=fields)

        headers['User-Agent'] = self._user_agent

        req = requests.post(url="{}{}".format(self._url, resource),
                            data=fields,
                            headers=headers,
                            proxies=self._proxy,
                            timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req, verify_code=verify_code)


    def smart(self,
              phone_number,
              use_case_code,
              verify_code=None,
              language="en",
              preference=None,
              ignore_risk=False,
              extra=None,
              timeout=None):
        """
        Calls the specified phone number, and using speech synthesis, speaks the verification code to the user.

        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number to receive the text message. You must specify the phone number in its entirety. That is, it must begin with the country code, followed by the area code, and then by the local number. For example, you would specify the phone number (310) 555-1212 as 13105551212.
           * - `verify_code`
             - (optional) The verification code to send to the user. If omitted, TeleSign will automatically generate a random value for you.
           * - `language`
             - (optional) The written language used in the message. The default is English.
           * - `use_case_code`
             - A four letter code (use case code) used to specify a particular usage scenario for the web service.
           * - `preference`
             - (optional) Customer preference for delivery method.   One of 'call', 'sms', 'push'.  This may override TeleSign's determination of the method to use when possible (for instance, it is not possible to send an sms to all phones).
           * - `ignore_risk`
             - (optional) If true, TeleSign will ignore the evaluated risk for the phone and attempt delivery in all cases.
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        .. rubric:: Use-case Codes

        The following table list the available use-case codes, and includes a description of each.

        ========  =====================================
        Code      Description
        ========  =====================================
        **BACS**  Prevent bulk account creation + spam.
        **BACF**  Prevent bulk account creation + fraud.
        **CHBK**  Prevent chargebacks.
        **ATCK**  Prevent account takeover/compromise.
        **LEAD**  Prevent false lead entry.
        **RESV**  Prevent fake/missed reservations.
        **PWRT**  Password reset.
        **THEF**  Prevent identity theft.
        **TELF**  Prevent telecom fraud.
        **RXPF**  Prevent prescription fraud.
        **OTHR**  Other.
        **UNKN**  Unknown/prefer not to say.
        ========  =====================================

        **Example**::

            from telesign.api import Verify
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

            verify = Verify(cust_id, secret_key) # Instantiate a Verify object.

            phone_number = "13107409700"

            try:
                phone_info = verify.call(phone_number, use_case_code="ATCK")
            except AuthorizationError as ex:
                # API authorization failed, the API response should tell you the reason
                ...
            except TelesignError as ex:
                # failed to execute the Verify service, check the API response for details
                ...

            # When the user inputs the validation code, you can verify that it matches the one that you sent.
            if (phone_info != None):
                try:
                    status_info = verify.status(phone_info.data["reference_id"], verify_code=phone_info.verify_code)
                except AuthorizationError as ex:
                    ...
                except TelesignError as ex:
                    ...
        """

        resource = "/v1/verify/smart"
        method = "POST"

        fields = {
            "phone_number": phone_number,
            "language": language,
            'ucid': use_case_code,
        }

        if preference:
            fields['preference'] = preference

        if ignore_risk:
            fields['ignore_risk'] = ignore_risk

        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method,
            fields=fields)

        headers['User-Agent'] = self._user_agent

        req = requests.post(url="{}{}".format(self._url, resource),
                            data=fields,
                            headers=headers,
                            timeout=timeout or self._timeout,
                            proxies=self._proxy)

        return Response(self._validate_response(req), req, verify_code=verify_code)


    def push(self,
             phone_number,
             use_case_code,
             extra={},
             timeout=None,):
        """
        The **push** method sends a push notification containing the verification code to the specified phone number (supported for mobile phones only).

        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number to receive the text message. You must specify the phone number in its entirety. That is, it must begin with the country code, followed by the area code, and then by the local number. For example, you would specify the phone number (310) 555-1212 as 13105551212.
           * - `use_case_code`
             - A four letter code (use case code) used to specify a particular usage scenario for the web service.
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

         .. rubric:: Use-case Codes

        The following table list the available use-case codes, and includes a description of each.

        ========  =====================================
        Code      Description
        ========  =====================================
        **BACS**  Prevent bulk account creation + spam.
        **BACF**  Prevent bulk account creation + fraud.
        **CHBK**  Prevent chargebacks.
        **ATCK**  Prevent account takeover/compromise.
        **LEAD**  Prevent false lead entry.
        **RESV**  Prevent fake/missed reservations.
        **PWRT**  Password reset.
        **THEF**  Prevent identity theft.
        **TELF**  Prevent telecom fraud.
        **RXPF**  Prevent prescription fraud.
        **OTHR**  Other.
        **UNKN**  Unknown/prefer not to say.
        ========  =====================================

        **Example**::

            from telesign.api import Verify
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

            verify = Verify(cust_id, secret_key) # Instantiate a Verify object.

            phone_number = "13107409700"

            try:
                phone_info = verify.push(phone_number, "ATCK")
            except AuthorizationError as ex:
                # API authorization failed, the API response should tell you the reason
                ...
            except TelesignError as ex:
                # failed to execute the Verify service, check the API response for details
                ...

            # When the user inputs the validation code, you can verify that it matches the one that you sent.
            if (phone_info != None):
                try:
                    status_info = verify.status(phone_info.data["reference_id"], verify_code=phone_info.verify_code)
                except AuthorizationError as ex:
                    ...
                except TelesignError as ex:
                    ...

        """

        resource = "/v2/verify/push"
        method = "POST"

        fields = {
            "phone_number": phone_number,
            "ucid": use_case_code
        }

        fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method,
            fields=fields)

        headers['User-Agent'] = self._user_agent

        req = requests.post(url="{}{}".format(self._url, resource),
                            headers=headers,
                            data=fields,
                            timeout=timeout or self._timeout,
                            proxies=self._proxy)

        return Response(self._validate_response(req), req)


    def status(self,
               ref_id,
               resource_uri=None,
               verify_code=None,
               extra=None,
               timeout=None):
        """
           Retrieves the verification result. You make this call in your web application after users complete the authentication transaction (using either a call or sms).

        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `ref_id`
             - The Reference ID returned in the response from the TeleSign server, after you called either **call** or **sms**.
           * - `verify_code`
             - (optional) The verification code received from the user.
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        **Example**::

            from telesign.api import Verify
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"

            verify = Verify(cust_id, secret_key) # Instantiate a Verify object.

            phone_info = verify.sms(phone_number) # Send a text message that contains an auto-generated validation code, to the user.

            # When the user inputs the validation code, you can verify that it matches the one that you sent.
            if (phone_info != None):
                try:
                    status_info = verify.status(phone_info.data["reference_id"], verify_code=phone_info.verify_code)
                except AuthorizationError as ex:
                    ...
                except TelesignError as ex:
                    ...

        """

        if resource_uri:
            resource = resource_uri
        else:
            resource = "/v1/verify/%s" % ref_id

        method = "GET"

        fields = {}

        if verify_code is not None:
            fields["verify_code"] = verify_code

        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method)

        headers['User-Agent'] = self._user_agent

        req = requests.get(url="{}{}".format(self._url, resource),
                           params=fields,
                           headers=headers,
                           proxies=self._proxy,
                           timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req)

    def soft_token(self,
                   bundle_id,
                   phone_number,
                   soft_token_id,
                   verify_code,
                   session_id=None,
                   extra=None,
                   timeout=None):
        """
        The TeleSign Mobile Device Soft Token Notification web service allows you to anticipate when your users need to use their soft token to generate a time-sensitive one-time passcode. You can use this web service to preemptively send them a push notification that initializes their on-device TeleSign AuthID application with the right soft token. When they open the notification, the soft token launches ready for them to use.

         .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number for the Mobile Device Soft Token Notification request, including country code. For example, phone_number=13105551212
           * - `soft_token_id`
             - The alphanumeric string that uniquely identifies your TeleSign soft token subscription.
           * - `bundle_id`
             - Unique identifier for the mobile app.
           * - `verify_code`
             - The verification code to send to the user. 
           * - `session_id`
             - [Optional] A free form string (up to 64 ASCII characters) that indicates an ID (either raw or hashed) that is unique to the user's session with the customer. The session_id links multiple calls and other TeleSign services that are associated with the current session.
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        **Example**::

            from telesign.api import Verify
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"

            verify = Verify(cust_id, secret_key) # Instantiate a Verify object.
            bundle_id = 'abcde12345'
            soft_token_id = '12345abc'
            verify_code = '12345'
            phone_info = verify.soft_token(bundle_id, phone_number, soft_token_id, verify_code) 

            if (phone_info != None):
                try:
                    status_info = verify.status(phone_info.data["reference_id"], verify_code=phone_info.verify_code)
                except AuthorizationError as ex:
                    ...
                except TelesignError as ex:
                    ...
        """
        resource = "/v2/verify/soft_token"
        method = "POST"

        fields = {
                    'bundle_id': bundle_id,
                    'phone_number': phone_number,
                    'soft_token_id': soft_token_id,
                    'verify_code': verify_code
                }

        if session_id:
            fields['session_id'] = session_id

        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method,
            fields=fields)

        req = requests.post(url="{}{}".format(self._url, resource),
                            headers=headers,
                            data=fields,
                            proxies=self._proxy,
                            timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req, verify_code=verify_code)

    def registration_status(self,
                            phone_number,
                            bundle_id,
                            extra=None,
                            timeout=None):
        """
        The TeleSign Mobile Device Registration Status web service allows you to query the current state of the
        Push Verify application registration.

         .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number for the Push Verify registration, including country code. For example, phone_number=13105551212
           * - `bundle_id`
             - Unique identifier for the mobile app.
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        **Example**::

            from telesign.api import Verify
            from telesign.exceptions import AuthorizationError, TelesignError

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"

            verify = Verify(cust_id, secret_key) # Instantiate a Verify object.
            bundle_id = 'com.example.authid'
            status = verify.registration_status(bundle_id, phone_number) 

            if (status != None):
                device_info = status['device']
                app_info = status['app']
                status_info = status['status']
        """

        resource = "/v2/verify/registration/{}".format(phone_number)
        method = "GET"

        fields = {
                    'bundle_id' : bundle_id,
                 }

        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method)
        
        headers['User-Agent'] = self._user_agent

        req = requests.get(url="{}{}".format(self._url, resource),
                           headers=headers,
                           params=fields,
                           proxies=self._proxy,
                           timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req)



class Telebureau(ServiceBase):
    """
    The **Telebureau** class exposes services for creating, retrieving, updating and deleting telebureau fraud events. You can use this mechanism to simply test whether you can reach teleburea services.

    .. list-table::
       :widths: 5 30
       :header-rows: 1

       * - Attributes
         -
       * - `customer_id`
         - A string value that identifies your TeleSign account.
       * - `secret_key`
         - A base64-encoded string value that validates your access to the TeleSign web services.
       * - `ssl`
         - Specifies whether to use a secure connection with the TeleSign server. Defaults to *True*.
       * - `api_host`
         - The Internet host used in the base URI for REST web services. The default is *rest.telesign.com* (and the base URI is https://rest.telesign.com/).
       * - `proxy_host`
         - (optional) The host and port when going through a proxy server. ex: "localhost:8080. The default to no proxy.
       * - `timeout`
         - (optional) A timeout value to use in requests - float or tuple (see requests documentation for details).  Defaults to None.

    .. note::
       You can obtain both your Customer ID and Secret Key from the `TeleSign Customer Portal <https://portal.telesign.com/account_profile_api_auth.php>`_.

    """

    def __init__(self, customer_id, secret_key, ssl=True, api_host="rest.telesign.com", proxy_host=None, timeout=None):
        super(Telebureau, self).__init__(api_host, customer_id, secret_key, ssl, proxy_host, timeout)

    def create(self,
               phone_number,
               fraud_type,
               occurred_at,
               verified_by=None,
               verified_at=None,
               discovered_at=None,
               fraud_ip=None,
               impact_type=None,
               impact=None,
               extra=None,
               timeout=None):
        """
        Creates a telebureau event corresponding to supplied data.

        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `phone_number`
             - The phone number you want to submit, composed of a string of digits without spaces or punctuation, beginning with the country dialing code (for example, "1" for North America). You would specify the phone number (310) 555-1212 as 13105551212.
           * - `fraud_type`
             - The type of fraud committed.
           * - `occurred_at`
             -  A string value specifying when the fraud event occurred. The value must be in RFC 3339 time format (for example, yyyy-mm-ddThh:mm:ssZ).

           * - `discovered_at` (optional)
             - A string value specifying when you discovered the fraud event. The value must be in RFC 3339 time format (for example, yyyy-mm-ddThh:mm:ssZ).
           * - `fraud_ip` (optional)
             - If you managed to capture the user's IP address, then specify it here.
           * - `impact_type` (optional)
             - A string enumeration value indicating the area of your business that was affected by this fraud event.
           * - `impact` (optional)
             - A string enumeration value indicating how severely your business was affected by this fraud event.
           * - `verified_by` (optional)
             - A string enumeration value identifying the method used to verify the submitted phone number.
           * - `verified_at` (optional)
             - If you verified the user's phone number, then you use this parameter to specify when. The value must be in RFC 3339 time format (for example, yyyy-mm-ddThh:mm:ssZ).
           * - `extra`
             - (optional) dict - any extra optional params
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        .. rubric:: Fraud Type Codes

        The following lists the available fraud-type values.

        =================================
        Fraud Type
        =================================
        chargeback
        coupon
        harass
        identity_theft
        other
        property_damage
        spam
        takeover
        telco
        =====================================

        .. rubric:: Impact Type Codes

        The following lists the available impact-type values.

        =====================================
        Impact Type
        =====================================
        revenue_loss
        operational_overhead
        customer_experience
        other
        =====================================

        .. rubric:: Impact Codes

        The following lists the available impact values.

        ====================================
        Impact
        ====================================
        low
        medium
        high
        ====================================

        .. rubric:: Verified By

        The following lists the available impact values.

        ====================================
        Impact
        ====================================
        telesign
        other
        ====================================


        **Example**::

            from telesign.api import Telebureau, to_utc_rfc3339
            from telesign.exceptions import AuthorizationError, TelesignError
            from datetime import datetime

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"

            telebureau = Telebureau(cust_id, secret_key) # Instantiate a telebureau object.

            try:
                event = telebureau.create(phone_number, "spam", to_utc_rfc3339(datetime.utcnow()))
            except AuthorizationError as ex:
                # API authorization failed, the API response should tell you the reason
                ...
            except TelesignError as ex:
                # failed to execute the telebureau service, check the API response for details
                ...

            # Once the event is created, you can verify that the submission was accepted.
            if (event != None):
                try:
                    status = telebureau.retrieve(event.data["reference_id"])
                except AuthorizationError as ex:
                    ...
                except TelesignError as ex:
                    ...

        """
        resource = "/v1/telebureau/event"
        method = "POST"

        fields = {
            "phone_number": phone_number,
            "fraud_type": fraud_type,
            "occurred_at": occurred_at,
        }
        if verified_by:
            fields['verified_by'] = verified_by
        if verified_at:
            fields['verified_at'] = verified_at
        if discovered_at:
            fields['discovered_at'] = discovered_at
        if fraud_ip:
            fields['fraud_ip'] = fraud_ip
        if impact_type:
            fields['impact_type'] = impact_type
        if impact:
            fields['impact'] = impact
        if extra is not None:
            fields.update(extra)

        headers = generate_auth_headers(
            self._customer_id,
            self._secret_key,
            resource,
            method,
            fields=fields)

        req = requests.post(url="{}{}".format(self._url, resource),
                            headers=headers,
                            data=fields,
                            proxies=self._proxy,
                            timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req)

    def retrieve(self,
                 ref_id,
                 extra=None,
                 timeout=None):
        """
        Retrieves the fraud event status. You make this call in your web application after completion of create transaction for a telebureau event.

        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `ref_id`
             - The Reference ID returned in the response from the TeleSign server, after you called **create**.
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        **Example**::

            from telesign.api import Telebureau, to_utc_rfc3339
            from telesign.exceptions import AuthorizationError, TelesignError
            from datetime import datetime

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"

            telebureau = Telebureau(cust_id, secret_key) # Instantiate a telebureau object.

            try:
                event = telebureau.create(phone_number, "spam", to_utc_rfc3339(datetime.utcnow()))
            except AuthorizationError as ex:
                # API authorization failed, the API response should tell you the reason
                ...
            except TelesignError as ex:
                # failed to execute the telebureau service, check the API response for details
                ...

            # When the event is submitted, you can verify that it was accepted.
            if (event != None):
                try:
                    status = telebureau.retrieve(event.data["reference_id"])
                except AuthorizationError as ex:
                    ...
                except TelesignError as ex:
                    ...

        """

        resource = "/v1/telebureau/event/{}".format(ref_id)
        method = "GET"

        headers = generate_auth_headers(self._customer_id,
                                        self._secret_key,
                                        resource,
                                        method)
        fields = {}

        if extra is not None:
            fields.update(extra)

        req = requests.get(url="{}{}".format(self._url, resource),
                           headers=headers,
                           params=fields,
                           proxies=self._proxy,
                           timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req)

    def delete(self,
               ref_id,
               extra=None,
               timeout=None):
        """
        Deletes a previously submitted fraud event. You make this call in your web application after completion of the create transaction for a telebureau event.

        .. list-table::
           :widths: 5 30
           :header-rows: 1

           * - Parameters
             -
           * - `ref_id`
             - The Reference ID returned in the response from the TeleSign server, after you called **create**
           * - `extra`
             - (optional) Key value mapping of additional parameters.
           * - `timeout`
             - (optional) Timeout for the request (see timeout in the requests documentation).   Will override any timeout set in the initialization.

        **Example**::

            from telesign.api import Telebureau, to_utc_rfc3339
            from telesign.exceptions import AuthorizationError, TelesignError
            from datetime import datetime

            cust_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
            secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
            phone_number = "13107409700"

            telebureau = Telebureau(cust_id, secret_key) # Instantiate a telebureau object.

            try:
                event = telebureau.create(phone_number, "spam", to_utc_rfc3339(datetime.utcnow()))
            except AuthorizationError as ex:
                # API authorization failed, the API response should tell you the reason
                ...
            except TelesignError as ex:
                # failed to execute the telebureau service, check the API response for details
                ...

            # If the event is submitted in error, you can submit a delete request.
            if (event != None):
                try:
                    status = telebureau.delete(event.data["reference_id"])
                except AuthorizationError as ex:
                    ...
                except TelesignError as ex:
                    ...

        """

        resource = "/v1/telebureau/event/{}".format(ref_id)
        method = "DELETE"

        headers = generate_auth_headers(self._customer_id,
                                        self._secret_key,
                                        resource,
                                        method)

        fields = {}

        if extra is not None:
            fields.update(extra)

        req = requests.delete(url="{}{}".format(self._url, resource),
                              headers=headers,
                              params=fields,
                              proxies=self._proxy,
                              timeout=timeout or self._timeout)

        return Response(self._validate_response(req), req)
