Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: C:/Users/Rose/Desktop/python 2/fun.py ===============
5
>>> 
=============== RESTART: C:/Users/Rose/Desktop/python 2/fun.py ===============
first line
0
1
2
3
last line
>>> 
=============== RESTART: C:/Users/Rose/Desktop/python 2/fun.py ===============
5
>>> 
=============== RESTART: C:/Users/Rose/Desktop/python 2/fun.py ===============
global variable 10
inside function  20
inside function 50
Traceback (most recent call last):
  File "C:/Users/Rose/Desktop/python 2/fun.py", line 31, in <module>
    func(20)
  File "C:/Users/Rose/Desktop/python 2/fun.py", line 28, in func
    print("inside golbal variable",gnum)
UnboundLocalError: local variable 'gnum' referenced before assignment
>>> 
=============== RESTART: C:/Users/Rose/Desktop/python 2/fun.py ===============
global variable 10
inside function  20
inside function 50
inside golbal variable 10
inside global variable 10
outside global variable 10
>>> 
