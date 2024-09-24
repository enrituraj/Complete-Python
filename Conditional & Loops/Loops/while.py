# WHILE LOOP

# print 1 to 10
i = 1
while i <= 10:
    print(i)
    i +=1

# while loop with else
i = 1
while i <= 10:
    print(i)
    i +=1
else:
    print("we have reach the end")

# while loop with else 
# else part not get executed if break happen
i = 1
while i <= 10:
    print(i)
    break
    i +=1
else:
    print("we have reach the end")