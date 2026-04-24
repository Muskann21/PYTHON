a="hello world"
#printing a using string functions
b=len(a)
for i in range (b):
    print(a[i])
#printing a using traversing
for i in a:
    print(i)
#counting vowels using string functions
x=a.count("a")
e=a.count("e")
i=a.count("i")
o=a.count("o")
u=a.count("u")
print("No. of vowels=",x+e+i+o+u)
#printing no. of vowels using traversing
x=0   
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
       x+=1
print("No. of vowels=",x)
#input string by user
x=str(input("Enter a string value"))
z=0
for i in x:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        z=z+1
    
print("total number of vowels are",z)

