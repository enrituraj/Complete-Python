
### Lists in Python

1. Write a Python program to create a list of integers from user input and print the sum of all the elements in the list.
```python
user_inputs = []
while True:
    data = int(input("Enter a number (or press 0 to stop) : "))
    if data == 0:
        break
    user_inputs.append(data)

sum = 0
for number in user_inputs:
    sum += number

print(f"sum of all inputs is {sum}")
```


2. Write a program that takes a list of numbers and prints the largest and smallest elements in the list without using built-in functions like `max()` and `min()`.
```python
my_list = [14,65,11,9,80]
maximum = minimun = my_list[0]
for num in my_list:
    if num < minimun:
        minimun = num
    if num > maximum:
        maximum = num

print(minimun,maximum)

```


3. Create a Python program to remove all occurrences of a specified element from a list. The element and list should be provided by the user.
```python
user_input = input("Enter number separated by spaces : ")
input_list = user_input.split()

element = input("Enter the element that has to remove : ")
input_list.remove(element)
print("Item present in list ",input_list)

```
4. Write a Python program to replace all occurrences of a specified element in a list with another value provided by the user.


5. Write a Python program to merge two lists into a single list. Then, remove any duplicate elements from the merged list and print the result.

### List Comprehension

6. Use list comprehension to create a list of squares of all numbers from 1 to 20.
```python
square = [x*x for x in range(1,21)]
print(square)
```

7. Write a Python program using list comprehension to extract all even numbers from a given list of integers.
```python
my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
even_no = [x for x in my_list if x%2 == 0]
print(even_no)
```

8. Create a list of tuples using list comprehension, where each tuple contains a number and its square, for numbers between 1 and 10.
```python
# do it after tuple completed
```

9. Write a program to filter out words from a list that are shorter than 5 characters using list comprehension.
```python
words = ['john','mark','darwin']
newlist = [word for word in words if len(word) < 5]
print(newlist) 
```

10. Use list comprehension to convert a list of Celsius temperatures `[0, 10, 20, 30]` to Fahrenheit.
```python
celsius = [0, 10, 20, 30]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)
```


### Copying Lists

11. Write a Python program that demonstrates the difference between shallow copy and deep copy by copying a nested list. Modify the original list and show how the copies are affected.

12. Create a program to copy a list using slicing. Modify the original list and demonstrate that the copy remains unchanged.

13. Write a Python program to clone or copy a list using the `copy()` method. Verify that changes to the original list do not affect the copied list.

14. Create a Python program to copy a list using list comprehension. Modify the original list and show that the copy remains unaffected.

15. Write a Python program to create a deep copy of a list using the `copy` module. Demonstrate how changes in the nested list of the original do not affect the copied list.

### Sorting Lists

16. Write a Python program to sort a list of numbers in ascending order using the `sort()` method. Also, sort the list in descending order.
```python
my_list = [14,65,11,9,80]
# by default in ascending order
my_list.sort()
print(my_list)
# descending order
my_list.sort(reverse=True)
print(my_list)
```

17. Create a Python program to sort a list of strings by their lengths. Use the `key` argument in the `sort()` method.

18. Write a program to sort a list of dictionaries by a specific key (e.g., sorting a list of student dictionaries by their age).

19. Use the `sorted()` function to sort a list of tuples where each tuple contains a person's name and their age. Sort the list based on the age.

20. Write a Python program to reverse a list using both `reverse()` method and list slicing. Compare the results.
```python
my_list = [1,2,3,4,5]
my_list.reverse()
print(my_list) # [5, 4, 3, 2, 1]


my_list = [1,2,3,4,5]
# copy of list is created
print(my_list[::-1]) # [5, 4, 3, 2, 1]

```
### Methods Applicable on Lists

21. Write a Python program to append an item to a list and remove the last element using `append()` and `pop()`.
```python
my_list = [1,2,3,4]
# adding new element
my_list.append(5)

print(my_list)
# removing last element
my_list.pop()

print(my_list)
```
22. Create a Python program to count the occurrences of a specific item in a list using the `count()` method.
```python
my_list = [1,2,2,3,2,2,4]
# counting no of elements
no_of_occurance = my_list.count(2)
print(no_of_occurance)
```

23. Write a program to find the index of a specific element in a list using the `index()` method.
```python
my_list = [1,2,2,3,2,2,4]
# return index of first match
index = my_list.index(2)
print(index)
```

24. Write a Python program to extend a list with another list using the `extend()` method and demonstrate how it differs from `append()`.


25. Create a Python program that uses the `insert()` method to add an element at a specified position in the list.
```python
my_list = [1,2,3,4,5]
# insert(index,value)
my_list.insert(2,5)
print(my_list) # [1, 2, 5, 3, 4, 5]

```
---
