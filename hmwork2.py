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

#### I should practice more <<isdigit, isalpha, isalnum, islower, isupper and isspace>> 
# 
# 
######## The task: We should find the largest number from 3 inputs.. Using "if, elif, else" conditions >>

# num1 = input(int("Please enter your first number: "))
# num2 = input(int("Please enter your second number: "))
# num3 = input(int("Please enter your third numbre: "))

# if num1 >= num2 and num1 >= num3:
#     print(f"The largest number is {num1}")
# elif num2 >= num1 and num2 >= num3:
#     print(f"The largest number is {num2}")
# else:
#     print(f"The largest number is {num3}")
################### The wrong one


#### Second attepmt:
# num1 = int(input("Please enter your first number: "))
# num2 = int(input("Please enter your second number: "))
# num3 = int(input("Please enter your third numbre: "))

# if num1 >= num2 and num1 >= num3:
#     print(f"The largest number is {num1}")
# elif num2 >= num1 and num2 >= num3:
#     print(f"The largest number is {num2}")
# else:
#     print(f"The largest number is {num3}")

####### OR

# num1 = int(input("Please enter your first number: "))
# num2 = int(input("Please enter your second number: "))
# num3 = int(input("Please enter your third numbre: "))

# if num1 >= num2 and num1 >= num3:
#     print("The largest number is first input.")
# elif num2 >= num1 and num2 >= num3:
#     print("The largest number is second input.")
# else:
#     print("The largest number is third input.")



#### Task number 4. Password checker... >> 

# password = input("Please eneter your password: ")

# if len(password) >= 8 and any(char.isdigit() for char  in password) and any(char.isalpha() for char in password):
#     print("This is a strong password.")
# else:
#     print("This is a weak password.") 

################# Should practice more -> <<isdigit, isalpha, len(input)>>


#### Task number 5. Checking even/odd numbers.. >>

# number = int(input("Please enter a number/digit: "))

# if number > 0:
#     if number % 2 == 0:
#         print("Positive even.")
#     else:
#         print("Positive odd.")
# elif number < 0: 
#     if number % 2 == 0:
#         print("Negative even.") 
#     else:
#         print("Negative odd")

# else:
#     print("This number is 0.")

###################### OR 

# number = int(input("Please enter a number/digit: "))

# if number > 0:
#     if number % 2 == 0:
#         print(f"{number} is positive even.")
#     else:
#         print(f"{number} is positive odd.")
# elif number < 0: 
#     if number % 2 == 0:
#         print(f"{number} is negative even.") 
#     else:
#         print(f"{number} is negative odd")

# else:
#     print("This number is 0.")





#### Task number 6. Age classifier.. >>>

# age = int(input("Please enter your age: "))

# if 0 <= age <= 12: 
#     print("Child")
# elif 13 <= age <= 19: 
#     print("Teenager")
# elif 20 <= age <= 59:
#     print("Adult")
# elif 60 <= age: 
#     print("Senior Citizen")
# else: 
#     print("Invalid Input")

############################### 