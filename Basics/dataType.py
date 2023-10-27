## String data type 

#Literal assignment
first = 'King'
last = 'Xerxes'

# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str ))

## constructor function 

# pizza = str("Chicken MAn pizza ")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str ))


## Concatenation
fullName = first + " " + last 
print(fullName)

fullName += "!"
print(fullName)


## Casting a number to a string 
# decade = str(1999)


# statement = "I like rock music form the " + decade +  "s. "
# print(statement)

# # Escaping special characters 
# sentence = 'I\'m back at work!\t'
# print(sentence )


## String methods 

print(first)
print(first.lower())
print(first.upper())
print(first)

print(last.title())

print(last.replace('Xerxes', 'Isaac'))