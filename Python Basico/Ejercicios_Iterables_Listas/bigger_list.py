numbers = [ ]

for i in range(10):
    big_num = (int(input(f'Please enter number {i+1}:')))
    numbers.append(big_num)
    
big_num = max(numbers)
print(f'The numbers you entered were: {numbers} and the biggest number is: {big_num}')