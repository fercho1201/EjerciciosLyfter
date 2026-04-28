def calcularor(a):
    current_number = float(a)
    while True:
        menu = input("Please select an option: "
                    "1. Addition "
                    "2. Subtraction "
                    "3. Multiplication "
                    "4. Division "
                    "5. Clear result: "
                    "6. Exit: ")
        if menu in ["1", "2", "3", "4"]:
            try:
                b= float(input("Enter the second number: ")) 
                if menu == "1":
                    menu = "+"
                    result = current_number + b
                elif menu == "2":
                    menu = "-"
                    result = current_number - b
                elif menu == "3":
                    menu = "*"
                    result = current_number * b
                elif menu == "4":
                    if b == 0:
                        raise ZeroDivisionError("You cannot divide by zero.")
                    menu = "/"
                    result = current_number / b
            except ZeroDivisionError:
                print("Error: You cannot divide by zero.")
                continue
            except TypeError:
                print("Error: Both inputs must be numbers.")
                continue
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue
            print(f"The result of {current_number} {menu} {b} is: {result}")
            current_number = result    
            continue 
        elif menu == "5":
            current_number = 0
            print("Result cleared. ---- The value of the current number is now: ", current_number) 
            continue           
        elif menu == "6":
            print("Exiting the calculator....")
            break
        elif menu not in "123456":
            print("Error: --Invalid Operator-- Please select a valid option from the menu."  )
            continue
            break


a = 100
calcularor(a)
