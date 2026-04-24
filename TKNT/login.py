
from tkinter import *
from tkinter import messagebox
import homepg
class register:
    def __init__(self):
        self.root=Tk()
        self.root.title("LOGIN PAGE")
        self.root.geometry("400x600")
        self.root.config(bg="#c8cacb")
        self.root.resizable(False,False)
        self.label1=Label(self.root,text="LOGIN",bg="#1e7fa1",fg="white",font=("Times New Roman",30,"bold"))
        self.label1.place(x=130,y=50)
        self.label2=Label(self.root,text="First Name:",bg="#c8cacb",fg="black",font=("Arial",10))
        self.label2.place(x=50,y=100)
        self.enter1=Entry(self.root,bg="white",fg="black",font=("Arial",15))
        self.enter1.place(x=50,y=130)
        self.label3=Label(self.root,text="Last Name:",bg="#c8cacb",fg="black",font=("Arial",10))
        self.label3.place(x=50,y=160)
        self.enter2=Entry(self.root,bg="white",fg="black",font=("Arial",15))
        self.enter2.place(x=50,y=190)
        self.label4=Label(self.root,text="Email:",bg="#c8cacb",fg="black",font=("Arial",10))
        self.label4.place(x=50,y=220)
        self.enter3=Entry(self.root,bg="white",fg="black",font=("Arial",15))
        self.enter3.place(x=50,y=250)
        self.label5=Label(self.root,text="Password(6 or more characters)",bg="#c8cacb",fg="black",font=("Arial",10))
        self.label5.place(x=50,y=280)
        self.enter4=Entry(self.root,show="*",bg="white",fg="black",font=("Arial",15))
        self.enter4.place(x=50,y=310)
        self.label5=Label(self.root,text="By clicking on Join now,you agree to our",bg="#c8cacb",fg="black",font=("Arial",10))
        self.label5.place(x=50,y=340)
        self.label5=Label(self.root,text="User Agreement ",bg="#c8cacb",fg="black",font=("Arial",10,"bold"))
        self.label5.place(x=290,y=340)
        self.label6=Label(self.root,text="Privacy Policy, and Cookie Policy",bg="#c8cacb",fg="black",font=("Arial",10,"bold"))
        self.label6.place(x=100,y=360)
        self.button1=Button(self.root,text="         Join Now         ",bg="#0E6C9C",fg="white",font=("Arial",20,"bold"),command=self.show)
        self.button1.place(x=50,y=390)
        self.root.mainloop()
    def show(self):
        a=(self.enter1.get())
        b=(self.enter2.get())
        c=(self.enter3.get())
        d=(self.enter4.get())    
        if a=="" or b=="" or c=="" or d=="":
            messagebox.showwarning("warning","Enter all the details")
        else:
            print(self.enter1.get())
            print(self.enter2.get())
            print(self.enter3.get())
            print(self.enter4.get())
            messagebox.showinfo("Success", "You have successfully logged in")
            self.root.destroy()
            homepg.Screen()
            
            
        
obj=register()