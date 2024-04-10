import random

options = ["rock", "paper", "scissors"]

playAgain="yes"

while playAgain == "yes":

    playerChoice = input("Pick: rock, paper, or scissors? ")
    computerChoice = random.choice(options)

    if playerChoice == "rock" and computerChoice == "paper":
            result = "The computer wins!"
    elif playerChoice == "rock" and computerChoice == "scissors":
            result = "You win!"
    elif playerChoice == "paper" and computerChoice == "rock":
            result = "You win!"
    elif playerChoice == "paper" and computerChoice == "scissors":
            result = "The computer wins!"
    elif playerChoice == "scissors" and computerChoice == "paper":
            result = "You win!"
    elif playerChoice == "scissors" and computerChoice == "rock":
            result = "The computer wins!"
    else:
            result = "You tie!"

    print("You chose " + playerChoice)
    print("The computer chooses " + computerChoice)
    print(result)

    playAgain = input("Would you like to play again?")
