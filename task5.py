#QUESTION 1
# def fizzbuzz():
#     for i in range(1,51):
#         if i%3!=0 and i%5!=0:
#             print(i)
#         elif i%3==0 and i%5!=0:
#             print("Fizz")
#         elif i%3!=0 and i%5==0:
#             print("Buzz")
#         elif i%3==0 and i%5==0:
#             print("FizzBuzz")
# fizzbuzz()

#QUESTION 2
# def prime():
#     for a in range(1,100):
#         x=0
#         for i in range(1,a+1):
#             if a%i==0:
#              x+=1
#         if x==2:
#          print(a," is prime")
# prime()    
     
#QUESTION 3
# def grade():
#     a=int(input("Enter marks"))
#     if a<=100 and a>=90:
#         print("Grade:A")
#     elif a<=89 and a>=80:
#         print("Grade:B")
#     elif a<=79 and a>=70:
#         print("Grade:C")
#     elif a<=69 and a>=60:
#         print("Grade:D")
#     elif a<60:
#         print("Grade:E")
#     else:
#         print("INVALID INPUT")
# grade()

#QUESTION 4
# def table():
#     a=int(input("Enter a number"))
#     for i in range(1,11):
#         print(a,"*",i,"=",a*i)
# table()


#QUESTION 5
# def square():
#     for i in range(1,21):
#         if i%2==0:
#             print("Square of ",i," is ",i*i)
# square()


#QUESTION 6
# def leap():
#   x=int(input("Enter year"))
#   if x%4==0 or x%400==0:
#     print("It is a leap year")
#   elif x%100==0:
#     print("It is not a leap year")
#   else:
#       print("It is not a leap year")
# leap()


#QUESTION 7
# def triangle():
#     a=int(input("Enter first side of triangle"))
#     b=int(input("Enter second side of triangle"))
#     c=int(input("Enter third side of triangle"))
#     if a+c>b and a+b>c and b+c>a:
#         if a==b and b==c:
#             print("It is an equilateral triangle")
#         elif a==b or b==c or b==c:
#             print("It is an isosceles triangle")
#         elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
#             print("It is a right angled triangle")
#         elif a!=b and b!=c and a!=c:
#             print("It is a scalene triangle")
#     else:
#         print("They donot form a triangle")
# triangle()


#QUESTION 8
# def num():
#    a=int(input("Enter a number"))
#    if a>0:
#        print(a," is positive")
#    elif a<0:
#        print(a," is negative")
#    else:
#        print("It is zero")
# num()


#QUESTION 9
# def strong():
#     a=str(input("Enter your password"))
#     if len(a)>=8:
#         for i in a:
#             if i.isupper():
#                 for i in a:
#                     if i.islower():
#                         for i in a:
#                             if i.isdigit():
#                                 for i in a:
#                                     if not i.isalnum():
#                                      print("Your password is strong")
#                                      return
#         print("Password is weak.It must contain uppercase, lowercase, digit, and special character")
#     else:
#         print("Password is weak.It must contain uppercase, lowercase, digit, and special character")                               
# strong()

#QUESTION 10
# def bmi():
#     a=float(input("Enter weight in kilograms"))
#     b=float(input("Enter heightin meters"))
#     x=a/(b**2)
#     print("Your BMI is ",x)
#     if x<18.5:
#         print("You are underweight")
#     elif x>=18.5 and x<24.9:
#         print("Normal weight")
#     elif x>=24.9 and x<29.9:
#         print("You are overweight")
#     else:
#         print("OBESITY")
# bmi()

#QUESTION 11
# def day():
#     x=int(input("ENTER A NUMBER"))
#     if x==1 :
#         print("MONDAY")
#     elif x==2 :
#         print("TUESDAY")
#     elif x==3 :
#         print("WEDNESDAY")
#     elif x==4 :
#         print("THURSDAY")
#     elif x==5 :
#         print("FRIDAY")
#     elif x==6 :
#         print("SATURDAY")
#     elif x==7 :
#         print("SUNDAY")
#     else:
#         print("INVALID INPUT")
# day()


#QUESTION 12
# def discount():
#     x=int(input("Enter price of product in $"))
#     if x>1000:
#         print("Discounted price:$",x-x*0.1)
#     elif x>=500 and x<=1000:
#         print("Discounted price:$",x-x*0.05)
#     else:
#         print("No discount...Kindly pay the original price:$",x)
# discount()


#QUESTION 13
# def sum():
#     x=0
#     n=int(input("Enter value of n"))
#     for i in range(1,n+1):
#         x+=i
#     print("Sum of ",n,"natural numbers is ",x)
# sum()


#QUESTION 14
# def lists():
#     x=int(input("Enter number of lists you want"))
#     li1=[]
#     for i in range(x):
#         y=int(input("Enter number of elements in list"))
#         li2=[]
#         for i in range(y):
#             z=int(input("Enter element"))
#             li2.append(z)
#         li1.append(li2)
#     print(li1)    
# lists()
            
            
#QUESTION 15
# def vowels():
#     x=str(input("Enter a string value"))
#     y=0
#     for i in x:
#         if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#             y+=1
#     print("Number of vowels: ",y)
# vowels()


#QUESTION 16
# def add():
#     a=str(input("Enter a number"))
#     x=0
#     for i in a:
#         b=int(i)
#         x+=b
#     print("Required sum=",x)
# add()
                

#QUESTION 17
# def pattern():
#     b=0
#     for i in range(0,5,1):
#         for j in range(i+1):
#             b+=1
#             print(b,end=" ")
#         print()
# pattern()


#QUESTION 18
# def game():
#     import random as rn
#     a=rn.randint(1,100)
#     if a>90:
#         print("It is a higher number")
#         b=int(input("Enter your guess between 1 and 100"))
#     elif a<10:
#         print("It is a lower number")
#         b=int(input("Enter your guess between 1 and 100"))
#     else:
#         b=int(input("Enter your guess between 1 and 100"))
#     if a==b:
#         print("YES...YOU GUESSED IT RIGHT!!!")
#     else:
#         print("YOUR GUESS IS WRONG")
# game()