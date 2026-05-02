numbers = [ ]

for i in range(10):  
    while True:
        try:
            num = int(input('type a number: '))
            numbers.append(num)       
            break 
        except ValueError:  
          print ('please enter a valid input') 

smallest = numbers[0]
for i in numbers[1:]:
    if i < smallest: smallest = i
print(f'The smallest number on {numbers} is: ',smallest)