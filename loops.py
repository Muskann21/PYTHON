#while loop
i=1
while i<10:
    print("hello world")
    i+=1
 #for loop(default start=0,default step=1)
for i in range(5):
    print("hello")
 
for i in range(2,5,1):
 print(i,"world")
#NESTED LOOP
for i in range(3):
  for j in range(2):
      print(i,"muskan")
      
 #nested loop(j depending on i)
for i in range(5):
  for j in range(i+1):
   print("*",end=" ")
  print()
print("  ")
for i in range (6,0,-1):
  for j in range(i-1):
    print("*",end=" ")
  print()
a=15
for i in range(6,0,-1):
  for j in range(i-1):
    a-=1
    print(a,end=" ")
  print()
b=0
for i in range(0,5,1):
  for j in range(i+1):
    b+=1
    print(b,end=" ")
  print()
  
  