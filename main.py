# a, b, c = "x", "y", "z";

# print(a);
# print(b);
# print(c);

########################################################################################################################

# All variables are defined same values

# a = b = c = "x", "y", "z";

# print(a);
# # print(b);
# print(c);

########################################################################################################################

# names = ['a', 'b', 'c']

# a, b, c = names;


# print(a, c );
# # print(b);
# print(a + c);


# function and global variables

# def morFun ():
#   global x, y
#   x = 4;
#   y = 5 - 2;

#   print("1st global value is:", x + y);
# morFun();

# print( "2nd global value is:", x + y +1);


################################################################################################################

# function

# def fun(a, b, c):
#   print("1st factory fun value is :", a + b + c);
# fun(1, 2, 3);


# def fun(a, b, c):
#   print("2nd factory fun value is :", a + b + c);
# fun(3, 4, 6);


#######################################################################################################################

# import random

# print(random.randrange(1,9))


# ###################################################################################################################################################


# txt = "My name is Main";
# if "My" in txt:
#   print("my my");
# print("Main" in txt);


# ###############################################################################################################################################
# I will learn it by Subin vai

# class myclass():
#   def __len__(self):
#     return 0
# myobj = myclass()
# print(bool(myobj))

# x = 1
# y = 2
# if not (x == 3 or y == 4):
#     print("x = y")
# else:
#     print("x is not equal to y")
#
# x = 5
# y = 1
# if not (x == y):
#     print("aaa")
# else:
#     print("x is not equal to y")
#
# x = 5
# y = 1
# if x is not y:
#     print("bbb")
# else:
#     print("x is not equal to y")

# x = 2
# y = 3
#
# # x = [1, 2, 3]
# # y = [1, 2, 3]
#
# print(x is not y)
# print(not (x == y))


# ##############################################################################################################################################

# array listing

# x = [1, 2, 3, 4, 5, 6]
# print(x[-1]);
# print(x[2:4]);
# print(x[2:]);
# print(x[:3]);
# x[2] = 5
# print("Chenge", x)
# x[2:3] = [5,7];
# print("Chenge 2", x);

# x.insert(2, "aaa");
# print("insert", x);

# x.append("bbb")
# print("append", x)

# x.extend(["ccc", "ddd"]);
# print("extend", x);

# x.pop();
# print("pop 1", x);

# x.pop(2);
# print("pop 2", x);

# x.remove(3);
# print("remove", x);


# x.pop();
# print("pop 0", x);

# x.clear();
# print("clear", x);

# for i in x:
#   print("for 1", i);

# for i in range(len(x)):
#   print("for 2", x[i]);
#   print("for index", i);


# i =0;
# while i < len(x):
#   print(x[i]);
#   i=i+1;


# subArray = [];
# for i in x:
#  if i == 2:
#    subArray.append(i);
#    print(f"list is {subArray}")
#    break;


###############################################################################################
# lowercase to uppercase
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"];
# print([x.upper() for x in fruits]);


#################################################################################

# Tuples

# tuples = ("main", "Sazzad", "Mijan", "marjan", "koli", 9)
# print("tuples 1", tuples)
# print("tuples 2", tuples[5] + 1);

# for i in range(len(tuples)):
#   print("tuples 3", i);

# if "Mi" in tuples:
#   print("tuples 4");
# else:
#   print("tuples 4", "not found");

# updateTuples = list(tuples)
# updateTuples[1] = "Zamia"
# print("update", updateTuples)

# ############################################################################

# sets = {"main", "Mijan", "Marjan"}
# sets.add("Zamia")
# print("sets", sets)
# sets2 = ['Marjan', 'main', 'c', 'd', 'e', 'f']
# sets3 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# sets4 = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
# sets5 = {"l", "m", "n", "o", "p", "q", "r", "s", "t"}
# sets6 = {"u", "v", "w", "x", "y", "z"}
# sets.update(sets2, sets3)
# print('set update', sets)

# sets = {1,2,3,4,5}
# print(sets)

# for i in sets:
#     print("for 1", i)

# for i in range(len(sets)):
#     print("for 2", i)


# ##############################################################################################

# Sets

# obb = {
#     "name": "main",
#     "age": 20,
#     "hobbis": ["codeing", "Learning", "thinking"],
#     "family": [
#         {
#             "name": "mijan"
#         },
#         {
#             "name": "marjan"
#         }
#     ],
# }
#
# # c = [
# #     {
# #         "name": "main",
# #     }
# # ]
#
# obb["sub"] = [
#     {
#         "class": "One",
#         "sub": "en"
#     }
# ]
#
# # we can update it like array
#
# print(obb)
# print(obb["hobbis"][0])
# print(obb["family"][1]["name"])
# print(obb.get("family"))


# ##############################################################################################

# While loop

# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break


# ################################################################################################
# for loop

# for i in range(5):
#     print(i)

# for i in range(5, 10):
#     print(i)
#
# for i in range(1, 20, 2):
#     print(i)


# ################################################################################################

# function


def myFun():
    print("hi")


myFun()

# def myFun1(*x):
#     print(x[1])
#
#
# myFun1('a', 'b', 'c')

# def myfun(*x):
#     print(x[0])
#
#
# myfun("a", "b", "c")


# def myfun(**x):
#     print(x["b"])
#
#
# myfun(a="a", b="b")


# def myfun(a, b, c):
#     print(a, b)
#
#
# myfun(a="a", b="b", c="c")


# def myfun(cun="NO"):
#     print("I an from", cun)
#
#
# myfun(cun="USA")
# myfun()


# add array in function
# lists = ["a", "b", "c", "d"]
# lists = [
#     {
#         "name": "main"
#     },
#     {
#         "name": "Zamia"
#     }
# ]
#
#
# def myfun(arr):
#     for i in range(len(arr)):
#         print(lists[i]["name"])
#
#
# myfun(arr=lists)


# def myFun(a, b):
#     return a + b
#
#
# x = myFun(4, 6)
# print(x)


# ############################################################################################################
# for Fun

# import psutil
#
# # import os
#
# # Get CPU usage
# cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage for the last second
# print("CPU Usage:", cpu_usage)
#
# # Get memory usage
# memory = psutil.virtual_memory()
# total_memory = memory.total / (1024 * 1024)  # Convert to MB
# available_memory = memory.available / (1024 * 1024)  # Convert to MB
# used_memory = memory.used / (1024 * 1024)  # Convert to MB
# print("Total Memory:", total_memory, "MB")
# print("Available Memory:", available_memory, "MB")
# print("Used Memory:", used_memory, "MB")
#
# # os.system("shutdown /r /t 1")


# ######################################################################################################

# x = lambda a, b: a * b
# print(x(2, 3))

# def myfun(a):
#     return lambda x, y: x + y + a
#
#
# z = myfun(1)
# print(z(2,3))


# ######################################################################################################

# classes and object

# class Profile:
#     x = 1
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def myfun(self):
#         return f'{self.name} {self.age}'
#
#
# a = Profile("John", 36)
# # del a.age
# print(a.myfun())
# print(a.age)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
# p1.myfunc()


# class Profile2:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def information(self, gen):
#         text = f"Hi, my name is {self.name}. I am {self.age}, I am {gen}"
#         return text
#
# zamia = Profile2("Zamia", "21")
# print(zamia.information("femail"))


# class ProfileData:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def profile(self):
#         return f"name is {self.name}. age is {self.age}"
#
#
# class SubProfileData(ProfileData):
#     def __init__(self, name, age, sex):
#         # super.__init__(name, age)
#         super().__init__(name, age)  # inport from top class value
#         self.sex = sex
#
#     def subprofile(self):
#         return f"my name is {self.name}. i am {self.age} years old. my gender is {self.sex}"
#
#
# main = ProfileData("main", 22)
# print(main.profile())
#
# main2 = SubProfileData("main", 24, "male")
# print(main2.subprofile())

####################################################################################################

# I was learned iteration, but it's like for loop. for loop will be best
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))

# print(next(myit))
# print(next(myit))


###################################################################################


# import file1
#
# file1.myFunImp()
# print(file1.myDATA[0]['name'])


# ###############################################################################

# math

# import math
#
# x = math.pi
# print(x)
#
# x = [1, 2, 3]
# print(max(x))


# ################################################################################

# json
#
# import json
#
# # jsonData = '{"name": "Zamia", "age":"22"}'
# # toJson = json.loads(jsonData)
# # print(toJson)
#
# jsonData = {
#     "name": "Main",
#     "age": 22,
#     "hobby": [
#         {"play": ["main", "age"]}
#     ]
# }
# x = json.dumps(jsonData)
# print(x)
# print(jsonData)


# ############################################################|\\\\

# try except

# aro bujte hobe

# x = 2
# try:
#     print(x)
# except:
#     print("sorry")
# else:
#     print("so sorry")
# finally:
#     print("thank you")


###################################################################

# input

# x = int(input("Enter your input: "))

# for i in range(x):
#     print(i)
# for i in x:
#     print(i)
# print(x)


# since = int(input("Form: "))
# to = int(input("to: "))
#
# for since in range(since, to + 1):
#     print(f'{since} gorar namta')
#     for multiplyNumb in range(1, 10):
#         print(f"{since} * {multiplyNumb} = ", since * multiplyNumb)


# f = open("x.txt")
# print(f.read())


# ############################################################
# ATM Project

# pin = 1245
# balance = 2000
#
#
# def atm():
#     print("wellcome to EBL")
#     while True:
#         inpPin = int(input("Enter your PIN: "))
#         if inpPin == pin:
#             print("1. Check Balance")
#             print("2. Withdraw Money")
#             print("3. Deposit Money")
#             print("4. Change PIN")
#             print("5. Exit")
#
#             choose = int(input("Choose on"))
#             if choose == 1:
#                 print(f"Your balance is {balance}")
#             elif choose == 2:
#                 WithdrawAmount = float(input("Enter your amount to withdraw : "))
#                 if WithdrawAmount > balance:
#                     print(f"Insufficient Balance")
#
#
# atm()


# def atm():
#     pin = 1234
#     amount = 1000
#     print(f'Welcome to EBL')
#     inpPin = int(input("please enter your pin : "))
#     if pin == inpPin:
#         print("1. Check Balance")
#         print("2. Withdraw Money")
#         print("3. Deposit Money")
#         print("4. Change PIN")
#         print("5. Exit")
#         while True:
#             chooseNum = int(input(f"choose on : "))
#             if chooseNum == 1:
#                 print(f"your amount is {amount}")
#             if chooseNum == 2:
#                 WithdrawAmount = int(input(f"please enter your Withdraw amount : "))
#                 if WithdrawAmount > amount:
#                     print(f"your amount is less then {WithdrawAmount}. your amount is {amount}")
#                 elif WithdrawAmount < amount:
#                     amount -= WithdrawAmount
#                     print(f"you are withdraw {WithdrawAmount}\nnow your balance is {amount}")
#             if chooseNum == 3:
#                 depoAmount = float(input("Please enter deposit amount : "))
#                 amount += depoAmount
#                 print(f"Your deposit amount is {depoAmount}.\nNow your balance is {amount}")
#             if chooseNum == 4:
#                 newPin = int(input("Please Enter your new PIN : "))
#                 conPin = int(input("Confirm PIN : "))
#                 if newPin == conPin:
#                     pin = newPin
#                     print(f"Now your new PIN is {pin}")
#                 else:
#                     print(f"PIN doesn't match. please try again")
#             if chooseNum == 5:
#                 print(f"Thanks for using EBL")
#                 # atm()
#                 break
#     else:
#         print("incorrect PIN")
#
#
# atm()

# infinity input
# x = list(open(0))
# print(x)


# my_list = []
#
# for i in range(5):
#     x = input()
#     my_list.append(x)
# print(my_list)


# aye inp konodin ses hobe na
# my_list = []
#
# while True:
#     x = input()
#     my_list.append(x)
#
# print(my_list)


# my_list = []
#
# while input("More y/n") == 'y':
#     x = input()
#     my_list.append(x)
#
# print(my_list)


# convert from str to int
# x = "1 2 3 4 5 6"
# y = x.split()
#
# for i in range(len(y)):
#     print(type(int(y[i])))


# runing_total = 0
#
# while True:
#     n = input("inp is : ")
#     if n == 'q':
#         break
#
#     n = int(n)
#     runing_total += n
#
#     if n == 'q':
#         break
#     print(runing_total)


# ####################################################################
# name = "main"
# print(name[0])

# ###################################################################################
# find id
# n = 5
# print(id(n))
# print(id(n))

# for i in range(10):
#     # print(i)
#     for j in range( i+ 1):
#         print(j , end=" ")
#     print(" ")


# rows = 6
# for i in range(rows):
#     for j in range(i):
#         print(i, end=' ')
#     print('')


# li = [1, 2, 3, 4]
# # li[1: 2] = 5, 6, 7
# li[1:2] = [5, 6, 7]
# print(li)


# object like as a dictionary

# obb = [
#     {
#         "name": "zamia",
#         "age": 22,
#         "hobby": [
#             {"play": ["main", "age"]}
#         ],
#         "hobb": [
#             {
#                 "play": ["main", "age"]
#             }
#         ]
#     },
#     {
#         "name": "main",
#         "age": 22,
#         "hobby": [
#             {"play": ["main", "age"]}
#         ],
#         "hobb": [
#             {
#                 "play": ["main", "age"]}
#             ]
#     }
# ]

# print(obb[0]["name"])


# myList = []
# while True:
#     s = input("enter value: ")
#     myList.append(s)
#     if s == "q":
#         break
# print(myList)


# find max number without a builting function

# li = [2, 3, 4, 5, 6, 7, 8, 9, 8, 5, 6, 71, 2, 3, 44, 55, 66, 77]

# max_num = float('-inf')
# for i in li:
#     if i > max_num:
#         max_num = i
# print(max_num)

################################

# min_num = float('inf')
# for i in li:
#     if i < min_num:
#         min_num = i
# print(min_num)

########################

# sum = 0
# for i in li:
#     sum = sum + i
# print('sum', sum)

#####################

# for i in li:
#     if i == 6:
#         print(True)
#         break


# lenier scherch

# li1 = [1, 4, 5, 7, 8]
#
# key = 6
# flag = False
# for i in li1:
#     if i == key:
#         flag = True
#         print(flag)
# if flag == False:
#     print(flag)


# file write and read
# a for create new file and write anything
import os

# f = open('y.txt', 'a')
# f.write("jhfdsagnsrduihng")
# f.close()
#
# f = open("y.txt")
# print(f.read())

# if os.path.exists('y.txt'):
#     os.remove("y.txt")
# else:
#     print("sorry")

# with open("x.txt") as file1:
#     read_content = file1.read()
#     print(read_content)
with open("x.txt") as file:
    for line in file:
        print(line.strip())

################################################
# import file1
# print('name is', file1.myDATA[1]["name"])

###############################################

# class PersonData:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def profile(self, gen):
#         return f"name is {self.name}. age is {self.age}, gender is {gen}"


# class PersinData2(PersonData):
#     def __init__(self, name, age, cls, role):
#         super().__init__(name, age)
#         self.cls = cls
#         self.role = role

#     def profile2nd(self, gen):
#         return f"name is {self.name} age is {self.age} class is {self.cls} role is {self.role}, gen is {gen}"


# zamia = PersonData("zamia", 22)
# print(zamia.profile("F"))

# zamia = PersinData2("zamia", 22, "Two", 10)
# print(zamia.profile2nd("f"))
#
# import uuid25
# print("uuid is", uuid25.gen_v4())


# class Shop:
#     cart = []
#
#     def __init__(self, buyer):
#         self.buyer = buyer
#
#     def add_cart(self, item):
#         self.cart.append(item)
#
#
# p1 = Shop('Rohim')
# p1.add_cart('Phone')
# p1.add_cart('Watch')
# print(p1.cart)
# p2 = Shop('Korim')
# p2.add_cart('Shoe')


########################################################

# def get_even_number(numbers):
#     evenNumber = [i for i in numbers if i % 2 == 0]
#     return evenNumber
#     # for i in numbers:
#     #     if i % 2 == 0:
#     #         print(i)
#
#
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# print(get_even_number(list1))


# duble number

# x = [1, 2, 3, 4, 5, 6, 7]

# d_number = list(map(lambda num: num * 2, x))
#
# print(d_number)


# def duble_number(num):
#     for i in range(len(num)):
#         print(num[i]*2)
#
#
# duble_number(x)


####################################


# def contains_vowel(string):
#     vowels = "aeiouAEIOU"
#     for char in string:
#         if char in vowels:
#             return True
#     return False
#
#
# # Input from user
# input_string = input("Enter a String ; ")
#
# # Check if string contains a vowel
# if contains_vowel(input_string):
#     print("The string contains a vowel.")
# else:
#     print("The string does not contain any vowel.")


# def contains_vowel(s):
#     vowels = "AEIOUaeiou"
#     for char in s:
#         if char in vowels:
#             return "The string contains a vowel."
#     return "The string does not contain any vowel."
#
#
# # Get user input
# input_string = input("Enter a String : ")
#
# # Check for vowels and print the result
# result = contains_vowel(input_string)
# print(result)


# x = 'main'
# print('moon' in x)


# def vowelChecker(char):
#     vowel = 'aeiouAEIOU'
#     n = 0
#     for i in char:
#         if i in vowel:
#             n += 1
#     if n > 0:
#         print("The string contains a vowel.")
#     else:
#         print("The string does not contain any vowel.")
#
#
# inp = input()
#
# vowelChecker(inp)


##################################################


# text = input()
# vowel = ['a', 'e', 'i', 'o', 'u']
# flag = 0
# for i in text.lower():
#     if i in vowel:
#         flag += 1
#         break
# if flag > 0:
#     print('The string contains a vowel.')
# else:
#     print('The string does not contain any vowel.')


# maping #################################################

# a,b,c = map(int,input().split())
# print(a)
# print(b)
# print(c)

# def mapfun(a, b):
#     return a + b
#
#
# x = map(mapfun, (9, 4), (3, 4))
# print(list(x))


# bmi CALCULATOR
# def splitingFun(a):
#     return a
#
#
# x = map(splitingFun, input().split())
# y = list(x)
#
# h = float(y[0])
# w = float(y[1])
#
#
# def bmiCalculator(height, wight):
#     bmi = wight / (height ** 2)
#     print(f"BMI {bmi:.2f}")
#     if bmi < 18.5:
#         print("Underweight")
#     elif bmi >= 18.5 and bmi < 25.0:
#         print("Normal weight")
#     elif bmi >= 25.0 and bmi < 30.0:
#         print("Overweight")
#     else:
#         print("Obese")
#
#
# bmiCalculator(h, w)


# find nest number

# def splitingFun(a):
#     return a
#
#
# inp = map(splitingFun, input().split())
# toList = list(inp)
#
# inpNum1 = int(toList[0])
# inpNum2 = int(toList[1])
# inpNum3 = int(toList[2])
#
#
# def nextNumberFinder(n1, n2, n3):
#     differance = n2 - n1
#     n4 = n3 + differance
#     print(n4)
#
#
# nextNumberFinder(inpNum1, inpNum2, inpNum3)

#
# diff = b-a
# next_number = c+diff
# print(next_number)


# name = "main zamia"
# sploting = name.split()
# #
# print(sploting)
#
# w, h = input("write :")
#
# print(w)
# print(h)


# def get_odd_number(numbers):
#  odd_number = [num for num in numbers if num % 2 == 1]
#  return odd_number
#
#
# l1 = [0, 1, 2, 3, 4, 5]
# print(l1[::-1])
# print(get_odd_number(l1))


# def reverse_string(strings):
#  reversed_strings = [s[::1] for s in strings]
#  return reversed_strings
#
#
# str_list_1 = ["Hello", "Python", "Django"]
# print(reverse_string(str_list_1))


# def merge_dicts(dict1, dict2):
#  merged = dict2.copy()
#  merged.update(dict1)
#  return merged
#
#
# dict1 = {'a':1, 'b':2}
# dict2 = {'b':3, 'c': 4}
# print(merge_dicts(dict1, dict2))


# num = lambda l:l*l
#
# print(num(4**2))

contact_book = [
    {"name": "main", "phone": 23, "email": "Dhaka"},
    {"name": "zamia", "phone": 22, "email": "Dhaka"},
    {"name": "amana", "phone": 22, "email": "Dhaka"},
    {"name": "fatema", "phone": 22, "email": "Dhaka"},
    {"name": "kamal", "phone": 25, "email": "Chittagong"},
]


# print(contact_book[0]["name"])


# create contact
# contact_book = []


def contact_book_gen():
    name = input("name : ")
    phone = input("phone : ")
    email = input("email : ")

    contact_book.append(
        {
            "name": name,
            "phone": phone,
            "email": email,
        }
    )


# for contact in range(len(contact_book)):
#     print(
#         f"name {contact_book[contact]["name"]} phone {contact_book[contact]["phone"]} email {contact_book[contact]["email"]}",
#         sep=" | ",
#     )


# view contact
def view_contact():
    for contact in range(len(contact_book)):
        print(
            f"name {contact_book[contact]['name']} phone {contact_book[contact]['phone']} email {contact_book[contact]['email']}"
        )


# search contact
def search_contact():
    scherchInp = input("what do you want to scherch : ")

    for contact in range(len(contact_book)):
        if scherchInp in contact_book[contact]["name"]:
            print(
                f"name {contact_book[contact]['name']} phone {contact_book[contact]['phone']} email {contact_book[contact]['email']}",
                sep=" | ",
            )


# remove contact
def remove_contact():

    for contact in range(len(contact_book)):
        print(
            f"{contact + 1}. {contact_book[contact]["name"]}, {contact_book[contact]["phone"]}, {contact_book[contact]["email"]}"
        )

    removeInp = int(input("what do you want to remove : "))
    contact_book.pop(removeInp - 1)
    print(contact_book)


# remove_contact()


# update contact


def update_contact():
    # i have to see index number
    for contact in range(len(contact_book)):
        print(
            f"{contact + 1}. {contact_book[contact]['name']}, {contact_book[contact]['phone']}, {contact_book[contact]['email']}"
        )

    updateInp = int(input("what do you want to update : "))
    print(contact_book[updateInp - 1])

    newName = input("new name : ")
    newPhone = input("new phone : ")
    newEmail = input("new email : ")

    contact_book[updateInp - 1] = {
        "name": newName,
        "phone": newPhone,
        "email": newEmail,
    }

    print(contact_book)


# update_contact()


# backup contact


def backup_contact():
    # fp = open("contact.csv", "wt")
    with open("contact.csv", "wt") as fp:
        for contact in contact_book:
            line = f"{contact["name"]},{contact["phone"]},{contact["email"]}\n"
            fp.write(line)
            # fp.close()

    print("backup done !")


def restore():
    with open("contact.csv", "rt") as fp:
        for line in fp.readlines():
            spliteLines = line.strip().split(",")
            contact = {
                "name": spliteLines[0],
                "phone": spliteLines[1],
                "email": spliteLines[2],
            }
            contact_book.append(contact)


# manu_option = """
# 1. View Contact
# 2. Create contact
# 3. Search contact
# 4. Remove contact
# 5. Update contact
# 6. Backup contact
# 7. Restore contact
# 0. Exit
# """

# while True:
#     print(manu_option)
#     choice = int(input("Choose an option : "))
#     if choice == 1:
#         view_contact()
#     elif choice == 2:
#         contact_book_gen()
#     elif choice == 3:
#         search_contact()
#     elif choice == 4:
#         remove_contact()
#     elif choice == 5:
#         update_contact()
#     elif choice == 6:
#         backup_contact()
#     elif choice == 7:
#         restore()
#     elif choice == 0:
#         break


# def temCalculator():
#     cel = float(input())
#     print(cel)

#     fah = ((9/5 * cel) + 32)
#     print(f"The temperature in Fahrenheit is: {fah:.2f}")

# temCalculator()


# find minimum number


# numInp = input()
# splitingNumInp = numInp.split()

# num1 = int(splitingNumInp[0])

# num2 = int(splitingNumInp[1])

# num3 = int(splitingNumInp[2])

# minNun = min(num1, num2, num3)
# print(minNun)


# calculate the area of a Triangle

# def calculateTriangleArea(h, b):
#     area = (h * b) / 2
#     return area


# inp = input()

# splitingInp = inp.split()

# height = float(splitingInp[0])

# base = float(splitingInp[1])

# area = calculateTriangleArea(height, base)
# print(f"{int(area)}")


# find the difference between two numbers

# def finderBetweenTwoNumber(n1, n2):
#     diff = n1 - n2
#     return diff


# inp = input()

# splitingInp = inp.split()

# n1 = int(splitingInp[0])
# n2 = int(splitingInp[1])

# diff = finderBetweenTwoNumber(n1, n2)
# print(diff)


# calculate the area of a rectangle


# def calculateAreaRectangle(l, w):
#     area = l * w
#     return area


# inp = input()

# splitingInp = inp.split()

# l = int(splitingInp[0])
# w = int(splitingInp[1])

# area = calculateAreaRectangle(l, w)
# print(area)


# Write a program to find the quotient of two numbers (integer division).

# inp = input()

# splitingInp = inp.split()

# num1 = int(splitingInp[0])
# num2 = int(splitingInp[1])
# diviton = num1 / num2
# print(int(diviton))


# calculate the distance between two points
# math.dist()
# import math

# inp1 = input()
# inp2 = input()
# splitingInp1 = inp1.split()
# splitingInp2 = inp2.split()
# x1 = float(splitingInp1[0])
# y1 = float(splitingInp1[1])
# listing1 = [x1, y1]

# x2 = float(splitingInp2[0])
# y2 = float(splitingInp2[1])
# listing2 = [x2, y2]

# distance = math.dist(listing1, listing2)
# print(f"Distance: {distance:.2f}")


# num1 = [0, 0]
# num2 = [1, 2]
# print(math.dist(num1, num2))


# inp1 = input()
# # inp2 = input()
# splitingInp1 = inp1.split()
# print(splitingInp1)


# def mainFun(num1):
#     def inFun(num2):
#         return num1 + num2
#     return inFun(9)


# main = mainFun(6)

# print("zzz",main)


# inp = input("text here: ")


# print(inp)


# def SUM(a,b):
#     return a + b
# x = [1,2,3,4]
# y = map(SUM, x, x)
# print(list(y))


# namta
# x = 1
# y = 51000

# for i in range(x,y):
#     print(f"{i} gorar namta")
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * y}")


#  reuseable function

# class BBB():
#     def peofile(self, a , b):
#         return a + b

# # x = BBB().peofile(1,2)
# # print(x)

# def MtFun(a,b):
#     return BBB().peofile(a, b)

# print(MtFun(2,3))


# f are man bar korbo ============================================
# def fArMan(m1,m2,d2):
#     return (m1*m2)/d2

# m1 = 1
# m2 = 3
# d2 = 4

# f = fArMan(m1,m2,d2)
# print(f"F : {f}")


# import math

# print(math.sin(0))
# print(math.sin(30))
# print(math.sin(45))
# print(math.sin(60))
# print(math.sin(90))
# print(abs(-2999))


# import datetime

# print(datetime.MINYEAR)
# print(datetime.MAXYEAR)
# print(datetime.timedelta(100, 60))


# sum number
# def toInt(n):
#     return int(n)
# inp = map(toInt, input().split())
# listing = list(inp)
# print(sum(listing))


#  bonus of salary where bonus is the 10% of main salary

# salaery = float(input())
# bonus = 10

# bonus_salary = salaery * (bonus / 100)

# print(int(bonus_salary))


# checks if a number entered by the user is even or odd

# inp = int(input())

# if inp % 2 == 0:
#     print(f"{inp} is an even number.")
# elif inp % 2 == 1:
#     print(f"{inp} is an odd number.")


# calculates the area of a circle with that radius

# import math
# def area(r):
#     pi = round(math.pi, 2)
#     A = pi * (r ** 2)
#     return A

# r = float(input())
# a = area(r)
# print(f"The area of the circle is {a:.2f} square units.")


# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
# from collections import Counter

# class Solution:
#     def frequencySort(self, nums):
#         freq = Counter(nums)

#         nums.sort(key=lambda x: (freq[x], -x))

#         return nums

# s = Solution()
# print(s.frequencySort([1, 1, 2, 2, 2, 3]))
# print(s.frequencySort([2, 3, 1, 3, 2]))
# print(s.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))


# class Solution:
#     def frequencySort(self, nums):
#         x = nums
#         x.sort(reverse = True)
#         return x


# s = Solution()
# print(s.frequencySort([1, 1, 2, 2, 2, 3]))
# print(s.frequencySort([2, 3, 1, 3, 2]))
# print(s.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))


# from collections import Counter
# x = [1, 1, 2, 2, 2, 3]
# y = Counter(x)
# print(y)


# def sum_elements_less_than_median(arr):
#     # arr.sort()
#     median_index = len(arr) // 2

#     median = arr[median_index]

#     print(median)

#     sum_less_than_median = sum(num for num in arr if num < median)

#     return sum_less_than_median


# # Main program
# if __name__ == "__main__":
#     n = int(input("Enter size of the array: "))
#     if n == 0:
#         print("Input array is empty. Sum is 0.")
#     else:
#         print("Enter the elements:")
#         arr = list(map(int, input().split()))

#         if len(arr) != n:
#             print(f"Expected {n} elements but got {len(arr)} elements.")
#         else:
#             result = sum_elements_less_than_median(arr)
#             print(f"Output: {result}")


####################################################################

# inp = input()
# if not("0" in inp):
#     sorter = inp[::-1]
#     print(sorter)
# else:
#     sorter = inp[::-1]
#     sorter = sorter.lstrip('0')
#     print(sorter)


####################################################################

#  factorial of that number
# class Factorial_Number_Calculato():
#     def __init__(self, n):
#         self.n = n
    
#     def factorial(self):
#         if self.n == 0:
#             return 1
#         else:

#             # return self.n * (self.n - 1) * 2
#             # return self.n * (self.n - 1) * (self.n - 2) * 1
#             result = 1
#             for i in range(1, self.n + 1):
#                 result *= i
            
#             return result
            


# n = int(input())

# factorialsCalcucator = Factorial_Number_Calculato(n)
# factorial = factorialsCalcucator.factorial()

# print(f"{factorial}")




# check whether a number is palindrome or not
# class PalindromeChecker():
#     def __init__(self, n):
#         self.n = n
    
#     def is_palindrome(self):
#         str_n = str(self.n)
#         return str_n == str_n[::-1]

#     def palindromeValidation(self):
#         if self.is_palindrome():
#             return f"{self.n} is a palindrome number"
#         else:
#             return f"{self.n} is not a palindrome."
    
    

# inp = input()
# plindrome = PalindromeChecker(inp)
# print(plindrome.palindromeValidation())



##############################################################################
# Write a program where you have to find the GCD(Greatest Common Divisor) of two numbers.
# import math
# # inp = input().split()
# # num1 = int(inp[0])
# # num2 = int(inp[1])


# num1, num2 = map(int, input().split())
# print(math.gcd(num1, num2))


