numbers = [ ]

for i in range(10):  
    while True: 
        try: 
            num = int(input('type a number: '))
            numbers.append(num)
            break
        except ValueError:  
          print ('please enter a valid input or number') 
    
search = int(input('type the number you like to search: '))

print(f'The number {search} appears {numbers.count(search)} times')
