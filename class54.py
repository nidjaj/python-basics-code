Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=[1,23,45,6]
>>> a.append(37)
>>> a
[1, 23, 45, 6, 37]
>>> a.insert(0,6)
>>> a
[6, 1, 23, 45, 6, 37]
>>> a.insert(10,34)
>>> a
[6, 1, 23, 45, 6, 37, 34]
>>> 
a.remove(6)
>>> a
[1, 23, 45, 6, 37, 34]
>>> a.count(45)
1
>>> a.append(6)
>>> a
[1, 23, 45, 6, 37, 34, 6]
>>> a.remove(6)
>>> a
[1, 23, 45, 37, 34, 6]
>>> ab=a.count(6)
>>> ab
1
>>> ab=a.remove(6)
>>> ab
>>> type(ab)
<class 'NoneType'>
>>> ab=a.count(34)
>>> ab
1
>>> type(ab)
<class 'int'>
>>> a.pop()
34
>>> a
[1, 23, 45, 37]
>>> a.pop(3)
37
>>> a
[1, 23, 45]
>>> a.append[1,2,34]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.append[1,2,34]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.append(1,3,23)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.append(1,3,23)
TypeError: append() takes exactly one argument (3 given)
>>> a.append[(1,2,34)]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.append[(1,2,34)]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.index(2)
ValueError: 2 is not in list
>>> a
[1, 23, 45]
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.index(2)
ValueError: 2 is not in list
>>> a.index(23)
1
>>> a.reverse()
>>> a
[45, 23, 1]
>>> a.sort()
>>> a
[1, 23, 45]
>>> a.delete(2)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.delete(2)
AttributeError: 'list' object has no attribute 'delete'
>>> del a[0]
>>> a
[23, 45]
>>> b=[1,2,3,\
       4]
>>> b
[1, 2, 3, 4]
>>> len(b)
4
>>> max(b)
4
>>> min(b)
1
>>> sum(b)
10
>>> a.append(b)
>>> a
[23, 45, [1, 2, 3, 4]]
>>> a.extend(b)
>>> a
[23, 45, [1, 2, 3, 4], 1, 2, 3, 4]
>>> a[4][0]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a[4][0]
TypeError: 'int' object is not subscriptable
>>> a[2][0]
1
>>> a=[3,4,5,6]
>>> a+b
[3, 4, 5, 6, 1, 2, 3, 4]
>>> a
[3, 4, 5, 6]
>>> a=a+b
>>> a
[3, 4, 5, 6, 1, 2, 3, 4]
>>> a
[3, 4, 5, 6, 1, 2, 3, 4]
>>> 3 in a
True
>>> 3 not in a
False
>>> 10
10
>>> a is b
False
>>> c=a
>>> a is c
True
>>> a=10
>>> b=15
>>> c=10
>>> a is b
False
>>> a is c
True
>>> a=[1,3,4]
>>> b=(1,3,5)
>>> type(a)
<class 'list'>
>>> type(b)
<class 'tuple'>
>>> a[0]=12
>>> a
[12, 3, 4]
>>> b[0]=12
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    b[0]=12
TypeError: 'tuple' object does not support item assignment
>>> c,d,e=b
>>> c
1
>>> d
3
>>> e
5
>>> c,d,e=a
>>> c
12
>>> d
3
>>> e
4
>>> type(a)
<class 'list'>
>>> 
>>> 
