# Request input from the user
number = int(input("Enter a number to see its multiplication table: "))

# Loop through numbers 1 to 10
for x in range(1, 11):
    result = x * number
    # Use f-string to print the multiplication table
    print(f"{x} * {number} = {result}")

