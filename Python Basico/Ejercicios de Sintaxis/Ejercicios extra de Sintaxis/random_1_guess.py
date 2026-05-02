import random
guess = {0,10}
guess = random.randint(0,10)
number = (int(input(f"Guess a number between 1 and 10 : ")))
while number != guess:
    number = (int(input(f"Guess a number between 1 and 10 : ")))
else:
        print("Congratulations! You guessed the number.")