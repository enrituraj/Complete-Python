
# my_set1 = {1,2,3,4,5}
# my_set2 = {4,5,6,7,8}

# for item,j in my_set1,my_set2:
#     print(item,j)

# Input: Take a string from the user
# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common_elements = set1 & set2  
# You can also use set1.intersection(set2)
print("Common elements:")
for element in common_elements:
    print(element)

