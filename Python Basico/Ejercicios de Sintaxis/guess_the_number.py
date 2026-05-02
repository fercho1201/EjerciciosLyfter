import random
guess = {0,10}
guess = random.randint(0,10)
while True:
    number = (int(input(f"Guess a number between 1 and 10 : ")))
    if number >= 11:
        print('You have to chose a number between 1 and 10, try again!')
    elif number < guess:
        print('try one more time!')
    elif number > guess:
        print('try one more time!')
    else:
        print("Congratulations! You guessed the number.")
    break
        


