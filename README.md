### [Randomness-101-lavarand-in-production](https://blog.cloudflare.com/randomness-101-lavarand-in-production/)

https://csprng.xyz/

```
pip install lavarand
```

```python
>>> import lavarand
>>> random = lavarand.random()
>>> print(random)
"hp7RWuKfuUHWXvAQTUEtRits0chzZWHDjP58nVmwOZM="

>>> random = lavarand.random(with_time=True)
>>> print(random.time)
"2018-10-14T07:03:39.250Z="
>>> print(random.val)
"hp7RWuKfuUHWXvAQTUEtRits0chzZWHDjP58nVmwOZM"


>>> random = lavarand.random(length=50)
>>> print(random)
"F9Pziq9ZxBjntW2OYeADSMnpBDWtRI8txyZwH/JuzMpirs0cFh+eGiu3JGd4PVsDq+8=="

```