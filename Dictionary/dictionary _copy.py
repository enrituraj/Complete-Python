user = {
    "name" : "john",
    "age": 40,
    "password": "pass123"
}

# both are same
user_data = user.copy()
# user_data = dict(user_data)

user_data["age"] = 41

print(user_data["age"]) # 41
print(user["age"]) # 40