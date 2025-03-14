### Agenda 
# Learn List index(), split()
# LIst comprehensions
# Tuples
# Difference between mutable and immutable data types 
# Intro to dictionaties


# hmtask2 
# inp = input("Input: ")

# lst_of_wrds = inp.split()  # -----default value 

# filtered_lst = []

# for word in lst_of_wrds:
#     if word not in filtered_lst:
#         filtered_lst.append(word)

# print(filtered_lst)

# hmtask4 
# create max_number
# create second_max 

# run for loop in list 
# if condition  >>>>> this should find max number i > max >>>> max = i 
# elif condition >>>> this should find second max number i > second_max and second_max < max_num



# lst = ["Hello", 1, 10, True]

# print(lst.index(1))

# List Comprehensions >> generate a list of elements using a single line:
# Create me a list of even number till 10; 

# lst = []
# for num in range(1, 11):
#     if num % 2 == 0: 
#         lst.append(num)
# print(lst)

# what is the syntax?
# variable = [element | for element in sequence]
# lst_num = [i for i in range(1, 21)]
# print(lst_num)


# "aKumosolutions" >>>> ['a', 'k', ...]
# lst = [char for char in "aKumosolutions"]
# print(lst) 

# lst = []
# for i in range(1, 11):
#     if i % 2 == 0: 
#         lst.append(i)
# print(lst)


# num = int(input("Enter a number: "))
# sq = num ** 2
# print(sq)

 
# lst_num = [num*num for num in range(1, 11)] 
# print(lst_num)






# What is mutable and what is immutable? 
# mutable ----> mutate 
# mutable data type is constatly changes
# list ---> mutable ----> append, sort, remove, pop 
# string ----> immutable -----> string cannot be change

# lst = [1, 2, 3, 4, 5]       |
# lst[2] = 10                 |---------------> mutable
# print(lst)                  |


# string = "hello"              |
# string = "heelo"              |-----------------> immutable
# print(string)                 |






# Tuple
# Tuple is the immutable version of list; 

# tpl = 1, 2, True, 10.10, "Hello"

# print(tpl)
# print(type(tpl))
 # With tuple we can write without ()


# tpl = list((1, 2, True, 10.10, "Hello"))

# tpl[3] = 100
# tpl.append(10)
# print(tpl)


# lst.sort()
# tpl = (1, 0, -10, 8, 7)

# ans = sorted(tpl)
# print(tuple(ans))

# tpl = (i for i in range(1, 10))
# print(tuple(tpl))


# Intro to dictionary 

# string -----> 1 key and 1 value 
# int ------> 2 key nad 2 value
# list -------> 1 key and multiple values
# tuple ------> 1 kay and multiple values 

# dictionary -> multiple keys and multiple values

# Dictionary must be unique >>> only one key per value; 

# jan_class = {

#     "beka": "prius",
#     "iana": "cake",
#     "erkin": "coffee",
#     "kostya": "massage",
#     "aibek": "english teacher",
#     "aigerim": "ten years",
#     "cuneyt": "nerd",
#     "jykdyz": "uni student",
#     "gulnaz": "roses",
# }

# for element in jan_class.values:     # or keys or items; 

#     print(element)

# ############ OR 

#     print((jan_class.items))


# #print(jan_class)



# python_class = { 
#     1: {"firs_name": "Bektursun", "word": "Handsome", "phone_number": "2066102366"},
#     2: {"first_name": "Yana", "word": "cake", "phone_number": "2342278364"},
#     3: {"first_name": "aibek", "word": "teacher", "phone_number": "24253536"},
#     4: {"first_name": "kostya", "word": "masssage", "phone_number": "235343553"},
#     5: {"first_name": "erkin", "word": "coffee", "phone_number": "252345523"}, 
# }