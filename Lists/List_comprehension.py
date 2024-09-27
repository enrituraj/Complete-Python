
# list of no from 1 to 10
newlist = [x for x in range(1,11)] 
print(newlist)

# list of even no from 1 to 11
newlist = [x for x in range(1,11) if x%2 == 0] 
print(newlist)

# list of odd no from 1 to 10
newlist = [x for x in range(1,10) if x%2 != 0] 
print(newlist)

users = ['john','mark','darwin']
newlist = [user.upper() for user in users]
print(newlist) 


words = ['john','mark','darwin']
newlist = [word for word in words if len(word) < 5]
print(newlist) 