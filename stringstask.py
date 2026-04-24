#QUESTION 1
x=str(input("Enter a string value"))
y=0
for i in x:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        y+=1
    
print("total number of vowels are",y)
#OUESTION 2
x=str(input("Enter a string value"))
y=0
z=len(x)
for i in range (z):
  a=x.count("a")
  e=x.count("e")
  i=x.count("i")
  o=x.count("o")
  u=x.count("u")    
print("total number of vowels are",a+e+i+o+u)
print("a-",a)
print("e-",e)
print("i-",i)
print("o-",o)
print("u-",u)


#QUESTION 3
x=str(input("Enter a string value"))
a=e=s=o=u=y=0
for i in x:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        y+=1
    if i=="a":
        a+=1
    if i=="e":
        e+=1
    if i=="i":
        s+=1
    if i=="o":
        o+=1
    if i=="u":
        u+=1
print("No. of vowels=",a+e+s+o+u)
print("a-",a)
print("e-",e)
print("i-",s)
print("o-",o)
print("u-",u)
#QUESTION 4
x=str(input("Enter a string value"))
a=0
b=len(x)
for i in range (b):
  c=x[i]
  if c=="a":
    a+=1
    if a==2:
     print("Location of second ocuccuring a is ",i)
     
#QUESTION 5
x=str(input("Enter a string value"))
print("Last i location is",end=" ")
print(x.rfind("i")) 

#QUESTION 6
x=str(input("Enter a string value"))
print("Total characters in string=",end=" ")
print(len(x))  
c=len(x.replace(" ",""))
print("Total characters in string without space",end=" ")
print(c)
print(x.count("a"))
a=0
for i in x:
  if i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0":
       a+=1
print(a)
#QUESTION 7
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>=b and a>=c:
    print(a," is the greatest number")
elif b>=c and b>=a:
    print(b," is the greatest number")
else:
    print(c," is the greatest number")

#QUESTION 8
x=int(input("Enter a number"))
if x%3==0 or x%5==0 or x%10==0:
    print("ALLOW")
else:
  print("NOT ALLOWED")