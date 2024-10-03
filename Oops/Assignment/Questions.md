
### **Classes and Objects**

1. **Car Class**: Write a Python class `Car` with attributes like `make`, `model`, and `year`. Include a method `get_info()` that prints out the details of the car. Create an object of this class and call the method.

2. **Bank Account**: Create a class `BankAccount` with attributes like `account_number`, `balance`, and methods `deposit()` and `withdraw()`. Write a Python program to create an object of this class and perform deposit and withdrawal operations.

3. **Student Class**: Define a `Student` class with attributes `name`, `age`, and `grades`. Add a method `get_average_grade()` that calculates and returns the average of the grades. Create a student object and test the method.

4. **Rectangle Class**: Create a class `Rectangle` with attributes `length` and `width`. Include methods to calculate and return the area and perimeter of the rectangle. Create multiple objects with different dimensions and print their areas and perimeters.

5. **Library System**: Create a `Book` class with attributes `title`, `author`, and `status` (borrowed or available). Implement methods `borrow()` and `return_book()`. Write a Python program to create book objects and simulate borrowing and returning books.

### **Inheritance**

6. **Animal Inheritance**: Create a base class `Animal` with a method `make_sound()`. Then, create two subclasses, `Dog` and `Cat`, that override the `make_sound()` method to print the respective sounds ("Bark" for Dog and "Meow" for Cat). Create objects of each subclass and test the `make_sound()` method.

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
