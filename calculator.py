def calculator():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")
    
    try:
        # Take input from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        # Perform operation
        if operation == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid operation selected.")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator
calculator()
