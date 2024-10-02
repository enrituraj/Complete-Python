
### **Basic Function Definition and Usage**

1. **Area Calculator**: Write a Python function `calculate_area(shape, dimension)` that takes the name of a shape (`"circle"`, `"square"`, or `"rectangle"`) and its dimensions as arguments. The function should calculate and return the area of the shape based on the given dimensions.
```python
import math

def area_of_square(dimension):
    side = dimension[0]
    return side * side

def area_of_rectangle(dimension):
    length,breadth = dimension
    return length * breadth

def area_of_circle(dimension):
    radius = dimension[0]
    return math.pi * radius* radius


def calculate_area(shape, dimension = []):
    if shape == "circle":
        radius = int(input("Enter the radius : "))
        dimension.append(radius)
        area = area_of_circle(dimension)
        print(f"area of circle is {area}")
    elif shape == "rectangle":
        length = int(input("Enter the length : "))
        breadth = int(input("Enter the breadth : "))
        dimension.append(length)
        dimension.append(breadth)
        area = area_of_rectangle(dimension)
        print(f"area of rectangle is {area}")
    elif shape == "square":
        side = int(input("Enter the side : "))
        dimension.append(side)
        area = area_of_square(dimension)
        print(f"area of square is {area}")
    else:
        print("Our program only support (circle,rectangle,square)")

shape = input("Enter the shape name (circle,rectangle,square) : ")
calculate_area(shape)
```


2. **Temperature Converter**: Write a Python function `convert_temperature(temp, to_scale)` that converts a temperature from Fahrenheit to Celsius or vice versa. The function should accept the temperature and a scale (`"C"` for Celsius or `"F"` for Fahrenheit) and return the converted temperature.
```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_temperature(temp, to_scale):
    if to_scale == "C":
        temp_in_celsius = fahrenheit_to_celsius(temp)
        print(f"{temp} temperature in celsius {temp_in_celsius}")
    elif to_scale == "F":
        temp_in_fahrenheit = celsius_to_fahrenheit(temp)
        print(f"{temp} temperature in fahrenheit {temp_in_fahrenheit}")

    else:
        print("Not having a correct scale,Please choose 'C' for Celsius or 'F' for Fahrenheit ")

temp = float(input("Enter the temperature :"))
to_scale = input("Enter 'C' for Celsius or 'F' for Fahrenheit : ")
convert_temperature(temp,to_scale)
```

3. **Greeting Message**: Write a Python function `greet(name)` that takes a person's name as an argument and prints a personalized greeting message, such as “Hello, John! Welcome!”.
```python
def greet(name):
    print(f"Hello, {name}! Welcome!")

name = input("Enter your name : ")
greet(name)

```

4. **Factorial Calculation**: Write a Python function `factorial(n)` that calculates and returns the factorial of a given number `n` using recursion.
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number to calculate factorial : "))
factorial_of_n = factorial(n)
print(f"Factorial of {n} is {factorial_of_n}")

```

5. **Palindrome Check**: Write a Python function `is_palindrome(s)` that checks if a given string is a palindrome. The function should return `True` if the string is a palindrome and `False` otherwise.
```python
def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string to check it is palindrome or not : ")
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")

```

### **`*args` (Arbitrary Arguments)**

6. **Sum of Numbers**: Write a Python function `sum_numbers(*args)` that takes any number of arguments and returns their sum. Test the function with various numbers of arguments (e.g., `sum_numbers(1, 2, 3, 4)`).
```python
def sum_numbers(*num):
    total = 0
    for n in num[0]:
        total += n
    return total

num = input("Enter the number seperate by comma (,) : ")
num_list = map(int,num.split(","))
total = sum_numbers(num_list)
print(f"sum of all numbers are {total}")

```

7. **Maximum of Numbers**: Write a Python function `find_max(*args)` that takes any number of numeric arguments and returns the maximum value.
```python
def find_max(*nums):
    maximum = 0
    for n in nums[0]:
        if n > maximum:
            maximum = n
    return maximum

num = input("Enter the number seperate by comma (,) : ")
num_list = list(map(int,num.split(",")))
maximum = find_max(num_list)
print(f"maximum in all of them are {maximum}")


```

8. **Concatenate Strings**: Write a Python function `concatenate_strings(*args)` that takes any number of string arguments and returns a single concatenated string.
```python
def concatenate_strings(*string):
    single_string = ""
    for words in string[0]:
        single_string += words + " "

    return single_string

strings = input("Enter the words seperate by comma (,) : ")
strings_list = strings.split(",")
single_string = concatenate_strings(strings_list)
print(f"string looks like {single_string}")


```


9. **Average Calculator**: Write a Python function `calculate_average(*args)` that takes any number of arguments and returns their average.
```python

def calculate_average(*num):
    num_list = num[0]
    total = 0
    for n in num_list:
        total += n
    avg = total / len(num_list)
    return avg

num = input("Enter the number seperate by comma (,) : ")
num_list = list(map(int,num.split(",")))
average = calculate_average(num_list)
print(f"Average is {average}")
```


10. **Shopping List**: Write a Python function `shopping_list(*items)` that accepts an arbitrary number of items and prints each item in the shopping list.
```python
def shopping_list(*items):
    if not items:
        print("The shopping list is empty.")
    else:
        print("shopping list: ")
        for item in items:
            print(item)

shopping_list("milk","bread","gram")
```
### **`**kwargs` (Keyword Arguments)**

11. **Employee Info**: Write a Python function `employee_info(**kwargs)` that accepts keyword arguments like `name`, `age`, `position`, and `salary`, and prints the employee’s information in a readable format.
```python

def employee_info(**kwargs):
    if not kwargs:
        print("No employee information provided.")
        return
    
    # Print employee information
    print("Employee Information:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# Example usage of the function
employee_info(name="Yojesh kumar", age=30, position="Software Engineer", salary=75000)
# output
    # Employee Information:
    #     Name: Yojesh kumar
    #     Age: 30
    #     Position: Software Engineer
    #     Salary: 75000
```

12. **Student Grades**: Write a Python function `student_grades(**kwargs)` that accepts keyword arguments for student names and their grades, then prints each student’s name along with their grade.
```python
def student_grades(**kwargs):
    # Check if kwargs is empty
    if not kwargs:
        print("No student grades provided.")
        return
    
    # Print each student's name and grade
    print("Student Grades:")
    for student, grade in kwargs.items():
        print(f"{student}: {grade}")

student_grades(Aman=85, Priya=90, Rahul=78, Neha=92)
# output 
# Student Grades:
#     Aman: 85
#     Priya: 90
#     Rahul: 78
#     Neha: 92
```

13. **Build Profile**: Write a Python function `build_profile(first_name, last_name, **kwargs)` that builds a dictionary representing a user profile. The function should take the first and last names as required arguments and additional information (like age, location, and occupation) as optional keyword arguments.

14. **Book Details**: Write a Python function `book_details(**kwargs)` that accepts keyword arguments representing book details (e.g., title, author, year, genre) and prints these details in a formatted way.

15. **Order Details**: Write a Python function `order_details(**kwargs)` that accepts keyword arguments for order details like `order_id`, `customer_name`, `product`, and `quantity`, then prints the order information.

### **Lambda Functions**

16. **Square of Numbers**: Write a Python lambda function that takes a number as input and returns its square. Test it on different numbers.
```python
square = lambda x : x ** 2
num = int(input("Enter a number to get its square : "))
print(f"square of {num} is {square(num)}") 
```

17. **Sort by Length**: Given a list of strings, use a lambda function to sort the list in ascending order based on the length of the strings. Write the program to demonstrate this.

18. **Filtering Even Numbers**: Use a lambda function with the `filter()` function to filter out even numbers from a list of integers.
```python
nums = [1,2,3,4,5,6,7,8,9,10]
even_nums = list(filter(lambda x :x % 2 == 0,nums))
print(even_nums)
```

19. **Multiplication of Elements**: Write a lambda function that takes two numbers and multiplies them. Then, use this function to multiply a list of numbers by 2 using the `map()` function.
```python
multiply = lambda x,y=2 : x *y
nums = [1,2,3,4,5,6,7,8,9,10]

multiplied_nums = list(map(multiply,nums))
print(multiplied_nums)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

20. **Key Sorting**: Given a list of dictionaries representing products (with keys `"name"`, `"price"`), use a lambda function to sort the products based on their prices in descending order.

---
