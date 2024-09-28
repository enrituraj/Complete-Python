
### Python Tuple

1. Write a Python program to create a tuple of integers. Then, print each element of the tuple using a `for` loop.
```python
my_tuple = (1,2,3,4,5)

for i in range(len(my_tuple)):
    print(my_tuple[i])
```

2. Create a tuple with mixed data types (e.g., integers, floats, strings). Write a program to display the type of each element in the tuple.
```python
my_tuple = (1,2,True,"Str",3j)

for i in range(len(my_tuple)):
    print(my_tuple[i])
```

3. Write a Python program to check if an element exists in a tuple. If it exists, print the index of the element.
```python
my_tuple = (1,2,3,4,5)

if 3 in my_tuple:
    print(my_tuple.index(3))
```

4. Write a Python program to convert a tuple into a list, modify the list, and convert it back into a tuple.
```python
my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)
my_list[0] = 99
my_tuple = tuple(my_list)
print(my_tuple) # (99, 2, 3, 4, 5)
```

5. Create a program that takes a tuple of numbers as input from the user and prints the sum, minimum, and maximum values.
```python
nums = input("Enter numbers separated by commas: ")
my_tuple = tuple(map(int,nums.split(",")))
print("your input",my_tuple)

total_sum = sum(my_tuple)
minimum = min(my_tuple)
maximum = max(my_tuple)

print(f"Sum : {total_sum}")
print(f"Minimum : {minimum}")
print(f"Maximum : {maximum}")
```

### Access and Update

6. Write a Python program to access the first and last elements of a tuple. Use both positive and negative indexing.
```python
my_tuple = (1,2,3,4,5)
# first element
print(my_tuple[0])
print(my_tuple[-len(my_tuple)])

#last element
print(my_tuple[len(my_tuple) - 1])
print(my_tuple[-1])
```

7. Write a Python program to slice a tuple. Extract elements from index 2 to 5 from the tuple `(10, 20, 30, 40, 50, 60)`.
```python
my_tuple = (10, 20, 30, 40, 50, 60)
print(my_tuple[2:5]) #(30, 40, 50)
```

8. Write a program to demonstrate that tuples are immutable by attempting to change an element of a tuple. Handle the error gracefully.
```python
    # do it after exception handing
```
9. Write a Python program that creates a tuple, converts it to a list, updates an element of the list, and then converts the list back into a tuple.
```python
my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)
my_list[0] = 99
my_tuple = tuple(my_list)
print(my_tuple) # (99, 2, 3, 4, 5)
```

10. Create a Python program to access the elements of a tuple using a `for` loop, printing both the index and the element.
```python
my_tuple = (10, 20, 30, 40, 50, 60)

for i in range(len(my_tuple)):
    print(f"Index {i} : Element {my_tuple[i]}")
```

### Unpacking

11. Write a Python program that unpacks the tuple `(1, 2, 3)` into three variables `a`, `b`, and `c`, and prints the values of these variables.
```python
my_tuple = (1,2,3)

a,b,c = my_tuple
print(f"Value of a : {a}")
print(f"Value of b : {b}")
print(f"Value of c : {c}")
```

12. Create a tuple containing 5 elements and unpack the first two elements into individual variables, while the remaining elements are stored in another variable using the `*` operator.
```python
my_tuple = (10,20,30,40,50)

n1,n2,*n3 = my_tuple

print(f"Value of n1 : {n1}") # 10
print(f"Value of n2 : {n2}") # 20
print(f"Value of n3 : {n3}") # [30, 40, 50]
```

13. Write a Python program to swap the values of two variables using tuple unpacking.
```python
a = 20
b = 30
my_tuple = (a,b)

b,a = my_tuple
print(f"Value of a : {a}") # 30
print(f"Value of b : {b}") # 20
```

14. Write a Python program that takes a tuple of three elements (name, age, city) and unpacks them into individual variables.
```python
data = ("jhon",30,"London")
print(data)
name, age, city = data
print("Name : ",name)
print("Name : ",age)
print("Name : ",city)
```

15. Create a Python program that accepts a tuple with different lengths of sequences and unpacks them using extended unpacking (`*` operator).
```python
user_input= input("Enter elements separated by commas: ")
# example - user_input -> 1,2,3,4,5
my_tuple = tuple(user_input.split(","))

first , *second_list , last = my_tuple

print(f"value of first : {first}") # 1 
print(f"value of second : {second_list}") # [2,3,4]
print(f"value of last : {last}") # 5
```

### Join

16. Write a Python program to join two tuples into one. Display the result of concatenating `(1, 2, 3)` and `(4, 5, 6)`.
```python
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2
print(tuple3)
```

17. Create a program to concatenate multiple tuples and print the result.
```python
my_tuple = (1,2,3)
print(my_tuple * 3)
# 1, 2, 3, 1, 2, 3, 1, 2, 3)

```

18. Write a Python program to join two tuples, but before joining, check if both tuples contain at least one common element. If yes, concatenate them, otherwise return an error message.
```python
    # do it after exception handing
```

19. Write a Python program to repeat a tuple `n` times using the `*` operator. Take `n` as input from the user.
```python
my_tuple = (1,2,3)
print(my_tuple)

n = int(input("Enter the vlaue of n to repeate tuple : "))
print(my_tuple * n)

```

20. Write a Python program to join a tuple of strings into a single string, separated by spaces or a given delimiter.
```python
my_tuple = ("Hello","world,","i","am","on","fire","🔥")
delimeter = "-"
result = delimeter.join(my_tuple)
print(result)
# Hello-world,-i-am-on-fire-🔥
```

### Tuple Methods

21. Write a Python program to count the occurrences of an element in a tuple using the `count()` method.
```python
my_tuple = ("apple","banana","coconut","banana")
print(my_tuple.count("banana")) # 2

```

22. Create a Python program to find the index of a specified element in a tuple using the `index()` method.
```python
my_tuple = ("apple","banana","coconut","banana")
print(my_tuple.index("banana")) # 1

```

23. Write a Python program to find and print the first occurrence of the number 5 in a tuple. If the element is not found, handle the error gracefully.
```python
    # do it after exception handing
```

24. Write a Python program to create a tuple, find the length of the tuple using the `len()` function, and print the result.
```python
my_tuple = (1,2,3,4,5,6,7)
print(len(my_tuple))
```

25. Create a Python program that demonstrates the immutability of tuples by trying to modify an element. Then, show how tuple methods like `index()` and `count()` can still work.
```python
my_tuple = (1,2,3,4,5)
# my_tuple[0] = 99  
#TypeError: 'tuple' object does not support item assignment

print(my_tuple)

print(my_tuple.count(2)) # number of occurrences of 2 = 1.
print(my_tuple.index(5)) # index of 5 = 4
```

---
