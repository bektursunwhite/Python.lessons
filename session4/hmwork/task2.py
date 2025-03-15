# Task 2: Remove Duplicates from a List
# Ask the user to enter multiple words separated by spaces. Store them in a list and remove duplicate words while maintaining the original order.
# Example:
# Enter words: apple banana apple cherry banana apple  
# Filtered List: ['apple', 'banana', 'cherry']


inp = input("Input: ")

lst_of_wrds = inp.split()  # -----default value 

filtered_lst = []

for word in lst_of_wrds:
    if word not in filtered_lst:
        filtered_lst.append(word)

print(filtered_lst)