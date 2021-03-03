Decorator pattern allows a user to add new functionality to an existing object without altering its structure. This type of design pattern comes under structural pattern as this pattern acts as a wrapper to existing class.

This pattern creates a decorator class, which wraps the original class and provides additional functionality keeping the class methods signature intact.

The motive of a decorator pattern is to attach additional responsibilities of an object dynamically.

## How to implement decorator design pattern

The code mentioned below is a simple demonstration of how to implement decorator design pattern in Python. The illustration involves demonstration of a coffee shop in the format of class. The coffee class created is an abstract, which means that it cannot be instantiated.

```python
import six
from abc import ABCMeta

@six.add_metaclass(ABCMeta)
class Abstract_Coffee(object):

   def get_cost(self):
      pass

   def get_ingredients(self):
      pass
   
   def get_tax(self):
      return 0.1*self.get_cost()

class Concrete_Coffee(Abstract_Coffee):
   
   def get_cost(self):
      return 1.00
   
   def get_ingredients(self):
      return 'coffee'

@six.add_metaclass(ABCMeta)
class Abstract_Coffee_Decorator(Abstract_Coffee):
   
   def __init__(self,decorated_coffee):
      self.decorated_coffee = decorated_coffee
   
   def get_cost(self):
      return self.decorated_coffee.get_cost()
   
   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients()

class Sugar(Abstract_Coffee_Decorator):
   
   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
   
   def get_cost(self):
      return self.decorated_coffee.get_cost()
   
   def get_ingredients(self):
	   return self.decorated_coffee.get_ingredients() + ', sugar'

class Milk(Abstract_Coffee_Decorator):
   
   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
   
   def get_cost(self):
      return self.decorated_coffee.get_cost() + 0.25
   
   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients() + ', milk'

class Vanilla(Abstract_Coffee_Decorator):
   
   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
   
   def get_cost(self):
      return self.decorated_coffee.get_cost() + 0.75
   
   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients() + ', vanilla'
```

The implementation of the abstract class of the coffee shop is done with a separate file as mentioned below −

```python
import coffeeshop

myCoffee = coffeeshop.Concrete_Coffee()
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Milk(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Vanilla(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Sugar(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))
```

### Output

The above program generates the following output −

![Decorator Pattern](https://www.tutorialspoint.com/python_design_patterns/images/decorator_pattern.jpg)