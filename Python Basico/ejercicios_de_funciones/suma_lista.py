def sum_list(n):
    total = sum(n)
    return total 

#now i understand why you guys wanted me to change the name of the variable to n, it makes it easier to reuse the function with different lists, just make sure to assign the list you want to sum to the variable n, that way you can reuse the function with different lists.

cars_prices = [10000, 25000, 30300, 45000, 58000]
nums = [10, 20, 30, 40, 50]
print(f'The total is: {sum_list(cars_prices)}')