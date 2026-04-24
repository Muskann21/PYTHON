from tkinter import *
import random as rn
from tkinter import messagebox
class page:
    def __init__(self):
        self.root=Tk()
        self.root.title("Gambling Game")
        self.root.geometry("1000x600")  
        self.root.resizable(False,False)
        self.root.config(bg="blue")
        self.frame=Frame(self.root,bg="#aaf9f1",width=500,height=600)
        self.frame.place(x=250,y=0)
        self.label1=Label(self.frame,text="Dice",fg="red",font=("Times New Roman",30,"bold"))
        self.label1.place(x=180,y=30)
        self.label2=Label(self.frame,text="Player 1",bg="#aaf9f1",fg="red",font=("Times New Roman",20,"bold"))
        self.label2.place(x=40,y=100)
        self.enter=Entry(self.frame,bg="#aaf9f1",fg="red",font=("Times New Roman",20,"bold"))
        self.enter.place(x=180,y=100)
        self.label3=Label(self.frame,text="Player 2",bg="#aaf9f1",fg="red",font=("Times New Roman",20,"bold"))
        self.label3.place(x=40,y=150)
        self.enter2=Entry(self.frame,bg="#aaf9f1",fg="red",font=("Times New Roman",20,"bold"))
        self.enter2.place(x=180,y=150)
        self.label4=Label(self.frame,text="Player 3",bg="#aaf9f1",fg="red",font=("Times New Roman",20,"bold"))
        self.label4.place(x=40,y=200)
        self.enter3=Entry(self.frame,bg="#aaf9f1",fg="red",font=("Times New Roman",20,"bold"))
        self.enter3.place(x=180,y=200)
        self.label5=Label(self.frame,text="Player 4",bg="#aaf9f1",fg="red",font=("Times New Roman",20,"bold"))
        self.label5.place(x=40,y=250)
        self.enter4=Entry(self.frame,bg="#aaf9f1",fg="red",font=("Times New Roman",20,"bold"))
        self.enter4.place(x=180,y=250)
        self.button1=Button(self.frame,text="Submit",bg="#aaf9f1",fg="red",font=("Arial",20,"bold"),command=self.show)
        self.button1.place(x=180,y=350)
        self.root.mainloop()
    def show(self):
        li=["1","2","3","4","5","6"]
        x=rn.choice(li)
        a=(self.enter.get())
        b=(self.enter2.get())
        c=(self.enter3.get())
        d=(self.enter4.get())
        if a==x:
            messagebox.showinfo("info","Player 1 won")
        elif b==x:
             messagebox.showinfo("info","Player 2 won")
        elif c==x:
             messagebox.showinfo("info","Player 3 won")
        elif d==x:
             messagebox.showinfo("info","Player 4 won")
        else:
             messagebox.showinfo("info","Everyone Lost")
        self.root.destroy()   
        
obj=page()