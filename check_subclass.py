class Parent:
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent))
print(issubclass(Parent, Child))

obj1 = Parent()
obj2 = Child()

print(isinstance(obj2, Child))
print(isinstance(obj1, Parent))
