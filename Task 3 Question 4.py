def sum_of_first_and_last_digit(number):
    # Convert the number to a string to extract digits
    num_str = str(number)
    
    # Get the first and last digits
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    
    # Calculate and return the sum
    return first_digit + last_digit

# Example usage:
user_input = int(input("Enter an integer: "))
result = sum_of_first_and_last_digit(user_input)
print("Sum of the first and last digit:", result)
