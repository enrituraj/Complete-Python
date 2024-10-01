
### **Access, Change, Add, and Remove Items**

1. **Employee Database**: You have an employee database stored in a dictionary where employee IDs are the keys and their names are the values. Write a Python program to:
   - Access and print the name of an employee by their ID.
   - Update the name of an employee by their ID.
   - Add a new employee to the dictionary.
   - Remove an employee from the dictionary after they leave the company.

```python
employees_db = {
    "101": "Rajesh Kumar",
    "102": "Sita Patel",
    "103": "Amit Sharma",
    "104": "Priya Nair",
    "105": "Vikram Singh",
    "106": "Neha Gupta",
    "107": "Arjun Mehta",
    "108": "Anjali Rao"
}

# access item
print("Access item")
print("-"*32)

employee_id = input("Enter id : ")
if employee_id in employees_db:
    print(f"id: {employee_id} , name = {employees_db[employee_id]}")
else:
    print("invalid id")

print("-"*32)

# update item
print("Update item")
print("-"*32)

employee_id = input("Enter id : ")
if employee_id in employees_db:
    print(f"id: {employee_id} , name = {employees_db[employee_id]}")
    new_name = input("Enter new name : ")
    employees_db[employee_id] = new_name
    print("Record upated successfully.")
    print(f"id: {employee_id} , name = {employees_db[employee_id]}")
else:
    print("invalid id")

print("-"*32)

# add item
print("Add item")
print("-"*32)

employee_id = input("Enter your id : ")
employee_name = input("Enter your name : ")

employees_db.update({employee_id:employee_name})
print("New record added successfully.")
print(f"id: {employee_id} , name = {employee_name}")

print("-"*32)


# Remove item
print("Remove item")
print("-"*32)

employee_id = input("Enter id : ")
if employee_id in employees_db:
    employee_name = employees_db[employee_id]
    print(f"id: {employee_id} , name = {employee_name}")
    employees_db.pop(employee_id)
    print("Data deleted successfully.")
else:
    print("invalid id")

print("-"*32)

```

2. **Shopping Cart**: You are building a shopping cart system where items and their prices are stored in a dictionary. Write a program to:
   - Access and print the price of a specific item.
   - Add a new item to the shopping cart with its price.
   - Update the price of an existing item.
   - Remove an item from the shopping cart once the user removes it.
```python
items_prices = {
    "apple": 30,
    "banana": 10,
    "mango": 50,
    "orange": 20,
    "grapes": 40,
}

# access item
print("Access item")
print("-"*32)

item_name = input("Enter item name : ")
if item_name in items_prices:
    print(f"name : {item_name} , price = ${items_prices[item_name]}")
else:
    print("invalid item name")

print("-"*32)

```


3. **Online Courses**: You manage a dictionary where course names are the keys and the number of enrolled students is the value. Write a Python program to:
   - Access the number of students enrolled in a specific course.
   - Add a new course and its student count.
   - Update the number of students for a specific course.
   - Remove a course that has been discontinued.

4. **Bookstore Inventory**: You are maintaining a bookstore inventory where each book title is a key, and its quantity in stock is the value. Write a Python program to:
   - Access the quantity of a specific book.
   - Add a new book to the inventory.
   - Update the stock quantity for an existing book.
   - Remove a book once it is out of stock.

5. **Voting System**: You are managing a voting system where candidates’ names are the keys, and the number of votes they’ve received is the value. Write a Python program to:
   - Access the current votes for a specific candidate.
   - Add a new candidate to the voting system.
   - Update the votes for a candidate when they receive more.
   - Remove a candidate from the system if they drop out of the race.

---

### **Looping Over Dictionaries**

6. **Student Marks**: You have a dictionary where student names are the keys, and their marks are the values. Write a Python program to loop through the dictionary and:
   - Print each student's name and their marks.
   - Calculate and print the average marks of all students.
```python
marks_data = {
    "John": 70,
    "Rahul": 100,
    "Manoj": 50,
    "Raj": 80,
    "Aman": 40,
}
total_marks = 0

for name,marks in marks_data.items():
    print(f"{name} : {marks} marks")
    total_marks += marks

avg_marks = total_marks / len(marks_data)
print(f"Average marks = {avg_marks}")
```

7. **City Temperatures**: You are tracking the temperatures of various cities using a dictionary where the city name is the key and the temperature is the value. Write a Python program to:
   - Print each city’s name and its temperature.
   - Loop through the dictionary to find the city with the highest temperature.

8. **Company Salaries**: You have a dictionary that stores employee names as keys and their salaries as values. Write a Python program to:
   - Print each employee’s name and salary.
   - Calculate the total payroll (sum of all salaries).
   - Find and print the employee with the highest salary.
```python
salary_data = {
    "John": 7000,
    "Rahul": 10000,
    "Manoj": 500000,
    "Raj": 80000,
    "Aman": 40000,
}
total_payroll = 0
highest_salary = ["",0]
for name,salary in salary_data.items():
    print(f"{name} : {salary} marks")
    # calculat total payroll
    total_payroll += salary
    # calculating highest salary
    if salary  > highest_salary[1]:
        highest_salary[0] = name
        highest_salary[1] = salary

print(f"Total payroll = {total_payroll}")
print(f"Highest salary {highest_salary[0]} with {highest_salary[1]}")
```

9. **Library Books**: A library tracks the number of times each book has been borrowed in a dictionary. Write a Python program to:
   - Print each book title and the number of times it has been borrowed.
   - Loop through the dictionary to find the book that has been borrowed the most.

10. **E-Commerce Sales**: You are maintaining a dictionary where product names are keys, and the number of units sold is the value. Write a Python program to:
    - Print each product and its sales count.
    - Calculate and print the total number of units sold for all products.

```python
product_data = {
    "milk": 50,
    "bread": 10,
    "cookies": 30,
    "chocobar": 90,
    "gram": 40,
}
total_sale = 0

for product_name,sale in product_data.items():
    print(f"{product_name} : {sale} ")
    total_sale += sale

print(f"Total sale = {total_sale}")
```

---

### **Copying Dictionaries**

11. **School Subjects**: You have a dictionary where subjects are the keys, and the number of students enrolled in each subject is the value. Write a program to:
    - Create a copy of the dictionary.
    - Make changes to the original dictionary (e.g., add students to a subject).
    - Demonstrate that changes in the original do not affect the copied version.

12. **Car Inventory**: A car dealership has an inventory stored in a dictionary where car models are the keys, and the number of available units is the value. Write a program to:
    - Create a copy of the inventory.
    - Add new models to the original inventory.
    - Print both the original and copied inventories to show that they are independent.

13. **Financial Data**: You maintain a dictionary of monthly expenses where months are the keys, and the amount spent is the value. Write a program to:
    - Copy the dictionary.
    - Modify the original dictionary (e.g., add new expenses for the current month).
    - Verify that the copied dictionary remains unchanged.

14. **Movie Ratings**: You have a dictionary where movie names are the keys, and user ratings are the values. Write a Python program to:
    - Create a copy of the dictionary.
    - Modify the original dictionary by adding new movies or updating ratings.
    - Show how the copied dictionary is not affected by changes to the original.

15. **Restaurant Menu**: You manage a restaurant menu in a dictionary where dish names are keys, and their prices are the values. Write a program to:
    - Copy the menu.
    - Change prices in the original menu.
    - Show how the copy remains unaffected by price updates in the original.

---

### **Nested Dictionaries**

16. **University Courses**: You are managing a university system where departments are keys, and their values are dictionaries containing courses as keys and student enrollments as values. Write a Python program to:
    - Access the number of students enrolled in a specific course within a specific department.
    - Add a new course to a department.
    - Update the enrollment number for an existing course.

17. **Company Hierarchy**: Create a nested dictionary where department names are keys, and the values are dictionaries where employee names are keys, and their roles are values. Write a Python program to:
    - Access the role of a specific employee in a specific department.
    - Add a new employee to a department.
    - Update the role of an employee.

18. **Family Tree**: Create a nested dictionary to represent a family tree where each family member’s name is the key, and the value is another dictionary containing information such as age, relation, and occupation. Write a program to:
    - Access and print the occupation of a specific family member.
    - Update the occupation or age of a family member.
    - Add a new member to the family tree.

19. **Classroom Management**: Create a nested dictionary where each class is the key, and the value is another dictionary with student names as keys and their grades as values. Write a Python program to:
    - Access a student's grade in a specific class.
    - Add a new student and their grade to a class.
    - Update the grade of an existing student.

20. **Online Orders**: Create a nested dictionary to represent customer orders where customer names are the keys, and the values are dictionaries containing products as keys and the quantities ordered as values. Write a Python program to:
    - Access the quantity of a specific product ordered by a specific customer.
    - Add a new product to an existing customer's order.
    - Update the quantity of a product in an order.

Here are **5 questions** related to **dictionary methods** with real-world examples or scenarios to complete the list:

### **Dictionary Methods**

21. **Currency Converter**: You are building a currency converter where the keys are currency codes (e.g., "USD", "EUR"), and the values are exchange rates to the local currency. Write a Python program to:
   - Use the `get()` method to retrieve the exchange rate for a given currency. If the currency is not found, return a default message like "Currency not available."
   
22. **Employee Records**: You maintain a dictionary of employee IDs as keys and employee names as values. Write a Python program to:
   - Use the `pop()` method to remove an employee from the dictionary by their ID and print the updated dictionary. If the employee ID is not found, handle it gracefully.
   
23. **Student Grades**: You are managing student grades where student names are the keys, and their grades are the values. Write a Python program to:
   - Use the `items()` method to print each student's name along with their grade.
   - Use the `keys()` and `values()` methods to print all student names and their respective grades separately.

24. **Grocery Prices**: You have a dictionary that stores grocery items as keys and their prices as values. Write a Python program to:
   - Use the `update()` method to modify the price of an item, and add a new item if it doesn't already exist.
   - Use the `setdefault()` method to add an item to the dictionary only if it doesn't exist, and print the updated dictionary.

25. **Website Traffic Data**: You are tracking website visits where the keys are URLs and the values are the number of visits. Write a Python program to:
   - Use the `popitem()` method to remove and return the last added (URL, visits) pair from the dictionary.
   - Use the `clear()` method to reset the visit count by clearing the entire dictionary and print the empty dictionary.



---