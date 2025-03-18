
bill_amount = int(input("Please enter the bill amount: "))
tip_percentage = int(input("Please enter the tip percentage: "))
people_amount = int(input("Please enter the amount of people: "))
# tip_amount = 0
# total_amount = 0
# each_person = 0

# if tip_amount == (tip_percentage / 100) * bill_amount:
#     tip_amount =+ 1 
#     print(f"The amount of tip is {tip_amount}RUB.")
# if total_amount == bill_amount + tip_amount:
#     total_amount =+ 1 
#     print(f"The total bill is {total_amount}RUB.")
# if each_person == total_amount / people_amount:
#     print(f"The amount for each people is {each_person}RUB.")
# else: 
#     print("Invalid input..")


if bill_amount < 0 or tip_percentage < 0 or people_amount < 0: 
    print("Invalid input...")
else:  
    tip_amount = (tip_percentage / 100) * bill_amount
    total_amount = bill_amount + tip_amount
    each_person = total_amount / people_amount
    print(f"The amount of tip is {tip_amount}RUB.")
    print(f"The total bill is {total_amount}RUB.")
    print(f"The amount for each people is {each_person}RUB.")

    print("Thank you for visiting <<AIBEK>> reastaurant!!")