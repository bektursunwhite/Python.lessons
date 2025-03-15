##### Agenda: 


# __ dictionaries >> task based 
# __ touch functuions
# __ 

##########HOMEWORK###############

# Task 3
# Take an input of list of numbers, find and print the unique numbers.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: 1, 3, 5


students = {
    "101": {
        "name": "Alice Johnson",
        "age": 20,
        "grade": "A",
        "courses": ["Math", "Physics", "Computer Science"],
        "attendance": 95
    },
    "102": {
        "name": "Bob Smith",
        "age": 21,
        "grade": "B",
        "courses": ["History", "Literature", "Political Science"],
        "attendance": 88
    },
    "103": {
        "name": "Charlie Brown",
        "age": 19,
        "grade": "A-",
        "courses": ["Biology", "Chemistry", "Physics"],
        "attendance": 92
    },
    "104": {
        "name": "Diana Adams",
        "age": 22,
        "grade": "C+",
        "courses": ["Economics", "Statistics", "Business"],
        "attendance": 80
    },
    "105": {
        "name": "Ethan Green",
        "age": 20,
        "grade": "B+",
        "courses": ["Computer Science", "Mathematics"],
        "attendance": 90
    }
}

# task1 - that prints id and name; 
# __ 101: "Alison Jhonson"


# for key, value in students.items():
#     print(f'{key}: {value["name"]}')

# task2 - print only students that grade  are A (A-, A)

# for key, value in students.items():
#     if "A" in value["grade"]:
#         print(f'{key}: {value["name"]}')



### # task3 ---
# Ask user for an input of course
# Print the studets that are taking this course
# Input: Computer Science
# Output:
# 101: Alice Johnson
# 105: Ethan Green

# inp = input("Enter a course: ")


# for key, value in students.items():
#     if inp in value["courses"]:
#         print(f'{key}: {value["name"]}') 

# for key, value in students.items(): 
#     for element in value["courses"]: 
#         if inp == element.lower():
#             print(f'{key}: {value["name"]}')




#### What is the functions?? 

# Functions: 
# Small chunk or repeatable code which you can call multiple times in your programm: 
# DRY (Dont repeat yourself)

# How do you create a function?
# 
#  
# def <functionNAME> (): 
#         ....code



# def helloworld(): 
#     print("hello world")







# ClassTask: Create a function that takes integer as an input and tell us is it odd or even::



# def testfunction(num):
#     if num % 2 == 0: 
#         print("even")
#     else: 
#         print("odd")

# testfunction(10)
# testfunction(5)


##### ClassTask
## Create a function that takes list of integers 
## return the list of even numbers


# def myfunc(lst_int):
#     even_lst = {}
#     for i in lst_int:
#     if i % 2 == 0: 
#         even_lst.append(i)
#         return even_lst
    


def my_func(word, character):
    if character in word:
        return word.index(character)
    else:
        return "No such character"




print(my_func("aKumoSolutions", "l"))
