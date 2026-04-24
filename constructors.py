class abc:
    def __init__(self):
        print("This is a constructor")
    def fun(self):
        print("This is a function")
obj=abc()
obj.fun()

class bank:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Welcome to bank ",a)
        print("Your balance is ",b)
        while True:
            x=int(input("Enter 1 for deposit,2 for withdraw and 3 for exit"))
            if x==1:
                y=int(input("Enter amount to be deposited"))
                self.deposit(y)
            elif x==2:
                z=int(input("Enter amount to be withdrawn"))
                self.withdraw(z)
            elif x==3:
                print("THANKYOU!!!")
                break
            else:
                print("Invalid input")
    def deposit(self,x):
        self.b=self.b+x
        print("New bank balance after deposit is ",self.b)
    def withdraw(self,x):
        self.b=self.b-x
        print("New bank balance after withdrawing is ",self.b)
obj=bank("Muskan",1234567890)
