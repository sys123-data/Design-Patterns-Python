Command Pattern adds a level of abstraction between actions and includes an object, which invokes these actions.

In this design pattern, client creates a command object that includes a list of commands to be executed. The command object created implements a specific interface.

Following is the basic architecture of the command pattern −

![Architecture of Command Pattern](https://www.tutorialspoint.com/python_design_patterns/images/architecture_of_command_pattern.jpg)

## How to implement the command pattern?

We will now see how to implement the design pattern.

```python
def demo(a,b,c):
   print 'a:',a
   print 'b:',b
   print 'c:',c

class Command:
   def __init__(self, cmd, *args):
      self._cmd=cmd
      self._args=args

   def __call__(self, *args):
      return apply(self._cmd, self._args+args)
cmd = Command(dir,__builtins__)
print cmd()

cmd = Command(demo,1,2)
cmd(3)
```

### Output

The above program generates the following output −

![Command Pattern](https://www.tutorialspoint.com/python_design_patterns/images/command_pattern.jpg)

### Explanation

The output implements all the commands and keywords listed in Python language. It prints the necessary values of the variables.

