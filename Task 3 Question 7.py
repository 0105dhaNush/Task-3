def find_first_non_repeating(nums):
    count_dict = {}
    
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num in nums:
        if count_dict[num] == 1:
            return num

    # If no non-repeating element is found
    return None

# Example list of integers
numbers = [3, 5, 2, 7, 5, 3, 8, 1, 2]

# Find the first non-repeating element
result = find_first_non_repeating(numbers)

# Display the result
if result is not None:
    print("The first non-repeating element is:", result)
else:
    print("No non-repeating element found.")
