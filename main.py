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

#function 

# def fun(a, b, c):
#   print("1st factory fun value is :", a + b + c);
# fun(1, 2, 3);


# def fun(a, b, c):
#   print("2nd factory fun value is :", a + b + c);
# fun(3, 4, 6);


#######################################################################################################################

# import random

# print(random.randrange(1,9))



####################################################################################################################################################


# txt = "My name is Main";
# if "My" in txt:
#   print("my my");
# print("Main" in txt);


################################################################################################################################################
# I will learn it by Subin vai

# class myclass():
#   def __len__(self):
#     return 0
# myobj = myclass()
# print(bool(myobj))

# x =1;
# y = 2;
# if not(x == 3 or y == 4):
#   print("x = y");
# else:
#   print("x is not equal to y");


# x =1;
# y = 2;
# if x is not 2:
#   print("x = y");
# else:
#   print("x is not equal to y");



###############################################################################################################################################

#array listing

x = [1,2,3,4,5,6];

# print(x[-1]);
# print(x[2:4]);
# print(x[2:]);
# print(x[:3]);
# x[2] = 5;
# print("Chenge", x);
# x[2:3] = [5,7];
# print("Chenge 2", x);

# x.insert(2, "aaa");
# print("insert", x);

# x.append("bbb");
# print("append", x);

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


subArray = [];
for i in x:
 if i == 2:
   subArray.append(i);
   print(f"list is {subArray}")
   break;


# cars = ["BMW", "MNW", "OD", "OM"];
# subArray = [];
# for i in cars:
#  if "O" in i:
#    subArray.append(i)
# print(subArray)