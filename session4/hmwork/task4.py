###### Task4. 



numbers = list(map(int, input("Enter numbers: ").split()))

# Initialize max_number and second_max
max_number = float('-inf')
second_max = float('-inf')

# Loop through the list to find the max and second max
for i in numbers:
    if i > max_number:  # If current number is greater than max_number, update both
        second_max = max_number
        max_number = i
    elif i > second_max and i < max_number:  # If greater than second_max but less than max_number, update second_max
        second_max = i

# Check if we found a valid second largest number
if second_max == float('-inf'):
    print("No second largest number found.")
else:
    print("Second largest number:", second_max)
