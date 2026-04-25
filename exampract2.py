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
list=[24,65,772,97,29,50,30,37]
x=list[0]
for i in range(len(list)):
    if(x<list[i]):
        x=list[i]
print(x)