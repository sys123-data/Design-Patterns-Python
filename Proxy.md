The proxy design pattern includes a new object, which is called “Proxy” in place of an existing object which is called the “Real Subject”. The proxy object created of the real subject must be on the same interface in such a way that the client should not get any idea that proxy is used in place of the real object. Requests generated by the client to the proxy are passed through the real subject.

The UML representation of proxy pattern is as follows −

![Proxy Pattern](https://www.tutorialspoint.com/python_design_patterns/images/proxy_pattern.jpg)

## How to implement the proxy pattern?

Let us now see how to implement the proxy pattern.

```python
class Image:
   def __init__( self, filename ):
      self._filename = filename
   
   def load_image_from_disk( self ):
      print("loading " + self._filename )
   
   def display_image( self ):
      print("display " + self._filename)

class Proxy:
   def __init__( self, subject ):
      self._subject = subject
      self._proxystate = None

class ProxyImage( Proxy ):
   def display_image( self ):
      if self._proxystate == None:
         self._subject.load_image_from_disk()
         self._proxystate = 1
      print("display " + self._subject._filename )

proxy_image1 = ProxyImage ( Image("HiRes_10Mb_Photo1") )
proxy_image2 = ProxyImage ( Image("HiRes_10Mb_Photo2") )

proxy_image1.display_image() # loading necessary
proxy_image1.display_image() # loading unnecessary
proxy_image2.display_image() # loading necessary
proxy_image2.display_image() # loading unnecessary
proxy_image1.display_image() # loading unnecessary
```

### Output

The above program generates the following output −

![Proxy Pattern Output](https://www.tutorialspoint.com/python_design_patterns/images/proxy_pattern_output.jpg)

The proxy pattern design helps in replicating the images that we created. The display_image() function helps to check if the values are getting printed in the command prompt.