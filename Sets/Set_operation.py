# access item
my_set = {"a","b","c"}

for item in my_set:
    print(item)

# add items
my_set = {"a","b","c"}

my_set.add("d")
print(my_set)
# {'a', 'c', 'd', 'b'}

# add set to current set
current_set = {"a","b","c"}
my_set = {1,2,3,4}

current_set.update(my_set)
print(current_set)
# {'c', 1, 2, 3, 4, 'a', 'b'}


# add Any Iterable

my_set = {"a","b","c"}
my_list = [1,2,3,4]

my_set.update(my_list)
print(my_set)
# {'c', 2, 'a', 1, 3, 4, 'b'}


# # Remove item
#     1. remove() 
#     2. discard()

my_set = {"a","b","c"}
my_set.remove("b")
print(my_set) # {'c', 'a'}

my_set = {"a","b","c"}
my_set.discard("d") 
# not getting error if item not exits
print(my_set) # {'c', 'a'}

# pop
my_set = {"a","b","c"}
my_set.pop() 
print("pop",my_set)

# clear

my_set = {"a","b","c"}
my_set.clear()
print(my_set) # set()

#del

my_set = {"a","b","c"}
del my_set
