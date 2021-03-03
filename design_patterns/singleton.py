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
         print('1')
         raise Exception("This class is a design_patterns!")
      else:
         print('2')
         Singleton.__instance = self

s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)

r = Singleton()
print(r)