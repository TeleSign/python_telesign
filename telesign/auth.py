""" Authorization header definitions """

from __future__ import print_function 

from hashlib import sha1, sha256
from base64 import b64encode, b64decode
from email.utils import formatdate
from time import mktime
try : 
    from urllib import urlencode 
except :
    from urllib.parse import urlencode 
import hmac
import uuid 
import datetime


__author__ = "Jeremy Cunningham, Michael Fox, and Radu Maierean"
__copyright__ = "Copyright 2012, TeleSign Corp."
__credits__ = ["Jeremy Cunningham", "Radu Maierean", "Michael Fox", "Nancy Vitug", "Humberto Morales"]
__license__ = "MIT"
__maintainer__ = "Jeremy Cunningham"
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
        hashcash=None ):

    now = datetime.datetime.now()
    stamp = mktime(now.timetuple())
    currDate = formatdate(
            timeval=stamp,
            localtime=False,
            usegmt=True
        )

    if(method in ("POST", "PUT")):
        content_type = "application/x-www-form-urlencoded"

    string_to_sign = "%s\n%s\n\nx-ts-auth-method:%s\nx-ts-date:%s" % (
        method,
        content_type, 
        AUTH_METHOD[auth_method]["name"],
        currDate) 

    if auth_method not in AUTH_METHOD :
        # what to do ?
        auth_method = 'sha256'    

    if use_nonce :
        nonce = str(uuid.uuid4()) 
        string_to_sign += "\nx-ts-nonce:" + nonce 

    if(fields):
        string_to_sign = string_to_sign + "\n%s" % urlencode(fields)

    string_to_sign = string_to_sign + "\n%s" % resource
    signer = hmac.new(b64decode(secret_key), string_to_sign.encode('utf-8'), AUTH_METHOD[auth_method]["hash"])

    signature = b64encode(signer.digest()).decode('utf-8') 

    headers = {
        "Authorization": "TSA %s:%s" % (customer_id, signature),
        "x-ts-date": currDate,
        "x-ts-auth-method": AUTH_METHOD[auth_method]["name"],
    }

    if hashcash :
        headers['X-Hashcash'] = hashcash 

    if use_nonce : 
        headers["x-ts-nonce"] = nonce 

    return headers
