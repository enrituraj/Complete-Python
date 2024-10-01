# salary_data =  dict(
#                     John= 7000,
#                     Rahul= 10000,
#                     Manoj= 500000,
#                     Raj= 80000,
#                     Aman= 40000
#                 )

salary_data = {
    "John": 7000,
    "Rahul": 10000,
    "Manoj": 500000,
    "Raj": 80000,
    "Aman": 40000,
}

# printing key of a dict
for key in salary_data:
    print(key)

for key in salary_data.keys():
    print(key)

# printing values of a dict
for key in salary_data:
    print(salary_data[key])

for val in salary_data.values():
    print(val)

# printing both item
for key,val in salary_data.items():
    print(f"{key}:{val}")