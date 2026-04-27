#Sum of digits
# num=957
# sum=0
# a=num
# while a!=0:
#   a=num%10
#   sum+=a
#   num=num//10
# print(sum)
# num=957
# x=str(num)
# sum=0
# for i in x:
#     b=int(i)
#     sum+=b
# print (sum)
# a=3965
# b=490
# c=95
# if(a>b):
#     if(a>c):
#         print("a is greatest")
#     else:
#         print("c is greatest")
# else:
#     if(b>c):
#         print ("b is greatest")
#     else:
#         print("c is greatest")
# a=5
# fact=1
# while a>0:
#     fact*=a
#     a=a-1
# print (fact)
# num=2
# count=0
# i=1
# while i<=num:
#     if(num%i==0):
#         count+=1
#     i+=1
# if(count==2):
#     print("it is prime")
# else:
#     print("not prime")
# num=98445678
# x=0
# while num>0:
#     num=num//10
#     x+=1
# print(x)
# def fact(n):
#    if n==0 or n==1:
#        return 1
#    else:
#        return n*fact(n-1)
# print(fact(4))
# num1=567
#num2=768980
# sum=0
# while num1>0:
#     x=num1%10
#     temp=num2
#     while temp>0:
#         y=temp%10
#         if(x==y):
#             sum+=x
#         temp=temp//10
#     num1=num1//10
# print(sum)
# a=0
# while num2>0:
#     x=num2%10
#     if(x>a):
#         a=x
#     num2=num2//10
# print(a)
# list=[2,5,2,7,9,5,3,7]
# x=0
# for i in list:
#     x+=i
# print(x)
num=11
for i in range(2,num):
    if(num%i==0):
        print("not prime")
        break
else:
    print("prime")