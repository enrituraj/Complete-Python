user = {
    "name" : "john",
    "age": 40,
    "password": "pass123"
}

# copy() :	Returns a copy of the dictionary
user_copy = user.copy()
print(user_copy)

# clear() :	Removes all the elements from the dictionary
user_copy.clear()
print(user_copy)

# fromkeys()	Returns a dictionary with the specified keys and value
keys = ('name','age','password')
val = None

user_dict = dict.fromkeys(keys,val)
print(user_dict)

# or

keys = ('name','age','password')
user_dict = dict.fromkeys(keys)
print(user_dict)

# get()	Returns the value of the specified key
print(f"name : {user.get('name')}")
print(f"age : {user.get('age')}")


# items()	Returns a list containing a tuple for each key value 
for key,val in user.items():
    print(f"{key} : {val}")


# keys()	Returns a list containing the dictionary's keys
print("printing all key")
for key in user.keys():
    print(key)


# pop()	Removes the element with the specified key
print("using pop() : ")
print(user_dict)
user_dict.pop("age")
print(user_dict)


# popitem()	Removes the last inserted key-value pair
print("using popitem() : ")
print(user_dict)
user_dict.popitem()
print(user_dict)


# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
user.setdefault("is_admin",False)
print(user)

# update()	Updates the dictionary with the specified key-value pairs
# uodate existing value
user.update({"is_admin":True})
print(user)
# help in adding new item
user.update({"is_logged_in":True})
print(user)


# values()	Returns a list of all the values in the dictionary

for val in user.values():
    print(val)
