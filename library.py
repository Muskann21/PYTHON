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
print("compuet score:",c)
print("user score",u)
if c>u:
    print("FINAL:YOU LOSE")
elif c<u:
    print("FINAL:YOU WON")
elif c==u:
    print("FINAL:DRAW")
    
    

    


