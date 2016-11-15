# que_es
Hilariously simple little helper tool for Python object inspection.

Gets and prints object attributes, methods, docstring, and type with one command. Easy to read format.

`pip install que_es`

Usage:

```python

>>> import que_es
>>> que_es.esto([1,2,3])
>>> que_es.esto([1,2,3])
~~~~
VARS
~~~~
Object has no __dict__ attributes
 
~~~
DIR
~~~
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
 
~~~~~~~~~
DOCSTRING
~~~~~~~~~
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
 
~~~~
TYPE
~~~~
<type 'list'>
 
>>> 
```


