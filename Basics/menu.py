# Building a  menu 
title = 'menu'.upper()
print(title.center(20, "="))
print("coffee".ljust(16, ".")+ "$3".rjust(4))
print("Muffin".ljust(16, ".")+ "$7".rjust(4))
print("Cheesecake".ljust(16, ".")+ "$3".rjust(4))
print("Hotdogs".ljust(16, ".")+ "$10".rjust(4))

print(' ')


#String index values 
first = 'Isaac'
last = 'King'

print(first[1:-1])


## returning boolean

print(first.startswith('d'))
print('')
## Boolean data type 
myValue = True
x = bool(False)
print(type(x))


print('')
## Numeric Data types 

price = 100 
best_price = int(80)
print(type(price))
print(bool(best_price))

print('')
# Built in Function of numbers 
print(abs(33.4567))
print(round(6.7877, 1))

import math