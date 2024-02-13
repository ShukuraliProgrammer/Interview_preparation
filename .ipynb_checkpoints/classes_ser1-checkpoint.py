# class Dog:
#     attr1 = "Dog1"
#     def __init__(self):
#         attr1 = "Dog2"
#         return attr1
#
#     def attr1(self):
#         return "Salom"
#
# obj1 = Dog()
# res = obj1.__class__.attr1
# print(res)

class Base:
    def __init__(self):
        self.a = "GeeksforGeeks2"
        self.__c = "GeeksforGeeks"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()

print(obj1.a)
