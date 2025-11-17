# Assignment:
# Build a Person class with name and age.
# Inherit it in a Student class with an added course attribute.
# Create and display two student objects.

# # Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Child class inheriting from Person
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")

# Creating two student objects
student1 = Student("Alice", 20, "Mathematics")
student2 = Student("Bob", 22, "Computer Science")

# Displaying student information
student1.display()
student2.display()

