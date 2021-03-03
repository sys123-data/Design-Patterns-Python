class _Tigger:

    def __str__(self):
        return "I'm the only one!"

    def roar(self):
        return 'Grrr!'

_instance = None

def Tigger(): #only once init ... 2nd 3rd etc time the object will be the same
    global _instance #in order to make changes to the global variable
    if _instance is None:
        _instance = _Tigger()
    return _instance

