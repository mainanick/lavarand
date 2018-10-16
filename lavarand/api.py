import requests


"""
>>> import lavarand
>>> random = lavarand.random()

"""

API_URL = "https://csprng.xyz/v1/api"

class LavarandException(Exception):
  pass

class Random(dict):
  def __init__(self, val):
    super().update(val)
  
  @property
  def val(self):
    return self["value"]
  
  @property
  def time(self):
    return self["time"]

def random(length=32, form="base64", with_time=False):
  try:
    res = requests.get(API_URL, params={"length":length, "format":form}).json()
  except Exception as e:
    raise LavarandException(str(e))
  
  if not with_time:
    return res["Data"]
  
  return Random({"value":res["Data"], "time":res["Time"]})


if __name__ == '__main__':
  print(random().val)