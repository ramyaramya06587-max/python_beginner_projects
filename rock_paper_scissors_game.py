import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Choose rock, paper, or scissors: ").lower()

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif user == "rock" and computer == "scissors":
        print("You win!")

    elif user == "paper" and computer == "rock":
        print("You win!")

    elif user == "scissors" and computer == "paper":
        print("You win!")

    else:
        print("Computer wins!")

    again = input("Do you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Game over!")
        break