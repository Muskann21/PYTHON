#question 1
x=int(input("ENTER A NUMBER"))
if x==1 :
    print("JANUARY")
elif x==2 :
    print("FEBRUARY")
elif x==3 :
    print("MARCH")
elif x==4 :
    print("APRIL")
elif x==5 :
    print("MAY")
elif x==6 :
    print("JUNE")
elif x==7 :
    print("JULY")
elif x==8 :
    print("AUGUST")
elif x==9 :
    print("SEPTEMBER")
elif x==10 :
    print("OCTOBER")
elif x==11 :
    print("NOVEMBER")
elif x==12:
    print("DECEMBER")
else :
    print("INVALID")
    
    #QUESTION 2
a=int(input("Enter first number"))
b=int(input("Enter second number"))
#1 
if a==b:
    print("Both numbers are equal")
else:
    print("They are not equal")
#2
a=int(input("Enter first number"))
b=int(input("Enter second number"))
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else :
    print("b is greater than a")
#3
a=int(input("Enter first number"))
b=int(input("Enter second number"))
if a<=b:
    print("a is smaller or equal to b")
else:
    print("a is greater than b")
#4
a=int(input("Enter first number"))
b=int(input("Enter second number"))
if a>b:
    print("MUSKAN")
    print("MUSKAN")
    print("MUSKAN")
    print("MUSKAN")
    print("MUSKAN")
elif a<b:
     print("SINGAL")
     print("SINGAL")
     print("SINGAL")
else:
    print("INVALID")
    #QUESTION 3
a=str(input("ENTER STRING 1"))
b=str(input("ENTER STRING 2"))
#1
if a==b:
    print("a is equal to b")
else:
    print ("a is not equal to b")
    #2
a=str(input("ENTER STRING 1"))
b=str(input("ENTER STRING 2"))
if a is b:
    print("a is equal to b")
else:
    print ("a is not equal to b")
    #4 QUESTION 4
a=str(input("ENTER STRING 1"))
b=str(input("ENTER STRING 2"))
p=int(a)
q=int(b)
if p is q :
    print("p is equal to q")
else:
    print("a is not equal to q")
 #QUESTION 5
x=int(input("Enter your budget(in USD)"))
if x>=2500:
    print("According to your budget we suggest you these countries")
    print("1.GERMANY")
    print("2.AUSTRALIA")
    print("3.MALAYSIA")
    a=int(input("Enter the corresponding number to select a country"))
    if a==1:
     print("You selected Germany")
     print("We suggest you to visit these places in Germany")
     print("1.BERLIN")
     print("2.MUNICH")
     print("3.HAMBURG")
    elif a==2:
     print("You selected Australia")
     print("We suggest you to visit these places in Australia")
     print("1.SYDNEY")
     print("GREAT BARRIER REEF")
     print("MELBOURNE")
    elif a==3:
     print("You selected Malaysia")
     print("We suggest you to visit these places in Malaysia")
     print("1.PENANG")
     print("2.LANGKAWI")
     print("3.MALACCA")
    else :
     print("INVALID")
else :
    print("No travel options for budget less than $2500")

    
