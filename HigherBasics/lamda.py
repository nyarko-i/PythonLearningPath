# Lamda function is a single expression that returns a value

from functools import reduce
def squared(num): return num * num
# lamda num : num * num


print(squared(2))


def addTwo(num): return num + 2
# lamda num: num + 2


print(addTwo(12))


def sumTotal(a, b): return a + b


# lamda a, b: a + b
print(sumTotal(10, 8))


########################

def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)
print(addTen(7))
print(addTwenty(7))


##################

# A higher order function is a function that returns a function as it's results


numbers = [3, 7, 12, 18, 20, 21]

squaredNums = map(lambda num: num * num, numbers)
print(list(squaredNums))

###################

odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))


numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 20)
print(total)

print(sum(numbers, 20))
