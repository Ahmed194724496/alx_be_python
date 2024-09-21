num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
operations = input ("Choose the operation (+, -, *, /): ")

match operations: 
    case "+":
        print(f"Result: {num1+num2}")  
    case  "-":
        print(f"Result: {num1-num2}")
    case "*":
        print(f"Result: {num1*num2}")
    case "/":
        if num2 != 0:
          print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed")
    case _:
        print("Invalid operation. Please choose one of +, -, *, /.")
