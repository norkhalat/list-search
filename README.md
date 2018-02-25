## NAME

**list-search** -- return the index of the number in the list


## DESCRTIPTION

The module [search.py](./search.py) implements a function `index`
which searches for the number in the list of integer numbers.

### Restrictions

Do not use `list.index` method.


## RETURN VALUE

The function returns the index of the number in the list if found,
else `-1`.


## EXAMPLES

```python
import search

l = [1, 4, 6]
print(search.index(4, l))   # -> 1
print(search.index(5, l))   # -> -1
```

Run tests:

```console
% python -m unittest discover -p '*_ut.py' 
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```
