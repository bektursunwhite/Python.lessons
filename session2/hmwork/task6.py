#### Task number 6. Age classifier.. >>>

age = int(input("Please enter your age: "))

if 0 <= age <= 12: 
    print("Child")
elif 13 <= age <= 19: 
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")
elif 60 <= age: 
    print("Senior Citizen")
else: 
    print("Invalid Input")

############################### 