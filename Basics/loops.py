value = 1
# while value < 10:
#     print(value)
#     value += 1


# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("value is now equal to " + str(value))


# For loops
names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)


# for x in range(4):
#     print(x)

# for x in range(2, 5):
#     print(x)


for x in range(0, 30, 5):
    print(x)

else:
    print("Glad that\'s over!")

actions = ["code", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")


for name in names:
    for action in actions:
        print(name + " " + action + ".")
