# from math import *

# print("Helllo world")

# ----------string----------------
# name = "sumit"
# name1 = "rahul"
# age = 35
# print("hello " + name)
# print(name.upper())
# print(name.lower().isupper())
# print(name.index("i"))
# print(len(name))
# print(name.replace('u','m'))

# -------------Number--------------------
nubmer = 89
# nubmer2 = str(nubmer)
# print(nubmer+8.897)
# print(nubmer*8)
# print(20%3)
# print(nubmer2+"56")
# print(max(4,8,9,10,56,78))
# print(min(4,8,0,89,1))
# print(round(6.34))
# print(bin(2))

# print(sqrt(5))
# print(pow(2,4))

#------Input-----

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print("My name is " + name + " and my age is " , age)

#---------List--------
# countries = ['india','nepal','america','russia']
# countries2 = list(('sumit',21,True))
# print(countries)
# print(countries[1])
# print(countries[-2])
# print(countries[1:])
# print(countries[1:3])
# print(type(countries2))

# print(len(countries))

#-------List method------------
# list1 = [1,2,7,9,5]
# list2 = ['banana','apples','mango','apples','oranges',"grapes"]
# list3 = list2.copy()

# list1.extend(list2)
# list2.append('cheery')
# list2.insert(1,'cheery')
# list2.remove('apples')
# list2.clear()
# list1.sort()
# list2.reverse()
# list2.pop()
# list2.pop(1)

# del list2[2]

# print(list2)
# print(list2.index("mango"))
# print(list2.count('apples'))

#------------Tuples------------
# three_number = (1,2,3,8)

# print(type(three_number))

#-----------Function---------
# def greeting_function(*names):
#     print("hello "+str(names[3]))
# def greeting_function1(name, age):
#     print("hello "+name+ " and your age is " + str(age))

# greeting_function()
# greeting_function("sumit","Rahul","Tom",78)
# greeting_function1(name = "sumit" , age = "21")

# def add(num1 , num2):
#     return num1+num2
# def subtract(num1 , num2):
#     return (num1-num2)
# def divide(num1 , num2):
#     return num1/num2

# numb1 = int(input("enter number 1:"))
# numb2 = int(input("enter number 2:"))

# print(add(numb1 ,numb2))
# print(subtract(numb1 , numb2))
# print(divide(numb1 , numb2))

# a = 5
# b = 8

# if a > b or b > a:
#     print("a is greater than between")
# elif b == a:
#     print(" b is greater")
# else: 
#     print("both are false")

#------ Dictionaries---------------

# my_dict = {
#     'name': 'sumit',
#     'nationality': 'indian',
#     'age': 21,
#     'qualification': 'undergraduate',
#     'friends': ['utkarsh' , 'rahul' , 'ankit']
# }

# x = my_dict['name']

# print(x)
# print(my_dict['name'])
# print(my_dict['friends'])

#--------Loops--------------------

# i = 1
# j = 1
# while i < 10 and j < 5:
#     print(i)
#     i += 1
#     j += 1

my_list = ['tim' , 'tom' , 'knk' ,'covk']

# for letter in "Hello":
#     print(letter) 

# for x in my_list:
#     print(x)
#     if x == 'knk':
#         break

# for x in range(1 , 9):
# for x in range(9):
#     print(x)

#-------------2D List----------------
'''
myList = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(myList)
for row in myList:
    for col in row:
        print(col)



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter Operator:")

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Not valid operator")


# ---------------- Try and Except---------------------
try:
    x = int(input('Input an integer: '))
    print(x)
except ValueError:
    print("Not a integer")
finally:
    print('try except finished')



# ------------------ File reading and writing--------------

# coun_file = open("countries.txt", 'r')

#------------ Reading file
# print(coun_file.readable())
# print(coun_file.readline())
# print(coun_file.readlines())
# print(coun_file.readlines()[3])

# for lines in coun_file.readlines():
#     print(lines)

# coun_file.close()

# coun_file = open("countries.txt", 'w') for writing
coun_file = open("countries.txt", 'a') # for append new text
coun_file = open("Newpython.py", 'w') 
coun_file.write("print(\'This is new file \')")


#-------------class and object-----------

# class Person:
#     def __init__(self , name ,age):
#         self.name = name
#         self.age = age
        
# p1 = Person("sumit" , 21)
# print(p1.name)

#-------------Inheritewnce-------------------

from Newpython import Student

class Person(Student):
    pass

p1 = Person()
print(p1.name)

'''

 