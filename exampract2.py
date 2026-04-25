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

