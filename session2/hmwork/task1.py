############# Task1. Number_Comparison. >> 

num1 = int(input("Please enter your number: "))
num2 = int(input("Please enter your number: "))

if num1 == num2:
     print("Both numbers are equal.")
elif num1 < num2:
     print(f"{num1} is less than {num2}")
else:
     print(f"{num1} is greater than {num2}") 

####### Well it worked however our tasks says next: 
####### "Task 1: Number Comparison**Write a program that takes two integer inputs and prints:

#  "Both numbers are equal"` if they are the same.
#  "The first number is greater"` if the first number is larger.
#  "The second number is greater"` if the second number is larger."  
####### Let's do everything how Esen asked..: 

num1 = int(input("Please enter your number: "))
num2 = int(input("Please enter your number: "))

if num1 == num2:
    print("Both numbers are equal")
elif num1 > num2:
    print("The first number is greater")
else: 
    print("The second number is greater") 

######## Hope everything worked as it should.. Moving further >>>