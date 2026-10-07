import random

number_to_guess=random.randint(1,100)
while True:
  try:
    guess=int(input("Guess the number between 1 and 100>> "))  

    if guess < number_to_guess:
      print("Too Low!")
    elif guess > number_to_guess:
      print("Too High")
    else:
      print("Congragulations! you guessed the number")

  except ValueError:
    print("please,Enter the valid number")