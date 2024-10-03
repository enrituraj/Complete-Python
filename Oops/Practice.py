# Define base class Animal
class Animal:
    # Method that will be overridden in subclasses
    def make_sound(self):
        print("Animal makes a sound")

# Define the subclass Dog that inherits from Animal
class Dog(Animal):
    # Override the make_sound method for Dog
    def make_sound(self):
        print("Bark")

# Define the subclass Cat that inherits from Animal
class Cat(Animal):
    # Override the make_sound method for Cat
    def make_sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.make_sound()  # Output: Bark
cat.make_sound()  # Output: Meow
