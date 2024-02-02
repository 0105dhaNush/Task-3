def find_duplicates(list1, list2, list3):
    common_elements = set(list1) & set(list2) & set(list3)
    return list(common_elements)

# Example lists
list1 = [11, 12, 13, 14, 15, 16]
list2 = [14, 15, 16, 17, 18]
list3 = [16, 17, 18, 19, 20]

# Find duplicates
duplicates = find_duplicates(list1, list2, list3)

# Display the result
if duplicates:
    print("Duplicates found:", duplicates)
else:
    print("No duplicates found.")
