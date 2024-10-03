
### **Classes and Objects**

1. **Car Class**: Write a Python class `Car` with attributes like `make`, `model`, and `year`. Include a method `get_info()` that prints out the details of the car. Create an object of this class and call the method.
```python
class Car:
    def __init__(self,make,model,year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def get_info(self) -> str:
        print("---"*30)
        return f"Car Information:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}"


tesla = Car("Tesla", "Model 3", 2022)
print(tesla.get_info())
bmw = Car("BMW", "X5", 2021)
print(bmw.get_info())
mercedes = Car("Mercedes", "C-Class", 2020)
print(mercedes.get_info())
audi = Car("Audi", "A4", 2017)
print(audi.get_info())
```


2. **Bank Account**: Create a class `BankAccount` with attributes like `account_number`, `balance`, and methods `deposit()` and `withdraw()`. Write a Python program to create an object of this class and perform deposit and withdrawal operations.
```python
class BankAccount:
    def __init__(self,name,account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0

    def get_info(self):
        print(f"Your current Account balanace is {self.balance}")

    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} is deposited successfully")

    def withdraw(self,amount):
        self.balance -= amount
        print(f"{amount} is withdrawal successfully")


john = BankAccount("John","123")
john.deposit(500)
john.withdraw(100)
john.get_info()
```

3. **Student Class**: Define a `Student` class with attributes `name`, `age`, and `grades`. Add a method `get_average_grade()` that calculates and returns the average of the grades. Create a student object and test the method.
```python
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades  # a list of grades
    
    def get_average_grade(self):
        if self.grades: 
            return sum(self.grades) / len(self.grades)
        else:
            return 0 

    def print_student_info(self):
        print(f"Student: {self.name}\nAge: {self.age}\nAverage Grade: {self.get_average_grade():.2f}")


student1 = Student("Raj Kumar", 20, [85, 90, 78, 92, 88])
student1.print_student_info()

```

4. **Rectangle Class**: Create a class `Rectangle` with attributes `length` and `width`. Include methods to calculate and return the area and perimeter of the rectangle. Create multiple objects with different dimensions and print their areas and perimeters.
```python

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def print_details(self):
        print(f"Rectangle with length {self.length} and width {self.width}:")
        print(f"Area: {self.area()} square units")
        print(f"Perimeter: {self.perimeter()} units")
        print("-" * 40)

rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(10, 4)
rectangle3 = Rectangle(7, 2)

rectangle1.print_details()
rectangle2.print_details()
rectangle3.print_details()

```

5. **Library System**: Create a `Book` class with attributes `title`, `author`, and `status` (borrowed or available). Implement methods `borrow()` and `return_book()`. Write a Python program to create book objects and simulate borrowing and returning books.
```python

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "available" 

    def borrow(self):
        if self.status == "available":
            self.status = "borrowed"
            print(f"You have successfully borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' by {self.author} is currently borrowed.")
    
    def return_book(self):
        if self.status == "borrowed":
            self.status = "available"
            print(f"Thank you for returning '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' by {self.author} was not borrowed.")
    
    def book_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Status: {self.status}")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

book1.book_info() 
book1.borrow()     
book1.book_info()  

print("\n")

book2.book_info()  
book2.borrow()    
book2.book_info()  

print("\n")
book2.return_book()  
book2.book_info()    

print("\n")
book3.book_info()  
book3.return_book()  

```

### **Inheritance**

6. **Animal Inheritance**: Create a base class `Animal` with a method `make_sound()`. Then, create two subclasses, `Dog` and `Cat`, that override the `make_sound()` method to print the respective sounds ("Bark" for Dog and "Meow" for Cat). Create objects of each subclass and test the `make_sound()` method.
```python
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

```

7. **Vehicle Inheritance**: Create a base class `Vehicle` with attributes like `speed` and methods like `drive()`. Then, create two subclasses `Car` and `Bike` that inherit from `Vehicle`. Add additional attributes or methods specific to cars and bikes. Create objects of both classes and test their functionality.

8. **Employee and Manager**: Write a base class `Employee` with attributes `name`, `id`, and `salary`, and a method `get_details()`. Create a subclass `Manager` that inherits from `Employee` and adds an attribute `department`. Override the `get_details()` method to include department information. Create an object of `Manager` and test it.

9. **Shape Inheritance**: Create a base class `Shape` with an abstract method `area()`. Create two subclasses `Circle` and `Square` that implement the `area()` method for their respective shapes. Test the implementation by creating objects of `Circle` and `Square`.

10. **School System**: Create a base class `Person` with attributes `name` and `age`, and a method `get_info()`. Create subclasses `Student` and `Teacher` that inherit from `Person` and add specific attributes like `grades` for students and `subject` for teachers. Override the `get_info()` method in each subclass. Create objects of both subclasses and call the `get_info()` method.

### **Polymorphism**

11. **Polymorphic Sound**: Create a base class `Instrument` with a method `play()`. Then, create subclasses `Guitar` and `Piano`, both of which override the `play()` method to print different sounds. Write a function that accepts an `Instrument` object and calls its `play()` method, demonstrating polymorphism.

12. **Payment System**: Write a base class `Payment` with a method `process_payment()`. Create two subclasses `CreditCardPayment` and `PayPalPayment`, each implementing `process_payment()` differently. Write a function that takes a `Payment` object and processes it, demonstrating polymorphism.

13. **Employee Polymorphism**: Create a base class `Employee` with a method `get_salary()`. Create two subclasses `FullTimeEmployee` and `PartTimeEmployee` that override the `get_salary()` method. Demonstrate polymorphism by calculating the salary of both types of employees using a single method.

14. **Transportation Polymorphism**: Create a base class `Transportation` with a method `move()`. Subclasses `Car`, `Plane`, and `Boat` should each have their own `move()` method (e.g., "driving", "flying", and "sailing"). Demonstrate polymorphism by calling `move()` on different transportation objects.

15. **Animal Actions**: Write a base class `Animal` with a method `action()`. Create subclasses `Bird` and `Fish` that override the `action()` method (e.g., birds fly and fish swim). Write a function that takes an `Animal` object and calls its `action()` method, demonstrating polymorphism.

### **Method Overriding and Super()**

16. **Smartphone Class**: Create a base class `Phone` with a method `call()` that prints "Making a call." Create a subclass `Smartphone` that overrides the `call()` method to also print "Using an app to make a call." Use the `super()` function to call the parent class method from the subclass.

17. **Vehicle Overriding**: Create a base class `Vehicle` with a method `start()` that prints "Vehicle is starting." Create a subclass `ElectricCar` that overrides `start()` to print "Electric car is starting." Use the `super()` method to call the `Vehicle`'s `start()` method before adding its own functionality.

18. **Food Menu**: Write a base class `Food` with a method `display()` that prints "Food Menu". Create a subclass `Dessert` that overrides `display()` to print "Dessert Menu" but also calls the parent class's `display()` using `super()`.

19. **Online Course**: Create a base class `Course` with attributes `title` and `duration` and a method `display_info()` that prints course details. Create a subclass `OnlineCourse` that adds an attribute `platform` and overrides `display_info()` to include the platform name. Use `super()` to call the parent class’s method and extend it.

20. **Company Hierarchy**: Create a base class `Employee` with a method `work()`. Create a subclass `Manager` that overrides the `work()` method but calls the parent class’s `work()` using `super()` to print both the employee’s and manager’s work duties.

---
