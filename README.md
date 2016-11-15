# que_es
When navigating the vast and wonderful Python ecosystem, it seems there is always a new object for which to ask "What Is This?!".

`que_es.esto()`, spanish for what is this, helps to quickly explain the object's class so you can continue forward.

To get to know a new class, you could read the docs, the API description, or use builtins with print statements, but why pull up a web browser when there are builtings, but who wants to type `print(var(object)), print(dirs(object)), print(object.__doc__")` every time they have a question.

With one command, this module prints object's attributes, methods, docstring, and type, in an easily readable format.

Installation:
`pip install que_es`

Usage:

```python

>>> import que_es
>>> que_es.esto([1,2,3])

```

```
----
VARS
----
Object has no --dict-- attributes
 
---
DIR
---
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
 
---------
DOCSTRING
---------
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
 
----
TYPE
----
<type 'list'>
```
