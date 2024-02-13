from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

obj1 = Person("Shukurs", 21)
print(obj1.age)