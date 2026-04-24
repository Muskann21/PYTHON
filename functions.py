#QUESTION 1
def temp():
 c=float(input("Enter temp in celsius"))
 f = (c * 9/5) + 32
 print("Temp in farenheit= ",f)
temp()
 
#QUESTION 2
def gcd():
    a=int(input("Enter first number"))
    b=int(input("Enter first number"))
    while b!=0:
        a,b=b,a%b
        print (a)
gcd()
    

 
#QUESTION 3
def list():
    li1=[1,"hello",25.87,True]
    li2=[63,"world",733.98,False]
    li3=[]
    for i in li1:
     li3.append(i)
    for i in li2:
     li3.append(i)
    print(li3)
list()    


#QUESTION 4
def vowels():
 x=0
 a=str(input("Enter a string value"))
 for i in a:
    if i =="a" or i=="e" or i=="i" or i=="o" or i=="u":
        x+=1
 print("No. of vowels= ",x)
vowels()


#QUESTION 5
def find():
    li=[23,65,9,84,678,26,100]
    li.sort()
    b=len(li)
    print("Second largest number in list id ",li[b-2])
find()

#QUESTION 6
def duplicate():
    li=[53,"hello",567.88,True,53,"hello"]
    for i in li:
     b=li.count(i)
     if b==2:
         li.remove(i)
    print(li)
duplicate()


#QUESTION 7
def prime():
    a=int(input("Enter a number"))
    x=0
    for i in range (1,a+1):
        for j in range(1,i+1):
         if i%j==0:
            x+=1
            if x==2:
             i+=0
    print(i)
prime()
         
#QUESTION 8
def leap():
  x=int(input("Enter year"))
  if x%4==0:
    print("It is a leap year")
  else:
    print("It is not a leap year")
leap()


#QUESTION 9
