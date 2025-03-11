### Trying to count vowels in input: 

# sentence = input("Please enter a word: ")

# vowel = "aeiouAEIOU" 
# vowel_count = sum(1 for char in sentence if char in vowel)
# print(vowel_count) 

########## in this task i learnt about "sum". As i understand "sum" gives us a total of smt.. 
# Example(from ChatGpt):

# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# print(total)

# This adds 1 + 2 + 3 + 4 + 5 = 15. And the output should be 15. 


########## Let's do the same task but with a tool that we have learnt with Esen. >> 
 
# sentence = input("Please enter your word: ")

# vowel = "aeiouAEIOU"

# vowel_counter = 0
# for char in sentence:
#     if char in vowel: 
#         vowel_counter += 1
# print(vowel_counter) 

########### Now it feels familiar to me.. But smt new here is "+=".,  So "+=" will increase counter one by one.
#### Examples: counter == counter + 1 
#              counter += 1       (both options are the same)  





############# Task1. Number_Comparison. >> 

# num1 = int(input("Please enter your number: "))
# num2 = int(input("Please enter your number: "))

# if num1 == num2:
#     print("Both numbers are equal.")
# elif num1 < num2:
#     print(f"{num1} is less than {num2}")
# else:
#     print(f"{num1} is greater than {num2}") 

####### Well it worked however our tasks says next: 
####### "Task 1: Number Comparison**Write a program that takes two integer inputs and prints:

#  "Both numbers are equal"` if they are the same.
#  "The first number is greater"` if the first number is larger.
#  "The second number is greater"` if the second number is larger."  
####### Let's do everything how Esen asked..: 

# num1 = int(input("Please enter your number: "))
# num2 = int(input("Please enter your number: "))

# if num1 == num2:
#     print("Both numbers are equal")
# elif num1 > num2:
#     print("The first number is greater")
# else: 
#     print("The second number is greater") 

######## Hope everything worked as it should.. Moving further >>>




### Task2. Character type identifier. >> 

# char = input("Enter a single character: ")

# if char.isdigit():
#     print("It's a digit")
# elif char.isalpha():
#     print("It's a letter")
# else:
#     print("It's a special character")
