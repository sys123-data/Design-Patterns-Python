Singleton pattern restricts the instantiation of a class to one object. It is a type of creational pattern and involves only one class to create methods and specified objects.

It provides a global point of access to the instance created.

![Singleton Pattern](https://www.tutorialspoint.com/python_design_patterns/images/singleton_pattern.jpg)

## How to implement a singleton class?

The following program demonstrates the implementation of singleton class where it prints the instances created multiple times.

```python
class Singleton:
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
s = Singleton()
print s

s = Singleton.getInstance()
print s

s = Singleton.getInstance()
print s
```

### Output

The above program generates the following output −

![Implementation of Singleton](https://www.tutorialspoint.com/python_design_patterns/images/implementation_of_singleton.jpg)

The number of instances created are same and there is no difference in the objects listed in output.