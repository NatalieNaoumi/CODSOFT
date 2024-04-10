operator = input("Choose your operator! (+, -, *, /, %) ")

number1 = int(input("What's the first number? "))
number2 = int(input("What's the second number? "))

if operator == "+":
    answer = (number1) + (number2)
elif operator == "-":
    answer = number1 - number2
elif operator == "*":
    answer = number1 * number2
elif operator == "/":
    answer = number1 / number2
elif operator == "%":
    answer = number1 % number2
else:
    answer = "not valid, try again"

print("Your answer is " + str(answer))
