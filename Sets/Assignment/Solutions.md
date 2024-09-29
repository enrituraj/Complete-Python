### Sets in Python

1. Write a Python program to create a set of integers and print all its elements. Demonstrate that sets do not allow duplicate values.
```python
my_nums = {1,2,3,4,5,1,2,3}

for item in my_nums:
    print(item) # 1,2,3,4,5

```

2. Create a Python program that initializes a set with multiple data types (e.g., integers, strings, floats). Display the set and verify that it can hold elements of different types.
```python
my_set = {1,2,3,True,"john"}
# 1 - true
# 0 - false
for item in my_set:
    print(item) # 1,2,3,john

```

3. Write a program to create a set of numbers. Check whether a specified number is present in the set using the `in` keyword and print an appropriate message.
```python
my_set = {1,2,3,4}

if 2 in my_set:
    print("2 is in the set ", my_set)
```

4. Write a Python program to convert a list into a set and print both the original list and the converted set. Note the differences in the order of elements.
```python
my_list = [1,2,3,4,5]
my_set = set(my_list)

print("List ",my_list)
print("Set ",my_set)

```

5. Write a Python program to convert a string into a set of characters. Use a string input from the user.
```python
user_input = input("Enter a string: ")
char_set = set(user_input)
print("Set of characters:", char_set)
# {'p', 'l', 'e', 'a'}
```

### Access, Update, and Remove Items from a Set

6. Write a Python program to add a single item to an existing set using the `add()` method and print the updated set.
```python
my_set = {"a","b","c"}

my_set.add("d")
print(my_set)
# {'a', 'c', 'd', 'b'}
```

7. Write a Python program to update a set by adding multiple elements (e.g., from a list or another set) using the `update()` method.
```python
current_set = {"a","b","c"}
my_set = {1,2,3,4} #set
my_list = [11,12,13,14] #list

current_set.update(my_set)
current_set.update(my_list)
print(current_set)
# {1, 2, 3, 4, 'a', 11, 12, 13, 14, 'b', 'c'}
```

8. Write a program to remove a specified element from a set using the `remove()` method. Handle the case when the element does not exist in the set by catching the `KeyError`.
```python

my_set = {"a","b","c"}
my_set.remove("b")
print(my_set) # {'c', 'a'}

# error part will after try-expect
```

9. Write a Python program to discard an element from a set using the `discard()` method and explain how it differs from `remove()`.
```python

my_set = {"a","b","c"}
my_set.discard("d") 
# not getting error if item not exits
print(my_set) # {'c', 'a'}
```

10. Create a Python program that uses the `pop()` method to remove and return an arbitrary element from the set. Print the set before and after using `pop()`.
```python
my_set = {"a","b","c"}
my_set.pop() 
print("pop",my_set)
```

### Join Operations

11. Write a Python program to perform the union of two sets and print the result. Demonstrate the `union()` method.
```python
set1 = {1,2,3,4}
set2 = {5,6,7,8}

set3 = set1.union(set2)
print(set3) # {1, 2, 3, 4, 5, 6, 7, 8}
```

12. Write a Python program to find the intersection of two sets using the `intersection()` method and print the common elements.
```python
set1 = {1,2,3,4}
set2 = {3,4,5,6}

set3 = set1.intersection(set2)
print(set3) # {3,4}
```

13. Create a Python program to find the difference between two sets (i.e., elements that exist in the first set but not in the second) using the `difference()` method.
```python
set1 = {1,2,3,4}
set2 = {3,4,5,6}

set3 = set1.difference(set2)
print(set3) # {1,2}

set4 = set2.difference(set1)
print(set4) # {5,6}
```

14. Write a Python program to compute the symmetric difference of two sets using the `symmetric_difference()` method and explain its purpose.
```python

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set3 = set1.symmetric_difference(set2)

print(set3) # {1,2,5,6}
```

15. Write a Python program to check if one set is a subset of another using the `issubset()` method. If it is, print an appropriate message.
```python
set1 = {1,2,3,4}
set2 = {3,4}

is_subset = set2.issubset(set1)
print(is_subset) # True

if is_subset:
    print("set2 is a subset of set1")
```

### Loop Over Sets

16. Write a Python program that iterates over a set of numbers and prints only the even numbers.
```python
my_set = {1,2,3,4,5,6} 

for item in my_set:
    if item % 2 == 0:
        print(item)
```

17. Write a Python program to iterate over a set of words and print each word along with its length.
```python
my_set = {"apple","axe","bat","ball"} 

for item in my_set:
    print(f"item {item}: {len(item)} charcter")
    
"""
item bat: 3 charcter
item ball: 4 charcter
item apple: 5 charcter
item axe: 3 charcter
"""
```


18. Create a program that creates a set of unique elements from a list and then loops over the set to print all elements that are greater than a specified value.
```python

my_list = [1,2,1,3,4,5,6,1,2,1]
my_set = set(my_list)
print("Given Set =",my_set)
specific_value = int(input("Choose a no from given set : "))

for item in my_set:
    if item > specific_value:
        print(item)
```

19. Write a Python program that iterates over two sets simultaneously and prints the common elements found in both sets.
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common_elements = set1 & set2  
# You can also use set1.intersection(set2)
print("Common elements:")
for element in common_elements:
    print(element)
```

20. Write a Python program that uses a `for` loop to add all elements of a set of integers and prints the total sum.
```python
my_set = {1,2,3,4,5}
total = 0
for item in my_set:
    total += item
print("total sum =",total) #15
```

### Set Methods in Python

21. Write a Python program to check if two sets are disjoint (i.e., they have no elements in common) using the `isdisjoint()` method.
```python
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

if set1.isdisjoint(set2):
    print("The sets are disjoint (no elements in common).")
else:
    print("The sets are not disjoint (they have common elements).")

```

22. Write a Python program to check if a set is a superset of another set using the `issuperset()` method. Print a message indicating whether the first set contains all elements of the second.
```python
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3}

if set1.issuperset(set2):
    print("set1 is a superset of set2 (contains all elements of set2).")
else:
    print("set1 is not a superset of set2.")
```

23. Write a Python program to clear all elements from a set using the `clear()` method. Print the set before and after clearing.
```python
my_set = {1, 2, 3, 4, 5}
print("Set before clearing:", my_set)

my_set.clear()
print("Set after clearing:", my_set)

```

24. Create a Python program that creates a frozen set using the `frozenset()` function and attempts to modify it. Explain why this is not possible by catching the error.
```python
    # do it after try-catch
```

25. Write a Python program that copies a set using the `copy()` method. Modify the original set and demonstrate that the copied set remains unaffected.
```python
original_set = {1, 2, 3, 4, 5}
copied_set = original_set.copy()
original_set.add(6)
print("Original set after modification:", original_set)
print("Copied set:", copied_set)

```

---
