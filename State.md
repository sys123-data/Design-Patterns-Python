It provides a module for state machines, which are implemented using subclasses, derived from a specified state machine class. The methods are state independent and cause transitions declared using decorators.

## How to implement the state pattern?

The basic implementation of state pattern is shown below −

```python
class ComputerState(object):

   name = "state"
   allowed = []

   def switch(self, state):
      """ Switch to new state """
      if state.name in self.allowed:
         print 'Current:',self,' => switched to new state',state.name
         self.__class__ = state
      else:
         print 'Current:',self,' => switching to',state.name,'not possible.'

   def __str__(self):
      return self.name

class Off(ComputerState):
   name = "off"
   allowed = ['on']

class On(ComputerState):
   """ State of being powered on and working """
   name = "on"
   allowed = ['off','suspend','hibernate']

class Suspend(ComputerState):
   """ State of being in suspended mode after switched on """
   name = "suspend"
   allowed = ['on']

class Hibernate(ComputerState):
   """ State of being in hibernation after powered on """
   name = "hibernate"
   allowed = ['on']

class Computer(object):
   """ A class representing a computer """
   
   def __init__(self, model='HP'):
      self.model = model
      # State of the computer - default is off.
      self.state = Off()
   
   def change(self, state):
      """ Change state """
      self.state.switch(state)

if __name__ == "__main__":
   comp = Computer()
   comp.change(On)
   comp.change(Off)
   comp.change(On)
   comp.change(Suspend)
   comp.change(Hibernate)
   comp.change(On)
   comp.change(Off)
```

### Output

The above program generates the following output −

![Design Pattern Output](https://www.tutorialspoint.com/python_design_patterns/images/design_pattern_output.jpg)