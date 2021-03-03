import math


class MyClass:
    def method(self):
        return 'instance method called', self
        #('instance method called', <__main__.MyClass object at 0x7f7f4e4bc070>)

    @classmethod
    def class_method(cls):
        return 'class method called', cls
        #('class method called', <class '__main__.MyClass'>)

    @staticmethod
    def static_method():
        return 'static method called'
        #static method called


obj = MyClass()
print(obj.method())
print(MyClass.method(obj))
print(obj.class_method())
print(obj.static_method())


class A:
    x = 1

    @staticmethod
    def change_static():
        A.x = 2

    @classmethod
    def change_class(cls):
        cls.x = 3
print(A.x)
A.change_static()
print(A.x)
A.change_class()
print(A.x)
# both methods change the class state but the access is different
# @classmethod uses cls and @staticmethod calls the Class name



class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    # def __str__(self):
    #     return (f'Pizza2({self.radius!r}, '
    #                 f'{self.ingredients!r})')

    def __repr__(self):
        return (f'Pizza1({self.radius!r}, '
                f'{self.ingredients!r})')


    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p)
print(p.area())
print(Pizza.circle_area(4))
