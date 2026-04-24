# class fun:
#     def area(self):
#         a=int(input("Enter len"))
#         b=int(input("Enter breadth"))
#         c=a*b
#         print("Area is ",c)
# obj=fun()
# obj.area()

# #Inheritance 
# class parent:
#     def vol(self):
#         r=int(input("Enter radius"))
#         h=int(input("Enter height"))
#         vol=3.14*r*r*h
#         print("Vol is ",vol)
# class child(parent):
#     def area(self):
#         r=int(input("Enter radius"))
#         h=int(input("Enter height"))
#         area=3.14*r*h
#         print("Area is ",area)
# obj1=child()
# obj1.area()
# obj1.vol()


#POLYMORPHISM
class base:
    def vol(self):
        r=int(input("Enter radius"))
        h=int(input("Enter height"))
        vol=3.14*r*r*h
        print("Vol is ",vol)
class derv:
    def vol(self):
        l=int(input("Enter length"))
        b=int(input("Enter breadth"))
        h=int(input("Enter height"))
        vol=l*b*h
        print("Vol is ",vol)
        
obj=base()
obj.vol()

obj1=derv()
obj1.vol()