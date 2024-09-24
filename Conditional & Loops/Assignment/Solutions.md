Solutions:

1. **Write a program to determine if a number is odd or even, taking input from the user.**
```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")
```

2. **Accept a name from the user and display a personalized greeting message.**

```python
name = input("Enter your name: ")

print(f"Welcome {name}")
print(f"I think {name}, you are doing well in life")
```

3. **Create a program to input principal, rate, and time (P, R, T) from the user and compute Simple Interest.**

```python
principal = int(input("Enter the principal amount :"))
rate = int(input("Enter the rate % :"))
time = int(input("Enter the time in years :"))

simple_interest = ( principal * rate * time ) / 100

print(f"Simple interest is {simple_interest}")

```

4. **Accept two numbers and an operator (+, -, *, /) from the user and calculate the result. (Use if-else conditions)**

```python 

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operator = input("Choose the operator (+,-,*,/,%) : ")

result = None

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 // num2
elif operator == '%':
    result = num1 % num2
else:
    print("invaid operator")
    exit()

print(f"Result is {result} after performing {operator} on {num1 , num2}")
```


5. **Input two numbers and print which one is greater.**

```python
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")
```


6. **Convert an amount entered in rupees to USD.**

```python 
EXCHANGE_RATE = 82.33 # 1USD = 82.33 inr

# convert usd to inr
amount_usd = int(input("Enter Amount (USD) : "))
amount_in_inr = amount_usd * EXCHANGE_RATE
print(f"${amount_usd} = {amount_in_inr} inr")

# convert inr to usd
amount_inr = int(input("Enter Amount (INR) : "))
amount_in_usd = amount_inr / EXCHANGE_RATE
print(f"{amount_inr} inr = ${amount_in_usd}")
```


7. **Generate the Fibonacci sequence up to 'n' terms.**

```python
n = int(input("Enter the number of term for Fibonacci sequence : "))

first_term = 0
second_term = 1
count = 2

while(count < n):
    next_term = first_term + second_term
    print(next_term)
    first_term = second_term
    second_term = next_term
    count = count + 1 # count += 1

```

8. **Check if a given string is a palindrome.**

```python
    string = str(input("Enter the string : "))
i=0
string_length = len(string)
is_palindrome = True

while i <= (string_length/2):
    if string[i] != string[(string_length - i) -1]:
        is_palindrome = False
        break
    i += 1

if is_palindrome == False:
    print(f"{string} is not palindrome")
else:
    print(f"{string} is palindrome")
```

9. **Find all Armstrong numbers between two specified numbers.**


10. **Input a year and determine if it's a leap year.**


11. **Take two numbers as input and display their sum.**

```python
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

sum = num1 + num2
print(f"sum of {num1} and {num2} is {sum}")
```


12. **Accept a number from the user and print its multiplication table.**
```python
num = int(input("Enter the number : "))

for i in range(1,11):
    print(f"{num} * {i} = {num * i}")

```

13. **Input two numbers and calculate both their HCF and LCM.**

14. **Continuously take numbers as input until the user enters 'x', then display the total sum of all entered numbers.**
```python 
user_input = None
total_sum = 0

while True:
    user_input = input("Enter a number : ")
    if (user_input == 'x') or (user_input == 'X'):
        print("Total sum =",total_sum)
        break
    else:
        total_sum +=int(user_input)
```

15. **Input a number and print all the factors of that number (use loops).**

16. **Take integer inputs till the user enters 0 and print the sum of all numbers (HINT: while loop).**
```python
user_input = None
total_sum = 0

while True:
    user_input = int(input("Enter a number : "))
    if user_input == 0:
        print("Total sum =",total_sum)
        break
    else:
        total_sum +=user_input
```

17. **Take integer inputs till the user enters 0 and print the largest number from all.**
```python
largest_number = 0

while True:
    user_input = int(input("Enter a number : "))
    if user_input == 0:
        print("largest number is ",largest_number)
        break 

    if user_input > largest_number:
        largest_number = user_input

```


18. **Subtract the Product and Sum of Digits of an Integer.**


19. **Print Fibonacci Series.**


20. **Calculate Average Marks.**
```python
math = int(input("enter marks of math : "))
phy = int(input("enter marks of physics : "))
che = int(input("enter marks of chemistry : "))

avg_marks = (math + phy + che) // 3
print(f"average marks is {avg_marks}")

```