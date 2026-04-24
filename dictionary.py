a={"name":"Avengers",
   "hero":"Ironman",
    "villain":"Thanos",
    "year":2018,
    200:"Cost",
    "hero":"Captain America",
    300:"Income",
    "Success":True}
print(a)
print(type(a))
print(len(a))
print(a["name"])
print(a[200])
print(a["Success"])
print(a["hero"])
dic={
    "movies":["Avengers","Ironman","Inception","Interstellar"],
    "hero":("RJD","RJD","Leonardo"),
    "year":[2018,2008,2010,2014],
    "Success":True,
    4000:"Cost",
    5000:"Income"
}

print(dic)
print(type(dic))
print(len(dic))
print(dic["movies"])
print(dic[4000])
print(dic["Success"])
print(dic["movies"][2])
print(dic["hero"][2])

a={"name":"Avengers",
   "hero":"Ironman",
    "villain":"Thanos",
    "year":2018,
    200:"Cost",
    "hero":"Captain America",
    "Income":300,
    "Success":True}


print(a.get("name"))

a.update({"name":"Avengers Endgame"})
print(a)

a.pop(200)
print(a)

print(a.keys())
print(a.values())
print(a.items())

a["hero"]="Hulk"
print(a)

a["heroine"]="Black Widow"  
print(a)


for i in a:
    print(i,a[i])

for i in a.values():
    print(i)

for i in a.keys():
    print(i)

for i in a.items():
    print(i)

for i,j in a.items():
    print(i,j)
    
for i in a:
    if type(a[i])==int :
        print(i,a[i])


dic={}

for i in range(3):
    key=input("enter key ")
    val=input("enter value ")
    dic[key]=val

print(dic)