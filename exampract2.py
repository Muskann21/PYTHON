# a=0
# b=1
# c=0
# for i in range(0,5):
#     a=b
#     b=c
#     print(c)
#     c=a+b
# list=[]
# for i in range(0,5):
#     a=b
#     b=c
#     print(c)
#     list.append(c)
#     c=a+b
# print(list)
# x=list[0]
# for i in range(len(list)):
#     if(x<list[i]):
#         x=list[i]
# print(x)

# list=[1,2,3,4,5,6,7,8,8,7,6,5,4,5,6,7]
# done=[]
# for x in list:
#     y=0   
#     if x not in done:
#      for i in list:
#         if i==x:
#             y+=1
#      done.append(x)
#      print(x," present ",y," times")

# list=[1,9,4,6,5,2,5,3,1,3,7,8]
# for i in range(len(list)):
#     for j in range(i,len(list)):
#         if list[j]<list[i]:
#             list[i],list[j]=list[j],list[i]
# print(list)

# mat1=[[2,3],
#       [4,5]]
# mat2=[[1,3],
#       [4,5,]]
# res=[[0,0],
#      [0,0]]
# for i in range(len(mat1)):
#     for j in range(len(mat1)):
#       for k in range(len(mat1)):
#         res[i][j]+=mat1[i][k]*mat2[k][j]
#     print(res[i])

# abc="Muskan293,_9"
# v=0
# c=0
# d=0
# s=0
# abc=abc.lower()
# for i in abc:
#     if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
#         v+=1
#     elif (i>='a' and i<='z'):
#       c+=1
#     elif (i>='0' and i<='9'):
#       d+=1
#     else:
#         s+=1
# print(v,c,d,s)

# x=5
# fact=1
# while x>0:
#     fact*=x
#     x-=1
# print(fact)

# num=4567
# order=len(str(num))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit**order
#     num=num//10
# print(sum)
    
# def palin(num1):
#     num2=""
#     for i in str(num1):
#         num2=i+num2
#     print(int(num2))
#     if(num1==int(num2)):
#         print("it is a palindrome")
#     else:
#         print("it is not a palindrome")
# palin(8396)

# list=[1,2,3,4,5,6,7,8,9]
# even=[]
# odd=[]
# for i in list:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# for i in range(5):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#n=5
# for i in range(1,n+1):
#     spaces=n-i 
#     stars=2*i-1
#     print(" "*spaces+"*"*stars)

# for i in range(1,n+1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()

# sum=0
# for i in range(1,n+1):
#     sum=sum+(1/i)
# print(sum)

# x=1
# n=5
# sum=1
# for i in range(1,n+1):
#     y=1
#     for j in range(1,i+1):
#         y*=j
#     sum=sum+(x**i/y)
# print(sum)

# file=open("myfile.txt","w")
# file.write("Hello")
# file.close()
# file=open("myfile.txt","r")
# a=file.read()
# print(a)
# file.close()


 
        

