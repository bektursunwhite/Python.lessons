######## The task: We should find the largest number from 3 inputs.. Using "if, elif, else" conditions >>

num1 = input(int("Please enter your first number: "))
num2 = input(int("Please enter your second number: "))
num3 = input(int("Please enter your third numbre: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")

################### The wrong one


#### Second attepmt:
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
num3 = int(input("Please enter your third numbre: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")

####### OR

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
num3 = int(input("Please enter your third numbre: "))

if num1 >= num2 and num1 >= num3:
    print("The largest number is first input.")
elif num2 >= num1 and num2 >= num3:
    print("The largest number is second input.")
else:
    print("The largest number is third input.")