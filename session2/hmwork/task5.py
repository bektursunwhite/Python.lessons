#### Task number 5. Checking even/odd numbers.. >>

number = int(input("Please enter a number/digit: "))

if number > 0:
    if number % 2 == 0:
        print("Positive even.")
    else:
        print("Positive odd.")
elif number < 0: 
    if number % 2 == 0:
        print("Negative even.") 
    else:
        print("Negative odd")

else:
    print("This number is 0.")

###################### OR 

number = int(input("Please enter a number/digit: "))

if number > 0:
    if number % 2 == 0:
        print(f"{number} is positive even.")
    else:
        print(f"{number} is positive odd.")
elif number < 0: 
    if number % 2 == 0:
        print(f"{number} is negative even.") 
    else:
        print(f"{number} is negative odd")

else:
    print("This number is 0.")
