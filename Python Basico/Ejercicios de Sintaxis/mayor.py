counter = 1
big_num = 0
while counter <= 3:
    num = int(input(f"Enter number {counter}: "))
    if num > big_num:
        big_num = num
    counter += 1
else:
    print(f"The biggest number is {big_num}")
