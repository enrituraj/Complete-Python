Solutions:

1. **What is the difference between declaring a variable using `x = 5` and `x = '5'` in Python?**
   - `x = 5` assigns an integer value (number) to `x`, while `x = '5'` assigns a string value (text) to `x`. They are of different data types, with one being an integer and the other a string.

2. **How would you get input from the user and store it in a variable named `age` in Python?**
   - You can use the `input()` function like this:
     ```python
     age = input("Enter your age: ")
     ```

3. **What does the `print()` function do in Python, and how can you use it to display multiple variables?**
   - The `print()` function outputs the values to the console. You can display multiple variables by separating them with commas:
     ```python
     name = "John"
     age = 25
     print("Name:", name, "Age:", age)
     ```

4. **If you input a number using `input()`, what data type is it stored as by default? How do you convert it to an integer?**
   - By default, the `input()` function stores the input as a string. To convert it to an integer, you can use `int()` like this:
     ```python
     number = int(input("Enter a number: "))
     ```

5. **Write a Python program that asks the user for their name and age, and then prints "Hello, [name]. You are [age] years old."**
   ```python
   name = input("Enter your name: ")
   age = input("Enter your age: ")
   print(f"Hello, {name}. You are {age} years old.")
   ```

6. **Explain the difference between concatenating strings and adding numbers in Python. What happens if you try to concatenate a string and a number?**
   - Concatenating strings combines two or more strings together, while adding numbers results in the sum of the values. If you try to concatenate a string and a number, Python will raise a `TypeError`. You need to convert the number to a string using `str()` before concatenating:
     ```python
     result = "Age: " + str(25)
     ```

7. **What will be the output of the following code snippet? Why?**
   ```python
   x = 10
   y = 20
   print('x + y =', x + y)
   ```
   - Output:
     ```
     x + y = 30
     ```
     The `print()` function first prints the string `'x + y ='`, then prints the result of `x + y` which is `10 + 20 = 30`.

8. **How can you format a string using f-strings to display a sentence with variable values? Provide an example.**
   - F-strings allow you to embed expressions inside string literals using curly braces `{}`. Example:
     ```python
     name = "Alice"
     age = 30
     print(f"Hello, {name}. You are {age} years old.")
     ```
     This will output:
     ```
     Hello, Alice. You are 30 years old.
     ```

9. **What happens if you try to assign a value to a variable using `x = input("Enter a number: ")` and then add it directly to another number like this: `y = x + 5`? How can you fix it?**
   - Since `x` is stored as a string from `input()`, trying to add a string to a number will cause a `TypeError`. To fix it, convert `x` to an integer first:
     ```python
     x = int(input("Enter a number: "))
     y = x + 5
     print(y)
     ```

10. **What is the difference between the following two code snippets, and what will they print?**
    ```python
    print("The answer is", 42)
    print("The answer is " + str(42))
    ```
    - In the first snippet, `print("The answer is", 42)` separates the string and number with a space and prints:
      ```
      The answer is 42
      ```
    - In the second snippet, `print("The answer is " + str(42))` explicitly concatenates the string and the string version of `42` without additional spaces. It prints:
      ```
      The answer is 42
      ```