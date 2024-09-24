# FOR LOOP

# print no from 1 to 10
for i in range(1,11):
    print(i)

# print odd no from 1 to 10
for i in range(1,11,2):
    print(i)

# print even no from 1 to 10
for i in range(2,11,2):
    print(i)

for i in range(1,11):
    print(i)
else:
    print("we have reach the end")


# else part not get executed if break happen

for i in range(1,11):
    if i == 3:
        break
    print(i)
else:
    print("we have reach the end")
