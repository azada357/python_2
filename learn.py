# ctrl + b ----->close the side bar
# ctrl + shift +  M-----> show the error and warning
# ctrl + shift + p------> step 2--> format docment----> organize codes/ another way ----> ctrl + s
# ctrl + backtick(`) -----> open the terminal
# ctrl + alt + n -----> run the code
# python implenetation---> python code----> compiler{cpython , pypy , ironpython, jython}-----> PVM, JVM....etc ----> machine code (010101)
# variable---> def: a container to store data, value, information[int, float, str, bool]
# variable naming rules:
# 1. should start with a letter (a-z, A-Z) or underscore(_)
# 2. can contain letters, digits(0-9) or underscores(_)
# 3. case sensitive
# 4. should not be a reserved keyword (if, else, for, while, def, return, import, etc..)
# string---> triple quote """ """----> long sentenses
# function def. codes already made for a espesific task ex. print(), Len(), input()...etc
# Len()---> a fnction to find the length of a string
# arugment---> the value passed to a function when calling it
# print(argument[0:n])---> to print the value of the argument passed to it
# escape notation---> a special charater used to represent certain whitespace or non-printable characters---> \n, \t, \', \", \\
# escape sequence---> \n (new line), \t (tab space), \\ (backslash), \' (single quote), \" (double quote)
# formatting strings---> 1. f" " , .format() 2.add string with + operator
# methods---> a function that is associated with an object
# string methods---> lower(), upper(), strip()/lstrip or rstrip for one side [delete space], replace(), split(), find(), count()
# numbers
# operators---> arithmetic(+,-,*,/,//,%,**), assignment(=,+=,-=,*=,/=,//=,%=,**=), comparison(==,!=,>,<,>=,<=), logical(and, or, not)
# operators precedence---> 1. parentheses() 2. exponentiation** 3. multiplication*, division/, floor division//)(No decimal), modulus%--->reminder 4. addition+, subtraction- 5. comparison(==, !=, >, <, >=, <=) 6. logical(not) 7. logical(and) 8. logical(or)
# operator in ex. print("py" in "python")---> True
# augmented assignment operators ex. x += 1 ---> x = x + 1
# funtion round()---> to round a float number to the nearest integer
# function abs()---> to get the absolute value of a number
# data types---> int, float, str, bool
# modules---> a file containing python code (functions, variables, classes) that can be imported and used in other python files
# import math---> to import the math module
# import math.sqrt()---> to import only the sqrt function from the math module
# import math.ceil()---> to import only the ceil function from the math module
# change type---> int(), float(), str(), bool()
# change type for bool()---> 0, 0.0, "", [], (), {} ----> False ; other than these ----> True
# comprison operators---> ==, !=, >, <, >=, <=
# function ord()---> to get the unicode code point of a character
# conditiional statements---> if, elif, else
# if statment : indentation (4 spaces or 1 tab)
# elif stentment: to check multiple conditions, it comes after if statment, and before else statment, Many elif can be used, INDEATATION
# else: to execute a block of code when all previous conditions are false, it comes at the end of if-elif statments, INDEATATION
# ternary operator---> value_if_true if condition else value_if_false
#short circuiting---> when the second oper and is not evaluated because the first operand determines the result of the expression
#between conditions---> and, or, not
#for loop---> to iterate over a sequence (list, tuple, string) or other iterable objects
student = "aza"
age = 19
height = 165.5
is_student = True
print(student)
print(len(student))
print(student[0:1])
print(
    f"student name is {student}, age is {age}, height is {height}, is student: {is_student}")
print(
    f"student name is {student}, age is {age}, height is {height}, is student: {is_student}.")
# x = input("x: ")
# y= int(x) +1
# print(y)
# x = input("x: ")
# y = int(x) **2
# print(y)
x = print(ord("A"))
y = ("ali" == "Aza")
print(y)
tempreture = 35
if tempreture > 30:
    print("It is hot today")
elif tempreture > 30:
    print("it is cool today")
else:
    print("it is cold today")
