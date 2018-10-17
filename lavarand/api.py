import os
import sys
import warnings
from base64 import b64encode

import requests

"""
>>> import lavarand
>>> random = lavarand.random()

"""

API_URL = "https://csprng.xyz/v1/api"

RANDMAX = 65535
RANDMIN = 1


def random(size=32):

    assert isinstance(size, int)

    size = 32 if size < RANDMIN else min([RANDMAX, size])

    try:
        return requests.get(API_URL, params={"length": size}).json()["Data"]
    except Exception:  # try catch all exceptions
        warnings.warn("Was unable to use lava random fallback to os urandom")
        return b64encode(os.urandom(size)).decode("utf-8")
