# : Classes & Objects

# - Introduction to OOP
# Object-Oriented Programming (OOP) in Python is a programming paradigm that structures code around objects, which are instances of classes. This approach helps in organizing code, improving reusability, and managing complexity in larger applications.
# Key Concepts of OOP in Python:
# Classes: A class serves as a blueprint or a template for creating objects. It defines the attributes (data) and methods (functions) that objects of that class will possess.

class Dog:
        # Class attribute
        species = "Canis familiaris"

        def __init__(self, name, age):
            # Instance attributes
            self.name = name
            self.age = age

        def bark(self):
            print(f"{self.name} says Woof!")