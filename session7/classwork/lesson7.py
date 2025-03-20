### Agenda... 

# for else and while else
# functions
# recursive functions
# exceptions / error handling
# exeptions classes

#---------------------

# for char in "Hello": 
#     print(char)
#     if char == "l":
#         break
# else: 
#     print("End")

# --------------------


# --------------
# functions
# --> starts with keyword def nameOFfunction(argument1, arg1, arg1)
# --> repetitive code


# def numberchecker(number=2, lst=[1, 2, 3, 4, 5]):
#     if number in lst: 
#         return True
#     else: 
#         return False
    
# print(numberchecker)




# factorial ---> 

# def factorial(n):
#     if n == 1:  # breaking point
#         return 1
#     return n * factorial(n - 1)  # call yourself once again


# # factorial of 5
# # n = 5

# # 5 * 4 * 3 * 2 * 1

# # factorial(4) == 4 * 3 * 2 * 1
# # n = 4
# # 4 * factorial(3)

# # factorial(3)
# # n = 3
# # 3 * 2 * 1


# # factorial(2)
# # n = 2
# # 2 * 1

# # factorial(1) == 1
# # return 1

# print(factorial(5))  # 5 * 4 * 3 * 2 * 1 == 120






### fibonacci sequence




# lst = [1, 2, 3, 4, 5]
# for i in range(1, len(lst) + 1):
#     print(lst[i])
# else: 
#     print("Out of list")






# students_data = {
#     "Alice": 95,
#     "Bob": 88,
#     "Charlie": 92,
#     "Diana": 80,
#     "Ethan": 90,
# }

# inp = input("Please provide the student name: ")
# try: 
#     score = students_data[inp]
#     print(f"{inp}'s score is {students_data}") 
# except: BaseException
# print(f"There is no students like {inp}")
# try:
#     a = int(input("input: "))
#     print(a)

# except:
#     print("sorry error")





# lst = ["alice", "bob", "charlie"]


# try: 
#     int(index)