from tkinter import *
from PIL import Image, ImageTk
from tkinter import Tk, Label
import requests
class Screen:
    def __init__(self):
        self.root = Tk()
        self.root.title("Home Page")
        self.a=self.root.winfo_screenheight()
        
        self.b=self.root.winfo_screenwidth()
        
        self.root.geometry(f"{self.b}x{self.a}")
        self.root.resizable(False,False)
        self.root.config(bg="#d1b796") 
        self.img=Image.open(r"C:\Users\muska\Desktop\PYTHON\TKNT\image.jpg")
        self.img=self.img.resize((self.b,self.a))
        self.img=ImageTk.PhotoImage(self.img)
        self.label=Label(self.root,image=self.img)
        self.label.place(x=0,y=0)
        self.label1=Label(self.root,text="Search for the movie",bg="#1e7fa1",fg="white",font=("Times New Roman",30,"bold"))
        self.label1.place(x=500,y=20)
        
        self.enter1=Entry(self.root,bg="white",fg="black",font=("Times New Roman",30,"bold"))
        self.enter1.place(x=300,y=80)
        self.button1=Button(self.root,text="Search",bg="#0E6C9C",fg="white",font=("Arial",20,"bold"),command=self.fetch_movie)
        self.button1.place(x=750,y=80)

        self.root.mainloop()

        
    def fetch_movie(self):
        a=self.enter1.get()
        url = f"https://www.omdbapi.com/?t={a}&apikey=fd70a16f"
        response = requests.get(url)
        data = response.json()
        if data["Response"] == "True":
            print(data)
            self.frame=Frame(self.root,bg="white",width=500,height=300)
            self.frame.place(x=300,y=140)
            self.la=Label(self.frame,text=data["Title"],font=("Times New Roman",20,"bold"))
            self.la.place(x=10,y=10)
            self.la1=Label(self.frame,text=("Year realeased:",data["Year"]),font=("Times New Roman",20,"bold"))
            self.la1.place(x=10,y=70)
            self.la1=Label(self.frame,text=("Runtime:",data["Runtime"]),font=("Times New Roman",20,"bold"))
            self.la1.place(x=10,y=120)
            self.la3=Label(self.frame,text=("imdb Rating:",data["imdbRating"]),font=("Times New Roman",20,"bold"))
            self.la3.place(x=10,y=160)
            
            return {
                        "Title": data["Title"],
                        "Year": data["Year"],
                        "Genre": data["Genre"],
                        "Director": data["Director"],
                        "Plot": data["Plot"],
                        "Poster": data["Poster"]
                    }
            
        else:
            
            self.la2=Label(self.root,text=("Movie not found."),font=("Times New Roman",20,"bold"))
            self.la2.place(x=300,y=140)
            print ("error:Movie not found.")
        
obj=Screen()
