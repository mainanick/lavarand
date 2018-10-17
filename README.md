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

>>> random = lavarand.random(size=50)
>>> print(random)
"F9Pziq9ZxBjntW2OYeADSMnpBDWtRI8txyZwH/JuzMpirs0cFh+eGiu3JGd4PVsDq+8=="

```