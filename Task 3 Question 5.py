def distribute_mangoes(mango_bags, students):
    # Sort the list of mango bags in ascending order
    sorted_bags = sorted(mango_bags)
    
    # Calculate the number of bags each student will get
    bags_per_student = len(mango_bags) // students
    
    # Calculate the remaining bags that need to be distributed among the students
    remaining_bags = len(mango_bags) % students
    
    # Initialize variables for tracking the minimum difference and the last bag distributed
    min_difference = float('inf')
    last_bag = 0
    
    # Iterate through each student and distribute the bags
    for i in range(students):
        # Calculate the range of bags for the current student
        start_index = i * bags_per_student + min(i, remaining_bags)
        end_index = start_index + bags_per_student + (1 if i < remaining_bags else 0)
        
        # Calculate the difference between the maximum and minimum mangoes in the current range
        difference = sorted_bags[end_index - 1] - sorted_bags[start_index]
        
        # Update the minimum difference if the current range has a smaller difference
        if difference < min_difference:
            min_difference = difference
            last_bag = end_index
    
    # Return the bags for each student
    return sorted_bags[:last_bag], sorted_bags[last_bag:]

# Example usage:
mango_bags = [10, 5, 8, 15, 20]
students = 3
result = distribute_mangoes(mango_bags, students)

print("Bags for each student:", result[0])
print("Remaining bags:", result[1])
