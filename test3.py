def calculate_numbers():
    # Ask the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum, difference, and quotient
    sum_result = num1 + num2
    difference_result = num1 - num2
    quotient_result = num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed"

    # Print the results
    print(f"Sum: {num1} + {num2} = {sum_result}")
    print(f"Difference: {num1} - {num2} = {difference_result}")
    print(f"Quotient: {num1} / {num2} = {quotient_result}")

calculate_numbers()