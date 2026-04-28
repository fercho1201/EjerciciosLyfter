numbers = [ ]
new_biggest = [ ]
for i in range(10):  
    while True:
        try:
            num = int(input('type a number: '))
            numbers.append(num)       
            break 
        except ValueError:  
          print ('please enter a valid input') 

average = sum(numbers)/len(numbers)
for i in numbers[1:]:
    if i > average: 
        new_biggest.append(i)


print(f'The average score is: ',average ,' and the numbers bigger than the avg are: ',new_biggest)