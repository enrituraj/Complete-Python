- Deep Dive In Conditional & Loops
    

    
    ### Conditional Statements
    
    1. Write a Python program to check if a number is positive, negative, or zero using `if-else`.

    ```python
    num = int(input("Enter a number : "))

    if num == 0:
        print("Given number is Zero.")
    elif num < 0:
        print(f"{num} is a negative number")
    elif num > 0:
        print(f"{num} is a positive number")
    else:
        print(f"Given value is not a number.")
    ```

    2. Write a Python program that takes three numbers as input and prints the largest one using nested `if-else`.
    ```python
    
    a = int(input("Enter a first number : "))
    b = int(input("Enter a second number : "))
    c = int(input("Enter a third number : "))

    if a > b:
        if a > c : 
            print(f"{a} is the greatest number")
        else:
            print(f"{c} is the greatest number")
    else:
        if c > b:
            print(f"{c} is the greatest number")
        else:
            print(f"{b} is the greatest number")
    ```

    3. Write a program to check whether a character is a vowel or consonant using `if-else`.
    ```python
    char = str(input("Enter a character : "))

    if char in 'aeiouAEIOU':
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")
    ```


    4. Write a Python program that checks if a given year is a leap year using `if-elif-else`.
    ```python
    year = int(input("Enter a year : "))

    if year % 400 == 0:
        print(f"{year} is a Leap year.")
    elif year % 100 == 0:
        print(f"{year} is a Non-Leap year.")
    elif year % 4 == 0:
        print(f"{year} is a Leap year.")
    else:
        print(f"{year} is a Non-Leap year.")
    ```

    5. Write a Python program to determine if a given number is divisible by both 3 and 5.
    ```python
    num = int(input("Enter a number : "))

    if num % 3 == 0 and num % 5 == 0 :
        print(f"{num} is divisible by 3 or 5.")
    else:
        print(f"{num} is not divisible by 3 or 5.")
    ```
    
    ### Loops (For, While)
    
    1. Write a Python program to print all numbers from 1 to 100 using a `for` loop.
    ```python
    for i in range(101):
    print(i)
    ```
    2. Write a Python program to print the multiplication table of a given number using a `while` loop.
    ```python
    num = int(input("Enter the number to print the table : "))

    i = 1
    while i <= 10:
        print(f"{num} * {i} = {num * i}")
        i += 1
    ```

    3. Write a Python program to calculate the sum of all numbers from 1 to `n` (where `n` is user input) using a `for` loop.
    ```python
    n = int(input("Enter a number : "))
    sum = 0

    for i in range(1,n+1):
        sum += i

    print(f"sum of all number till {n} = {sum}")
    ```
    4. Write a Python program to reverse a number using a `while` loop.
    ```python
    num = int(input("Enter the number to see their reverse : "))
    reversed_num = 0

    while num > 0:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num //=10

    print(f"Reverse = {reversed_num}")
    ```
    5. Write a Python program to print all prime numbers between 1 and 50 using a `for` loop.
    ```python
    for num in range(2,51):
        is_prime = True
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                
        if is_prime:
            print(num)    
    ```
    ### Nested Loops
    
    1. Write a Python program to print the following pattern using nested `for` loops:
        
        ```
        *
        **
        ***
        ****
        *****
        
        ```
    ```python
    for i in range(6):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    ```
        
    2. Write a Python program to print a multiplication table from 1 to 10 using nested `for` loops.
    ```python
    
    for num in range(11):
        for i in range(11):
            print(f"{num} * {i} = {num * i}")
        print()
    ```

    3. Write a Python program to print the following pattern using nested loops:
        
        ```
        1
        12
        123
        1234
        12345
        ```
    ```python
    for i in range(6):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
    ```
        
    4. Write a Python program that checks whether a number is prime or not using nested loops.
    ```python
    
    for num in range(2,51):
        is_prime = True
        for i in range(2,int(num ** 0.5) +1):
            if num % i == 0:
                is_prime = False
                
        if is_prime:
            print(num)    
    ```

    5. Write a Python program to print the following pattern using nested `for` loops:
        
        ```
        *****
        ****
        ***
        **
        *
        
        ```
    ```python
    for i in range(5,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()
    ```
        
    
    ### Control Flow (continue, break, pass)
    
    1. Write a Python program that prints numbers from 1 to 10, but skips the number 5 using the `continue` statement.
    ```python
    for i in range(11):
        if i == 5:
            continue
        print(i)
    ```
    2. Write a Python program that accepts input from the user until they enter a negative number, using the `break` statement to exit.
    ```python
    while True:
        user_input = int(input("Enter a number : "))
        if user_input < 0:
            break
        print("You have enter a postive number.")
    ```

    3. Write a Python program that counts from 1 to 10, but uses the `pass` statement inside the loop. (Explain its use in comments.)
    ```python
    for i in range(1,11):
        if i > 0:
            # 'pass' is a placeholder that does nothing;
            # used when no action is needed
            pass
        print(i)
    ```

    4. Write a Python program to print the first 10 numbers, but stop the loop if the sum of the numbers exceeds 30, using the `break` statement.
    ```python
    total_sum = 0  

    for i in range(1, 11):  
        total_sum += i 
        if total_sum > 30:  
            break  
        print(i) 
    ```

    
    ### Match Statement (Python 3.10+)
    
    1. Write a Python program using the `match` statement to implement a basic calculator that performs addition, subtraction, multiplication, and division based on user input.
    ```python
    
    num1 = int(input("Enter a first number : "))
    num2 = int(input("Enter a second number : "))
    operator = input("Enter a operator (+,-,*,/) : ")

    match operator:
        case '+':
            print(f"sum of {num1} and {num2} is {num1+num2}")
        case '-':
            print(f"Difference of {num1} and {num2} is {num1-num2}")
        case '*':
            print(f"{num1} * {num2} = {num1*num2}")
        case '/':
            print(f"{num1} / {num2} = {num1//num2}")
        case _:
            print("invalid operator")
    ```

    2. Write a Python program using the `match` statement to determine the type of a triangle (equilateral, isosceles, or scalene) based on the lengths of its sides.


    3. Write a Python program that uses the `match` statement to classify a given day of the week (input as a number 1-7) into "Weekday" or "Weekend."
    ```python
    day = int(input("Enter a day as (1,7) : "))

    match day:
        case 1 | 2 | 3 | 4 | 5:
            print("weekday")
        case 6 | 7:
            print("Weekend!")
        case _:
            print("Not in range.")
    ```

    4. Write a Python program using the `match` statement to check a student's grade based on their score (A, B, C, D, or F).

    5. Write a Python program that uses the `match` statement to map a month number (1-12) to its corresponding season (Spring, Summer, Fall, Winter).