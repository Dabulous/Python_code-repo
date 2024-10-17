def calculate_numbers():
    # Prompt the user to input three numbers
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    third_number = float(input("Enter the third number: "))
    
    # Perform arithmetic operations
    sum_result = first_number + second_number
    difference_result = first_number - second_number
    multiply_result = first_number * third_number
    quotient_result = first_number / second_number if second_number != 0 else "Error: Division by zero"

    # Display the results
    print(f"Sum: {first_number} + {second_number} = {sum_result}")
    print(f"Difference: {first_number} - {second_number} = {difference_result}")
    print(f"Product: {first_number} * {third_number} = {multiply_result}")
    print(f"Quotient: {first_number} / {second_number} = {quotient_result}")


calculate_numbers()