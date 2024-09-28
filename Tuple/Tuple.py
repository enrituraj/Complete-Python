my_tuple = (1,2,3,4,5)
my_tuple = tuple((1,2,3,4,5))


# # access
#     by Index
#     by negative indexing
#     by range based indexing

my_tuple = (1,2,3,4,5)
print(my_tuple[0]) # 1
print(my_tuple[-1]) # 5
print(my_tuple[2:5]) # (3,4,5)



# add.update,delete

# add
my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)
my_list.append(6)
my_tuple = tuple(my_list)
print(my_tuple) # (1,2,3,4,5,6)

# update
my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)
my_list[2] = 6
my_tuple = tuple(my_list)
print(my_tuple) # (1,2,6,4,5)

# remove
my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)
my_list.remove(1)
my_tuple = tuple(my_list)
print(my_tuple) # (2,3,4,5)

# delete
my_tuple = (1,2,3,4)
del my_tuple


# packing &  unpacking
my_tuple = (10,20,30)
a ,b, c = my_tuple
print(a,b,c) # 10,20,30

my_tuple = (10,20,30,40,50)
a ,b, *c = my_tuple
print(a,b,c) # 10,20,[30,40,50]

my_tuple = (10,20,30,40,50)
a ,*b, c = my_tuple
print(a,b,c) # 10 [20, 30, 40] 50

my_tuple = (10,20,30,40,50)
*a ,b, c = my_tuple
print(a,b,c) # [10, 20, 30] 40 50
