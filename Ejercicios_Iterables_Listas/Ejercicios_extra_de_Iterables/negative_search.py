numbers = [ ]
negative = 0
for i in range(10):  
    while True:
        try: 
            num = int(input('type a number: '))
            if num < 0:
                numbers.append(num)
                negative += 1
            
            break 
        except ValueError:  
          print ('please enter a valid input') 
    
print(f'There is atleast {negative} numbers that are negative in the list!')