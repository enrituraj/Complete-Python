# union

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 
# {1, 'b', 2, 3, 'a', 'c'}

# we can use | (pipe) instead of union method

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) 

# update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) 


# intersection
set1 = {"apple", "banana", "cherry","blueberry"}
set2 = {"google", "blueberry","microsoft", "apple"}

set3 = set1.intersection(set2) # we can use & too
print(set3) # {'blueberry', 'apple'}

# intersection_update

set1 = {"apple", "banana", "cherry","blueberry"}
set2 = {"google", "blueberry","microsoft", "apple"}

set1.intersection_update(set2)

print(set1) # {'blueberry', 'apple'}

# difference

set1 = {"apple", "banana", "cherry","blueberry"}
set2 = {"google", "blueberry","microsoft", "apple"}

set3 = set1.difference(set2) # OR set3 = set1 - set2

print(set3) # {'banana', 'cherry'}

# difference_update

set1 = {"apple", "banana", "cherry","blueberry"}
set2 = {"google", "blueberry","microsoft", "apple"}

set1.difference_update(set2)

print(set1) # {'banana', 'cherry'}


# symmetric_difference

set1 = {"apple", "banana", "cherry","blueberry"}
set2 = {"google", "blueberry","microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) # {'banana', 'cherry', 'google', 'microsoft'}

# symmetric_difference_update

set1 = {"apple", "banana", "cherry","blueberry"}
set2 = {"google", "blueberry","microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1) # {'cherry', 'banana', 'google', 'microsoft'}

