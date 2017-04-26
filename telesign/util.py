from __future__ import unicode_literals

from hmac import HMAC
from base64 import b64decode, b64encode
from hashlib import sha256
from random import SystemRandom


def to_utc_rfc3339(a_datetime):
    """
    Helper function to format a timezone unaware/UTC datetime in rfc3339 utc timestamp the easy way.
    """
    return "{date_string}Z".format(date_string=a_datetime.replace(microsecond=0).isoformat())


def random_with_n_digits(n):
    """
    Helper function to generate a random number n digits in length using a system random.
    """
    return "".join(SystemRandom().choice('123456789') for _ in range(n))


def verify_telesign_callback_signature(api_key, signature, json_str):
    """
    Verify that a callback was made by TeleSign and was not sent by a malicious client by verifying the signature.

    :param api_key: the TeleSign API api_key associated with your account.
    :param signature: the TeleSign Authorization header value supplied in the callback, as a string.
    :param json_str: the POST body text, that is, the JSON string sent by TeleSign describing the transaction status.
    """
    your_signature = b64encode(HMAC(b64decode(api_key), json_str.encode("utf-8"), sha256).digest()).decode("utf-8")

    if len(signature) != len(your_signature):
        return False

    # avoid timing attack with constant time equality check
    signatures_equal = True
    for x, y in zip(signature, your_signature):
        if not x == y:
            signatures_equal = False

    return signatures_equal
