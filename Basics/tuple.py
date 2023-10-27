mytuple = tuple([1, 'Neil', True])
anotherTuple = (1,3,5,4)

print(mytuple)
print(type(mytuple))
print(type(anotherTuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey ) = anotherTuple
print(one)
print(two)
print(hey)

