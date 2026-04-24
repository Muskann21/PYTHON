#QUESTION 1
x=int(input("Enter a number"))
for i in range(x):
    print("Muskan")
#QUESTION 2
a=int(input("Enter a value"))
for i in range(3,33,1):
    print(a,"*",i,"=",a*i)
#QUESTION 3
a=int(input("Enter first number"))
b=int(input("Enter second number"))
if a<b:
    for i in range(a,b):
     print(i)
else:
    for i in range(a,b,-1):
        print(i)
#QUESTION 4
a=str(input("Enter your name"))
b=int(input("Enter your current age"))
c=int(input("Enter current year"))
d=int(input("Enter expected year"))
for i in range(d):
    print("Hey",a,"in",c+i,"you are",b+i,"years old")