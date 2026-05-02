import random
guess = {0,10}
guess = random.randint(0,10)
number = (int(input(f"Guess a number between 1 and 10 : ")))
if number != guess:
        print('no it, it was ', guess)
else:
        print("Congratulations! You guessed the number.")