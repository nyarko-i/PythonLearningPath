users = ['Dave', 'King', 'Sara']

data = ['King', 43, True]

emptylist = []

print('Dave' in emptylist)

print(users[0])
print(users[-1])

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

users.extend(['Robert', 'Cecil'])
print(users)

# users.extend(data)
# print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']
print(users)

users.remove('Dave')           
print(users)   

print(users.pop())
print(users)

del users[0]
print(users)

#del data
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users )

users.sort(key=str.lower)
print(users )

nums = [4,43,5,22,45]
nums.reverse()
print(nums)
nums.sort(reverse=True)
print(nums)

numscopy = nums.copy 
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,'neil', True])
print(mylist)


