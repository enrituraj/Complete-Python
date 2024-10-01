employees_db = {
    "101": "Rajesh Kumar",
    "102": "Sita Patel",
    "103": "Amit Sharma",
    "104": "Priya Nair",
    "105": "Vikram Singh",
    "106": "Neha Gupta",
    "107": "Arjun Mehta",
    "108": "Anjali Rao"
}
# access item
# access item with its key
print(employees_db["101"])

# change value
employees_db["101"] = "Raj kumar"
print(employees_db["101"])

employees_db.update({"101":"Rajesh kumar"})
print(employees_db["101"])


# add item
employees_db["109"] = "Muskan kumari"
print(employees_db["109"])

employees_db.update({"110":"Puja kumari"})
print(employees_db["110"])

# Remove item
employees_db.pop("110") # remove user with id 110
employees_db.popitem() # remove user with id 109 or last one

print(employees_db)