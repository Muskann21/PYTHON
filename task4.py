#QUESTION 1
color_name =["Black", "Red", "Maroon", "Yellow"]
color_code=["#000000", "#FF0000", "#800000", "#FFFF00"]
outcome=[]
for i in range(4):
    a={"color_name":color_name[i],"color_code":color_code[i]}
    outcome.append(a)
    
print (outcome)
#QUESTION 2
import random as rn
c=0
u=0
for i in range (5):
    a=rn.choice(["r","p","s"])
    user=input("Enter input r or s or p")
    if user==a:
        print("draw")
    elif user=="r" and a=="s":
        print("You won")
        u+=1
    elif user=="r" and a=="p":
        print("comp won")
        c+=1
    elif user=="p" and a=="s":
        print("comp won")
        c+=1
    elif user=="p" and a=="r":
        print("you won")
        u+=1
    elif user=="s" and a=="p":
        print("you won")
        u+=1
    elif user=="s" and a=="r":
        print("comp won")
        c+=1
    else:
        print("Invalid input")
print("comp score:",c)
print("user score",u)
if c>u:
    print("FINAL:YOU LOSE")
elif c<u:
    print("FINAL:YOU WON")
elif c==u:
    print("FINAL:DRAW")
    
    

    


