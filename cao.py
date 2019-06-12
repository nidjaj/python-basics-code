#WAP that has a class person storing name and date of birth .the program should subtract dob from todays date
#and find out whether a person is eligible to vote or not.

#WAP that has a class store which keeps a record of code and price of each product.Display a menu of all product to the user and
#prompt him to enter the quantity of each item.Genereate the bill and display the total amount.

#WAP that has a class polygon ,derive two classes rectangle and triangle.Write method to get the detail of the dimension and
#calculate area.

#WAP to copy text in another label using tkinter


#WAP that print a histogram of frequencies of character occuring in a message

#WAP that use map function to print the double value of each element in a list

#WAP to implement stack and queue

#WAP to make a quiz, use zip function to extract question and answer from two separate list.

#WAP to remove all duplicate value from a list

#WAP to create a list of odd numbers using list comprehension
'''
import time
class Person:
    def __init__(self,name,DOB):
        self.name = name
        self.DOB  = DOB.split("/")  
        self.age = time.localtime().tm_year - int(self.DOB[-1])
while(True):
    
    name = input("entername:")
    if(name == '-1'):
        break
    DOB = input("Enter DOB (dd/mm/yyyy): ")
    a = Person(name,DOB)
    if(a.age >= 18):
        print(f"{a.name} is eligible to vote")
    else:
        print(f"{a.name} is not eligible to vote")

'''

'''
class Store:
    dict1 = {}
    dict3 = {}
    list1 = []
    def __init__(self,p_code,price):
        self.p_code = p_code
        self.price = price
        Store.dict1[p_code] = price
        Store.list1 = list(Store.dict1.keys())
        
    def display(self):
        print("Product-Code","Prices")
        for i,j in Store.dict1.items():
            print(i,j)

    def get(self,dict2):
        self.dict2 = dict2

    def bill(self):
        for i,j in self.dict2.items():
            Store.dict3[i] = Store.dict1[i] * j
        pay = sum(Store.dict3.values())
        print("Product-Code","Quantity")
        for i,j in self.dict2.items():
            print(i,j)
        print(f"Total payment:{pay}")

dict2 = {}
product = int(input("Enter no of products: "))
for i in range(product):
    p_code = input("enter p_code")
    price = int(input("enter price"))
    object1 = Store(p_code,price)
object1.display()
for i in object1.list1:
    quantity = int(input(f"Enter the quantity for {i}: "))
    dict2[i] = quantity
object1.get(dict2)
object1.bill()
'''

'''
class Polygon:
    def __init__(self,side):
        self.n = side
        self.sides = [ 0 for i in range(side)]

    def inputside(self):
        self.sides = [float(input("Enter side " + str(i+1)+" : ")) for  i in range(self.n)]

    def dispsides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
        
class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,4)

    def findArea(self):
        a,b,c,d = self.sides
        area = a*b
        print("Area of rectangle is",area)

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a,b,c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print(f"area of triangle is {area}")
    
t = Triangle()
t.inputside()
t.dispsides()
t.findArea()

r = Rectangle()
r.inputside()
r.dispsides()3
r.findArea()
'''

'''
from tkinter import *
def copy():
    a = e1.get()
    l2 = Label(root,font = ("Arial",15),fg="RED",bg="WHITE",width="20")
    l2.place(x=250,y=140)
    l2['text'] = a

root = Tk()
root.title("Copy the Text")
root.geometry("500x300")
root.resizable(True,True)


l1 = Label(root,text="Text to Copy: ",font = ("Arial",15),fg="RED")
l1.place(x=100,y=20)

e1 = Entry(root,font=("Arial",15,'bold'),fg="Blue")
e1.place(x=250,y=20)

b1 = Button(root,text="Copy",command =lambda:copy(),
            font=("Arial",15,'bold'),fg='Red')
b1.place(x=220,y=70)

l2 = Label(root,text="Text to Copy: ",font = ("Arial",15),fg="RED")
l2.place(x=100,y=140)

root.mainloop()
'''

'''
from collections import Counter
text = Counter(input("Enter any string : "))
text = dict(text)

for i,j in text.items():
    print(i,'*'*j)
'''

'''
#input karo [1,2,3,2,1,3] ya [2,3] aisa kuch a proper list
list1 = eval(input("enter a list of numbers"))
print(list(map(lambda x : 2*x,list1)))
'''

"""
class Stack:
    stack = []
    top = '-1'
    def Push(self,value):
        self.value = value
        Stack.stack.append(self.value)
        Stack.top = self.value
    def Pop(self):
        if(len(Stack.stack) == 0):
            print("Stack is empty")
        value = Stack.stack.pop()
        print("removed",value)
        Stack.top = Stack.stack[-1]
    def show(self):
        print(f"the current stack is {Stack.stack}")
        print("current Top value:",Stack.top)

s = Stack()
print('''choose an option:
1.PUSH
2.POP
3.Display
4.Exit''')
while(True):
    option = int(input("Choose the option: "))
    if(option == 1):
        value = input("enter a value to insert in stack: ")
        s.Push(value)
    elif(option == 2):
        s.Pop()
    elif(option == 3):
        s.show()
    elif(option == 4):
        break
    else:
        print("choose an correct option")
"""


"""
class Queue:
    queue = []
    rear = -1
    front = -1
    def Insert(self,value):
        self.value = value
        if(Queue.rear == -1 and Queue.front == -1):
            Queue.rear = self.value
            Queue.front = self.value
            Queue.queue.append(self.value)
        else:
            Queue.rear = self.value
            Queue.queue.append(Queue.rear)

    def Remove(self):
        if(Queue.front == -1):
            print("Queue --> empty")
        else:
            Queue.queue.pop(0)
            if(len(Queue.queue)==0):
                Queue.rear = -1
                Queue.front = -1
                return 0
            Queue.front = Queue.queue[0]
            if(len(Queue.queue)==1):
                Queue.rear = Queue.front
            
    def Display(self):
        print(Queue.queue)
        print("front: ",Queue.front)
        print("rear: ",Queue.rear)

q = Queue()
print('''Choose an option:
1.Insert
2.Remove
3.Display
4.Exit''')
while(True):
    option = int(input("Choose an option: "))
    if(option == 1):
        value = input("Enter value to insert: ")
        q.Insert(value)
    elif(option == 2):
        q.Remove()
    elif(option == 3):
        q.Display()
    elif(option == 4):
        break
    else:
        print("choose a correct option")
"""

'''
questions = ["5+4=?","which is the power operator","function inside class is?","time.time() returns ?"]
answers = ["9","**","method","current time in milliseconds since midnight,jan 1,1970 GMT"]
for i in list(zip(questions,answers)):
    for j in i:
        print(j,end=" ")
    print("")
'''

'''
list1 = input("Enter elements of list: ").split()
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list1)
print(list2)
'''

'''
a = [i for i in range(100) if i%2 != 0]
print(a)
'''
