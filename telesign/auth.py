""" Authorization header definitions """

from hashlib import sha1, sha256
from base64 import b64encode, b64decode
from email.utils import formatdate
from time import mktime
import urllib
import hmac
import random
import datetime


__author__ = "Jeremy Cunningham, Michael Fox, and Radu Maierean"
__copyright__ = "Copyright 2012, TeleSign Corp."
__credits__ = ["Jeremy Cunningham", "Radu Maierean", "Michael Fox", 
                        "Nancy Vitug" ]
__license__ = "MIT"
__maintainer__ = "Jeremy Cunningham"
__email__ = "support@telesign.com"
__status__ = "Production"



AUTH_METHOD = {
    'sha1': {"hash":sha1, "name":"HMAC-SHA1"},
    'sha256': {"hash":sha256, "name":"HMAC-SHA256"}
}

def generate_auth_headers(
        customer_id, 
        secret_key, 
        resource, 
        method, 
        content_type="",
        auth_method="sha1", fields=None):
    

    now = datetime.datetime.now()
    stamp = mktime(now.timetuple())
    currDate = formatdate(
            timeval     = stamp,
            localtime   = False,
            usegmt      = True
        )
    nonce = "%s" % random.random()

    if(method in ("POST","PUT")):
        content_type = "application/x-www-form-urlencoded"

    string_to_sign = "%s\n%s\n\nx-ts-auth-method:%s\nx-ts-date:%s\nx-ts-nonce:%s" % (
        method, 
        content_type,
        AUTH_METHOD[auth_method]["name"],
        currDate, 
        nonce)

    if(fields):
        string_to_sign = string_to_sign + "\n%s" % urllib.urlencode(fields)

    string_to_sign =  string_to_sign + "\n%s" % resource

    signer = hmac.new(b64decode(secret_key), string_to_sign, AUTH_METHOD[auth_method]["hash"])

    signature = b64encode(signer.digest())


    headers = {
        "Authorization" : "TSA %s:%s" % (customer_id, signature),
        "x-ts-date" : currDate,
        "x-ts-auth-method" : AUTH_METHOD[auth_method]["name"],
        "x-ts-nonce" : nonce 
    }

    return headers
