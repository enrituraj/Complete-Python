
# loops

# without index
my_tuple = (1,2,3,4,5)
for x in my_tuple:
    print(x)

# with index
my_tuple = (1,2,3,4,5)
for i in range(len(my_tuple)):
    print(i,my_tuple[i])

# using while loop
fruits = ("apple", "banana", "cherry")
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1 

# joins
fruit1 = ("apple", "banana", "cherry")
fruit2 = ("avocado", "blueberry", "coconut")

all_fruits = fruit1 + fruit2
print(all_fruits)
#('apple', 'banana', 'cherry', 'avocado', 'blueberry', 'coconut')

# repete n number of times a tuple

fruits = ("apple", "banana", "cherry")
my_tuple = fruits * 2

print(my_tuple) 
# ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')