seconds = (int(input("Enter the time in seconds: ")))
time = seconds / 60
if time > 10:
    print("greater than 10 minutes")
elif time == 10:
    print("equal to 10 minutes")
else:
    print(f"there is {600 - seconds} seconds left to reach 10 minutes")
