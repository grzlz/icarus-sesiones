# 1. Create a `Person` class with `name` and `age` attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 2. Create an instance of the `Person` class and assign attributes to it.
yo = Person("Memo", 26)

# 3. Add a `birthday` method to the `Person` class that increases the person's age by one.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

# 4. Modify the `Person` class to include an initialization method that assigns `name` and `age` to instances when they're created.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


# 5. Create a `Student` class that inherits from `Person` and includes an additional `grade` attribute.
class Student(Person):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Student still has access to birthday()

# 6. Override the `birthday` method in `Student` class so that it also prints a congratulatory message.
class Student(Person):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def birthday(self):
        print("Ya no cumples mas")
        
# 7. Use the `super()` function in the `Student` class to call the `birthday` method of the `Person` class.

# 8. Modify the `Person` class to make the `age` attribute private. Add a method that returns the value of `age`.

# 9. Use property decorators (`@property` and `@<attribute>.setter`) to get and set the value of private attributes in the `Person` class.

# 10. Add a `species` class attribute to the `Person` class and print it for an instance of the class.

# 11. Add a class method that modifies the `species` class attribute and call it on the class.

# 12. Add a static method that returns a greeting message, and call it on an instance of the class.

# 13. Create a `Teacher` class that inherits from both `Person` and a new `Employee` class.

# 14. Implement a method in the `Person`, `Student`, and `Teacher` classes that behaves differently in each class.

# 15. Add a `__str__` method to the `Person` class that returns a string representing a person instance.
