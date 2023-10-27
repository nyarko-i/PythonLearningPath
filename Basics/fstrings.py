person = "King"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left")
message = f"\n {person} has {coins} coins left."
print(message)


message = f"\n {person.lower()} has {coins} coins left."
print(message)


message = f"\n {person.lower()} has {2 * 5} coins left."
print(message)


# You can also pass formatiing options
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}\n")


for num in range(1, 11):
    print(f"{num} divided by 4.52 is  {num /4.52:.2%}\n")
