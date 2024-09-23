x = 10
name = "Ritu Raj"
is_active = True

# multiple variable assignment
a, b, c = 1, 2, 3

# multiple variable with same value
x = y = z = 100

# writing pattern of variable
# 1.Snake Case
user_age = 25
total_cost = 150.75
is_logged_in = False

# 2.Camel Case
userAge = 25
totalCost = 150.75
isLoggedIn = False

# 3.Pascal Case
UserAge = 25
TotalCost = 150.75
IsLoggedIn = False


# Constants
# Constants are variables that should not change and are typically written in all uppercase letters:

PI = 3.14159
MAX_USERS = 1000
API_KEY = "1234567890abcdef"

#  Single Underscore
_internal_value = 42

# Double Underscore
__private_value = 99

# input/output
# By default input accept data as string 

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("welcome ",name) # one space get added
print("welcome "+ name) # just concat it
print(f"welcome {name}") # we can add variable in one line

age: int = 25
name: str = "Ritu Raj"
is_student: bool = True
