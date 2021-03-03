### Static Methods

The third method, `MyClass.staticmethod` was marked with a [`@staticmethod`](https://docs.python.org/3/library/functions.html#staticmethod) decorator to flag it as a *static method*.

This type of method takes neither a `self` nor a `cls` parameter (but of course it’s free to accept an arbitrary number of other parameters).

Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.



### Instance Methods

The first method on `MyClass`, called `method`, is a regular *instance method*. That’s the basic, no-frills method type you’ll use most of the time. You can see the method takes one parameter, `self`, which points to an instance of `MyClass` when the method is called (but of course instance methods can accept more than just one parameter).

Through the `self` parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state.

Not only can they modify object state, instance methods can also access the class itself through the `self.__class__` attribute. This means instance methods can also modify class state.



### Class Methods

Let’s compare that to the second method, `MyClass.classmethod`. I marked this method with a [`@classmethod`](https://docs.python.org/3/library/functions.html#classmethod) decorator to flag it as a *class method*.

Instead of accepting a `self` parameter, class methods take a `cls` parameter that points to the class—and not the object instance—when the method is called.

Because the class method only has access to this `cls` argument, it can’t modify object instance state. That would require access to `self`. However, class methods can still modify class state that applies across all instances of the class.



Be aware that `__str__` has available the main string when the class is called.

 `__repr__` does the same thing but `__str__` overwrites it if is declared.

```python
def __str__(self):
    return (f'Pizza2({self.radius!r}, '
             f'{self.ingredients!r})')

def __repr__(self):
    return (f'Pizza1({self.radius!r}, '
            f'{self.ingredients!r})')
```