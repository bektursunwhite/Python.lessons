########## 
# 
# 
# # Get user input and convert it into a list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Initialize an empty list for the reversed version
reversed_list = []

# Loop through the list in reverse order
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])  # Append elements in reverse order

# Print the reversed list
print("Reversed List:", reversed_list)