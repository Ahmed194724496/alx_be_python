<<<<<<< HEAD
num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
operations = input ("Choose the operation (+, -, *, /): ")
=======
>>>>>>> 60757a3 (Initial commit for my Python project)

# Prompt the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to choose an operation
operations = input("Choose the operation (+, -, *, /): ")

# Using match-case to perform the operation based on user input
match operations: 
    case "+":
        print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"The result is {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed")
    case _:
<<<<<<< HEAD
        print("Invalid operation. Please choose one of +, -, *, /.")
=======
          print("Invalid operation. Please choose one of +, -, *, /.")
>>>>>>> 60757a3 (Initial commit for my Python project)
