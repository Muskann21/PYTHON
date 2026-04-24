# li=[]
# for a in range(1,4):
#  a=int(input("Enter first number"))
#  li.append(a)

# li.sort()
# print("Smallest number is:",li[0])

#QUESTION 2
# def is_prime(a):
#     x=0
#     for i in range(1,a+1):
#         if a%i==0:
#             x+=1
#     if x==2:
#         print("True,The number is prime")
#     else:
#         print("False,The number is not prime")
# is_prime(3)


#QUESTION 3
# li1=[2,3,4,5,6]
# x=0
# for i in li1:
#     x+=i
# print("Required sum is",x)


#QUESTION 4
# a=("Red","Green","Blue")
# for i in a:
#     if i=="Yellow" or i=="yellow":
#      print("Yellow is present in the set")
#     else:
#      print("Yellow is not present")


#QUESTION 5
# dic={
#     {"name1":"riya",
#      "marks1":98,
#      "course1":"b.tech",
#      },
#     {"name2":"jiya",
#      "marks2":88,
#      "course2":"b.tech"},
#     {"name3":"priya",
#      "marks3":30,
#      "course3":"b.tech"}}


# #QUESTION 6
# class Person:
#     def details(self):
#         name=str(input("Enter your name"))
#         age=int(input("Enter age"))
# class teacher(Person):
#     def subject(self):
#         subject=str(input("Enter subject"))

# obj=teacher()
# obj.subject()  #Calling the child class with its object
# obj.details()  #Calling the parent class with child class object

    
    
#QUESTION 7
# li=[23,"hello",79,True]
# try:
#     a=int(input("Enter index"))
#     print(li[a])
# except Exception as e:
#   print(e)

#Question 8
# f=open("user.txt","r")
# print(f.read())
# f.close()


