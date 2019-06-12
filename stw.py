"""str1="welcome!"
str2="to python"
str3=str1[ :2]+str2[len(str2)-2: ]
print(str3)"""

"""for i in range(1,4):
    for j in range(i,0,-1):
        print(j,end=" ")
    if(i==1):pass
    else:
        for k in range(2,i+1):
            print(k,end=" ")
        print(" ")

for i in range(1,5):
    print("*"*i)
for i in range(1,5):
    c=str(i)
    print(c*i)
a="jecrc university jaipur"
b=a.split()
print(b)
print(b[0])
str.capitalize(b)"""

for i in range(1,6):
    for j in range(5-i,0,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(i,end="  ")
print(" ")
