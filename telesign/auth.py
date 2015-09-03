""" Authorization header definitions """

from __future__ import print_function

from hashlib import sha1, sha256
from base64 import b64encode, b64decode
from email.utils import formatdate
from time import mktime
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
import hmac
import uuid
import datetime


__author__ = "Jeremy Cunningham"
__copyright__ = "Copyright 2015, TeleSign Corp."
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


AUTH_METHOD = {
    'sha1': {"hash": sha1, "name": "HMAC-SHA1"},
    'sha256': {"hash": sha256, "name": "HMAC-SHA256"}
}


def generate_auth_headers(
        customer_id,
        secret_key,
        resource,
        method,
        content_type="",
        auth_method="sha256",
        fields=None,
        use_nonce=True,
        hashcash=None):
    """
    Function to generate the REST API authentication headers. A signature is
    computed based on the contents of the request and the client's secret key.

    :param customer_id: A string value that identifies the TeleSign account.

    :param secret_key: A base64-encoded string value that validates access to the TeleSign web services.

    :param resource: The REST resource to invoke the request.

    :param method: HTTP verb to perform in the request.

    :param content_type: Content type to apply to the HTTP request headers.

    :param auth_method: Hash function to use to generate the signature.

    :param fields: Include additional fields to include in the signature.

    :param use_nonce: Optionally disable nonce generation to simplify testing.

    :param hashcash: Include a hashcash in the headers.

    :return: headers to be applied to the HTTP request
    """

    now = datetime.datetime.now()
    stamp = mktime(now.timetuple())
    current_date = formatdate(
        timeval=stamp,
        localtime=False,
        usegmt=True)

    if method in ("POST", "PUT"):
        content_type = "application/x-www-form-urlencoded"

    if auth_method not in AUTH_METHOD:
        auth_method = "sha256"

    # According to the documentation (authorization/canonicalization)
    # this should be method, content type, date, then the x-ts-
    # headers sorted lexicographically.
    # In the string (as constructed here) the date is left blank
    # (hence the double newline), then x-ts-auth-method and x-ts-date
    # are given (in sorted order).  (x-ts-date will override Date if
    # both are given or if no Date is given.)  If x-ts-nonce is
    # supplied below, it is also appended to the string so that the
    # headers remain in sorted order.
    # Finally if the request is a POST the request parameters are
    # url-encoded and added after a newline.  The Content-Type header
    # may also be empty if the request is a GET.

    string_to_sign = "%s\n%s\n\nx-ts-auth-method:%s\nx-ts-date:%s" % (
        method,
        content_type,
        AUTH_METHOD[auth_method]["name"],
        current_date)

    if use_nonce:
        nonce = str(uuid.uuid4())
        string_to_sign += "\nx-ts-nonce:" + nonce

    if method in ("POST", "PUT") and fields:
        string_to_sign += "\n%s" % urlencode(fields)

    string_to_sign += "\n%s" % resource

    signer = hmac.new(b64decode(secret_key), string_to_sign.encode("utf-8"), AUTH_METHOD[auth_method]["hash"])

    signature = b64encode(signer.digest()).decode("utf-8")

    headers = {
        "Authorization": "TSA %s:%s" % (customer_id, signature),
        "x-ts-date": current_date,
        "x-ts-auth-method": AUTH_METHOD[auth_method]["name"],
        "Content-Type": content_type
    }

    if hashcash:
        headers["X-Hashcash"] = hashcash

    if use_nonce:
        headers["x-ts-nonce"] = nonce

    return headers
