# A short Password Generator program to allow users genereate a strong password
import random
import string

# Function to generate random password


def passGen(numPass):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for chsr in range(passLength))
    return password


# Print to the console a welcoming message
print("**** WELCOME TO YOUR PASSWORD GENERATOR PAGE ****")

# Exception handling to ensure that users enters the exact value needed


try:
    numPass = int(input("PLEASE SPECIFY THE NUMBER OF PASSWORD NEEDED: "))
    passLength = int(input("PLEASE SPECIFY THE PASSWORD LENGTH: "))

# Specifying the amount of password a user needs
    for num in range(numPass):
        print('Your passowrd is: ', passGen(passLength))
except ValueError:
    print("Invalid input. Please enter a valid integers for the number of password length.")
