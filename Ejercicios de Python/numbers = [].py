numbers = []
try:
    count = int(input("How many numbers? "))  

    for i in range(count):
        num = int(input("Enter a number: "))
        numbers.append(num)

    average = sum(numbers) / len(numbers)

except (ValueError,  NameError):
    print("Invalid input. Please enter an integer.")

except ZeroDivisionError:
    print("No numbers were entered to calculate the average.")
else :
    print("The average is:", average)
