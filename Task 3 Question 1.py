original_list = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = [num for num in original_list if num % 2 == 0]
odd_numbers = [num for num in original_list if num % 2 != 0]

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
