#QUESTION 1
a=int(input("Enter a number"))
if a>0 and a%2==0:
    print("a is positive even")
elif a>0 and a%2>0 :
    print("a is positive odd")
elif a<0:
    print("a is negative")
else:
    print("a is zero")

#Question 3
a=int(input("Enter a number"))
for i in range (1,a):
    a*=i
print("Factorial of required no. is",a)
#QUESTION 4
a=str(input("Enter a number"))
x=0
for i in a:
    b=int(i)
    x+=b
print("Required sum=",x)
#Question 5
for i in range(1,50):
    if i%3!=0 and i%5!=0:
        print(i)
    elif i%3==0 and i%5!=0:
        print("Fizz")
    elif i%3!=0 and i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
#Question 6
for i in range(1,7):
    a=list(input("Enter a number"))
for i in a:
 smallest=0
 greatest=0
 if i<smallest:
    smallest=i
print(i," is smallest")
if i>greatest:
    greatest=i
print(i," is greatest")

#Question 10
x=str(input("Enter a string value"))
a=0
for i in x:
    
  if i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0":
       a+=1
print("number of digits= ",a)
  
b=len(x.replace(" ",""))
c=0
for i in x:
    if i=="a" or i=="b" or i=="c" or i=="d" or i=="e" or i=="f" or i=="g" or i=="h" or i=="i" or i=="j" or i=="k" or i=="l" or i=="m" or i=="n" or i=="o" or i=="p" or i=="q" or i=="r" or i=="s" or i=="t" or i=="u" or i=="v" or i=="w" or i=="x" or i=="y" or i=="z":
        c+=1
print("Number of alphabets",c)
print("no. of special characters=",b-(a+c))  

#QUESTION 2
a=int(input("Enter a digit"))
x=0
for i in range(1,a+1):
    if a%i==0:
        x+=1
if x==2:
    print("Number is prime")
else:
    print("Not prime")
 
 
#QUESTION 8
n=5
for i in range(1,i+1):
    spaces=n-i 
    stars=2*i-1
    print(" "*spaces+"*"*stars)  
    
    