The `*args` and `**kwargs` is a common idiom to allow arbitrary number of arguments to functions as described in the section [more on defining functions](http://docs.python.org/dev/tutorial/controlflow.html#more-on-defining-functions) in the Python documentation.

The `*args` will give you all function parameters [as a tuple](https://docs.python.org/dev/tutorial/controlflow.html#arbitrary-argument-lists):

```python
def foo(*args):
    for a in args:
        print(a)        

foo(1)
# 1

foo(1,2,3)
# 1
# 2
# 3
```

The `**kwargs` will give you all **keyword arguments** except for those corresponding to a formal parameter as a dictionary.

```python
def bar(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])  

bar(name='one', age=27)
# age 27
# name one
```

Both idioms can be mixed with normal arguments to allow a set of fixed and some variable arguments:

```python
def foo(kind, *args, **kwargs):
   pass
```

It is also possible to use this the other way around:

```python
def foo(a, b, c):
    print(a, b, c)

obj = {'b':10, 'c':'lee'}

foo(100,**obj)
# 100 10 lee
```

Another usage of the `*l` idiom is to **unpack argument lists** when calling a function.

```python
def foo(bar, lee):
    print(bar, lee)

l = [1,2]

foo(*l)
# 1 2
```

In Python 3 it is possible to use `*l` on the left side of an assignment ([Extended Iterable Unpacking](http://www.python.org/dev/peps/pep-3132/)), though it gives a list instead of a tuple in this context:

```python
first, *rest = [1,2,3,4]
first, *l, last = [1,2,3,4]
```

Also Python 3 adds new semantic (refer [PEP 3102](https://www.python.org/dev/peps/pep-3102/)):

```python
def func(arg1, arg2, arg3, *, kwarg1, kwarg2):
    pass
```

Such function accepts only 3 positional arguments, and everything after `*` can only be passed as keyword arguments.