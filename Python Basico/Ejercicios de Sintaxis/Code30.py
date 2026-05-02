counter = 1
number_sum = 0
number = 0
answer = 'incorrect'
while counter <= 3:
    number = int(input(f"Enter number {counter}: "))
    counter += 1
    number_sum += number
    
    if number == 30:
        answer = 'correct'
        
    if number_sum == 30:
        answer = 'correct'
            
print("This code is", answer)
