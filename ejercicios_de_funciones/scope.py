
lucky_number = 123

def good_luck ():
    global lucky_number
    print (f'your default lucky number is: {lucky_number}')
    new_lucky_number = int(input("Enter your new lucky number: "))
    lucky_number = new_lucky_number
    return f"once you've modified the value on the variable using -global- your new lucky number is: {lucky_number}"  


print(good_luck())

print (f'the new value of the variable is: {lucky_number}, even outside the function, now i understand how and why using -global-')

