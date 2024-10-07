a = 5
# b = 0
# b = 'z'
b = 5

try:
    x = a/b
    print(x)
except ZeroDivisionError:
    print("not able to divide a no by 0")
except Exception:
    print("Something went wronge")
finally:
    print("program executed successfully")
