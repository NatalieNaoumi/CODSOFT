import random
import string

generateAgain = "yes"

while generateAgain =="yes":

    letters = string.ascii_letters
    numbers = string.digits
    symbol = string.punctuation

    together = letters + numbers + symbol

    length = int(input("How many letters would you like your password to have? "))

    passwordList = random.sample(together, length)
    password = ''.join(passwordList)

    print("Your new password is " + password)

    generateAgain = input("Would you like to generate another password? ")
