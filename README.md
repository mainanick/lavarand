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

```