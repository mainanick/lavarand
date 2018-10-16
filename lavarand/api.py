from collections import namedtuple

import requests

"""
>>> import lavarand
>>> random = lavarand.random()

"""

API_URL = "https://csprng.xyz/v1/api"

RANDMAX = 65535
RANDMIN = 1


class LavarandException(Exception):
    pass


def random(length=32, with_time=False, form="base64"):

    length = 32 if length < RANDMIN else min([RANDMAX, length])

    try:
        res = requests.get(API_URL, params={"length": length, "format": form}).json()
    except Exception as e:
        raise LavarandException(str(e))

    if with_time:
        return namedtuple("Random", ["val", "time"])(val=res["Data"], time=res["Time"])

    return res["Data"]
