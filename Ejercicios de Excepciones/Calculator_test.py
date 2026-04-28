def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            print("Invalid operator")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

calculator()