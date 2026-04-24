#QUESTION 1
a=[1,"hello","muskan",232,34.8,True,False,"TRUE",89,"100"]
print(a)
#QUESTION 2
a=[1,10,100,3,6,8]
a.insert(3,"59")
a.append("5")
print(a)
print(len(a))
#QUESTION 3
a=[1,10,100,3,6,8,97,75,60]
print(a[::2])
#QUESTION 4
a=["Gaurav",12,23,33.33,"Sharma",True]  
li=[i for i in a if type(i)==str]
print(li)
#Question 5
sum=0
for i in a:
 if type(i) == int or type(i) == float:
    sum+=i
print(sum)
#QUESTION 6
li1=["muskan","sanya","isha","riya","jiya"]
x=str(input("Enter a friend name"))
li1.append(x)
print(li1)
y=str(input("Enter most important friend name"))
z=int(input("Enter location of most important friend"))
li1[z]=y
print(li1)
