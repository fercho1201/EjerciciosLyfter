def get_numbers_list():
    numbers = []
    for i in range(4):
        num4list = (int(input('Type a number: ')))
        numbers.append(num4list)
    return numbers


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


numbers = get_numbers_list()

list_prime = []
for i in (numbers):
    if is_prime(i):
        list_prime.append(i)


print ("the list of numbers you'd entered is:", numbers)
print ('And the prime numbers on your list is:', list_prime)
