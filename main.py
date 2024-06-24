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

# tuples = ("main", "Sazzad", "Mijan", "marjan", "koli")
# print("tuples 1", tuples)
# print("tuples 2", tuples[2]);

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
f = open('y.txt', 'a')
f.write("jhfdsagnsrduihng")
f.close()

f = open("y.txt")
print(f.read())



