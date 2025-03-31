
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

#prompts the user to input the first number and second number
        operation = input("Enter an operation (+, -, *, /): ")
#prompts one to input either of the arithemetic operators

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
         print(f{num1} {operation} {num2} = {result}")
