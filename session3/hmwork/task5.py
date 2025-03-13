######## Trying to build pyramid from input >>>>>>

word = input("Enter a word: ")

# Loop to print the pattern
for i in range(1, len(word) + 1):
    print(word[:i])  # Print substring from index 0 to i
