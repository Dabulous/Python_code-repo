
def calculate_numbers():
    
    """
    Prompt the user to input three numbers and calculate the sum, difference, product and quotient and then display the results.
    """

    # Ask the user to enter the first number
    first_number = float(input("Enter the first number: "))

    # Ask the user to enter the second number
    second_number = float(input("Enter the second number: "))

    # Ask the user to enter the third number
    third_number = float(input("Enter the third number: "))

    # Calculate the sum of the first and second numbers
    sum_result = first_number + second_number

    # Calculate the difference between the first and second numbers
    difference_result = first_number - second_number

    # Calculate the product of the first and third numbers
    multiply_result = first_number * third_number

    # Calculate the quotient of the first and second numbers
    if second_number != 0:
        quotient_result = first_number / second_number
    else:
        quotient_result = "Error: Division by zero"


    # Display the results
    print(f"Sum: {first_number} + {second_number} = {sum_result}")  # Display the sum result
    print(f"Difference: {first_number} - {second_number} = {difference_result}")  # Display the difference result
    print(f"Product: {first_number} * {third_number} = {multiply_result}")  # Display the product result
    print(f"Quotient: {first_number} / {second_number} = {quotient_result}")  # Display the quotient result
    

#This is the function which is used to call the calculate_numbers function
calculate_numbers()