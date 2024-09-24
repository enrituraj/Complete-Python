
# python doesn't have do-while like c/c++
while True:
    user_input = int(input("enter a no"))
    if user_input == 0:
        break
    else:
        print(f"you have enter a non-zero value {user_input}")

