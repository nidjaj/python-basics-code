#1
"""
def differ(x,y):    #function header
    return(x-y)     #function body
a=15
b=10
cal=differ(a,b)
print(cal)
"""

#2
"""
def func():
    for i in range(4):
        print(i)
print("first line")
func()
print("last line")
"""
#3
"""
def differ(x,y=5):    #function header
    return(x-y)     #function body
a=15
b=10
cal=differ(b)
print(cal)
"""
#4
"""
def total(a,b):
    c=a+b
    return c
p=int(input("enter first no"))
q=int(input("enter second no"))
d=total(p,q)
print("sum is",d)
"""
#5
"""
p=int(input("enter first no"))
q=int(input("enter second no"))
d=total(p,q)
print("sum is",d)

def total(a,b):
    c=a+b
    return c
"""
#6
"""
gnum=10   #global variable defined in the main body and visible throughout the program
print("global no",gnum)
def func(num):
    print("inside function",num)
    lnum1=50#local variable
    print("inside function",lnum1)
    print("inside function global variable",gnum)
    gnum=100
    print("inside function global variable",gnum)
func(20)
print("outside function global",gnum)
#print("outside function local",lnum1)
"""
#7
"""
gnum=100
def func():
    num=99
    print("local variable",num)
    


#8
###Required Arguments

def disp(str1,str2):
    print(str1)
    #print(str2)

disp("hello","vijay")
"""
###keyword Arguments
"""
def disp(y,x,z):
    print("value of x is {} y is {} and z is {}".format(x,y,z))
    #print("x is ",x)

disp(y=30,z=20,x="hello")

#default Arguments

#default argument must be written after non default arguments

def disp(x,y,z=60):
    print("value of x is {} y is {} and z is {}".format(x,y,z))

#disp("hello",90)
#or
disp("hello",90,213)

"""
#variable length arguments

def disp(name,*sub):
    print("name {}".format(name))
    print(type(sub))
    for i in sub:
        print("subjects are {}".format(i))
#disp("ajay","python","dsa","C++")
disp("ajay","python","dsa","C++","java")

"""
def disp(name,*sub):
    print("name {}".format(name))
    for i in sub:
        print("subjects are {}".format(i))
disp("ajay","python","dsa","C++")



##############################

def num(a,b):
    c=a+b
    d=a-b
    return c,d

sump,sub=num(10,15)
print(sump,sub)
 """   
