# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 21:46:10 2019

@author: vijay
"""

# List Comprehension  and Lambda, Filter, Map, Reduce and zip
 

# List Comprehension 

""""
List comprehensions are used for creating new list from another iterables.
As list comprehension returns list, they consists of brackets containing 
the expression which needs to be executed for each element along with the 
for loop to iterate over each element.

Basic syntax:

new_list = [expression for_loop_one_or_more_conditions]
"""
"""
# Find squares of a number using for loop.
numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
    squares.append(n**2)
print(squares)  



# Finding squares using list comprehensions
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares)  



a = [1,2,3]
print ( [x**2 for x in range(1,6)] )
print ([ x + 1 for x in [x**2 for x in a ]])



# Find common numbers from two list using list comprehension
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num)


#List comprehensions can also be used to iterate over strings as shown below:
list_a = ["Hello", "World", "In", "Python"]
small_list_a = [str.lower() for str in list_a]
print(small_list_a) # Output: ['hello', 'world', 'in', 'python']


# Just like tuples list comprehensions can be used to produce list of list as shown below.
list_a = [1, 2, 3]
square_cube_list = [ [a**2, a**3] for a in list_a]
print(square_cube_list) # Output: [[1, 1], [4, 8], [9, 27]]

"""

# Lambda

"""
Lambda is a way to create anonymous function i.e. functions without name 
Lambda function are mainly used with Filter, Map and Reduce 
Lambda operator or lambda function is used for creating small, 
one-time and anonymous function objects in Python.

Syntax:
lambda arguments: expression
This function can have any number of arguments but only one expression, 
which is evaluated and returned.



 
# showing difference between def() and lambda(). 
def cube(y): 
    return y*y*y; 

print(cube(5))
"""
"""
# Converting the function to lambda function  
g = lambda y: y*y*y 
print (type(g))
print(g(5))  


# Lambda with two arguments 
f  = lambda x,y : x + y
print(f(1,1))




# Explain the concept of filter map reduce using the example of getting multiple  
# Temperature every sec using an IoT device


# Filter 
"""
"""
The filter() function in Python takes in a function and a list as arguments. 
This offers an elegant way to filter out all the elements of a sequence "sequence", 
for which the function returns True.


def f(x) :
    return x%3 ==0 or x%5 ==0 

list(range(2,25 ))

list(filter ( f, range(2,25 ) ))

print( list(filter ( f, range(2,25 ) ) ))


# Filter with Lambda function 
#foo = list(range(2,25 ))

#print (tuple(filter (lambda x:x%3==0 or x%5==0,foo)) )


print (list ( filter (lambda x:x%3==0 or x%5==0,(range(2,25)))))


# Map 


map() function returns a list of the results after applying the given function
to each item of a given iterable (list, tuple etc.)

Syntax :

map(fun, iter)
Parameters :

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

Returns :
Returns a list of the results after applying the given function to each item 
of a given iterable (list, tuple etc.) 


# Return double of n 
def addition(n): 
  return n + n 

# We double all numbers using map() 
numbers = [1, 2, 3, 4] 
result = map(addition, numbers) 
print(list(result)) 


# Double all numbers using map and lambda 
numbers = [1, 2, 3, 4] 
result = map(lambda n: n + n, numbers) 
print(list(result)) 



# Multiple iterables to the map function

# Add two lists using map and lambda 
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 


result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 


# List of strings 

l = ['sat', 'bat', 'cat', 'mat'] 
# map() can listify the list of strings individually 
test = list(map(list, l)) 
print(test) 





# Reduce


The reduce() function in Python takes in a function and a list as argument. 
The function is called with a lambda function and a list and a new reduced result is returned. 
This performs a repetitive operation over the pairs of the list. 
This is a part of functools module



from functools import reduce

def add(x,y):
    return x+y

print(reduce( add, range(1,6)))

#print(list(map( add, range(1,6))))

# Reduce with Lambda function
from functools import reduce
foo = [2,18,9,22,17,24,8,12,27]
print (reduce (lambda x,y : x + y,foo))


# zip


In Python3, zip methods returns a zip object instead of a list. 
This zip object is an iterator. Iterators are lazily evaluated.
Lazy evaluation, or call-by-need is an evaluation strategy which 
delays the evaluation of an expression until its value is needed 
and which also avoids repeated evaluations
Iterators returns only element at a time. 
len function cannot be used with iterators. 
We can loop over the zip object or the iterator to get the actual list



list_a = [1, 2, 3]
list_b = [4, 5, 6,7]

zipped = zip(list_a, list_b) # Output: Zip Object. <zip at 0x4c10a30>

len(zipped) # TypeError: object of type 'zip' has no len()

zipped[0] # TypeError: 'zip' object is not subscriptable

list_c = list(zipped) #Output: [(1, 4), (2, 5), (3, 6)]
print (list_c)

list_d = list(zipped) # Output []... Output is empty list becuase by the above statement zip got exhausted.
print (list_d)








Dictionaries
How to store phone number in a phone book ? 
You would have a list of names and attached to each name a phone number 

Dictionaries is a key value un-ordered pair ( name : mobile number )
Unordered set of key: value pairs where keys are unique
Dictionaries consist of zero or more comma-separated key-value pairs that are enclosed in braces { }
The key and its value are separated by a colon :

We declare dictionaries using {} braces
Like lists dictionaries are also mutable



# Initialise the dictionary 
dict1 = dict() 
type(dict1)

dict1 = {}
type(dict1) 
dict1 = dict({})  
type(dict1)
  
dict1 = { 'name':'mobile_number'}
print(dict1)
print(type(dict1))

phone_book = { 'a':1234567, 'b':87654321, 'c':1232123432}
print(phone_book)


# Creation of dictionaries
dict1 = {'fname':'John', 'lname':'Mille', 'profession':'plumber',  'age':'32'}



# Add/Update
dict1['lname'] = 'Miller'
dict1['profession'] = 'electrician'
dict1['age'] = '36'
dict1['city'] = 'NY' #add
print(dict1)

dict1['city'] = 'MA' #update
print(dict1)

dict1.update ( {'age':32, 'city':'MA' } )
print(dict1)

# Printing Values
print (dict1["lname"])
print (dict1.get('lname'))
print (dict1.get('name', 'Not Found'))


# This is the old way  
my_string = "Hi ! My name is {name} and I live in {city}.".format('John Miller', 'MA')

my_string = "Hi ! My name is {name} and I live in {city}.".format(name='John Miller', city = 'MA')


# Assume that your have 
dict1 = { 'name': 'John Miller', 'city':'MA'}
 
my_string = "Hi ! My name is {name} and I live in {city}.".format(**dict1)

my_string = "Hi ! My name is {city} and I live in {name}.".format(**dict1)
# Remove from dictionary
del dict1['city']
print(dict1)

dict1.pop('city')


dict1 = {'fname':'John', 'lname':'Miller', 'profession':'plumber',  'age':'32'}


# To list all the keys
a  = dict1.keys()
print(type(a)) 

# To list all the values  
print(dict1.values())

# To list all the values  
print(dict1.items())



# To list all keys  
for key in dict1.keys() :
  print ( key )


# To list all values   
for value in dict1.values():
  print ( value )

 
# To list all values and keys  
for key in dict1:
  print ( key , dict1[key] )
 

# Looping the dictionary 
for key, value in dict1.items() :
  print ( key, value )

####in built function and methods
  
len(dict1)
str(dict1)
b=dict1
id(dict1)
id(b)
c=dict1.copy()
id(c)

seq=["python","c","c++"]
marks=60
ndict=dict.fromkeys(seq,marks)
ndict=dict.fromkeys(seq,-1)
print(ndict)
dict1.get("age")
"""

#a,b=map(int(input().split()))
