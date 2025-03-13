#### Task number 4. Password checker... >> 

password = input("Please eneter your password: ")

if len(password) >= 8 and any(char.isdigit() for char  in password) and any(char.isalpha() for char in password):
    print("This is a strong password.")
else:
    print("This is a weak password.") 

################# Should practice more -> <<isdigit, isalpha, len(input)>>