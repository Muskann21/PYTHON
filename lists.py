# a=["hello",223,"world",3.5,True,"abc",1.1]
# print(a)
# print(type(a))
# print(len(a))
# print(a[3])
# print(a[-1])
# print(a[0])
# print(a[2][2])
# print(a[1:5])
# print(a[2:10:2])
# print(a[6:1:2])
# print(a[-7:-2])

# b=["abc",99,True,["hi","hello",[1,2,3,False]],1.1]
# # #   0     1  2   3                             4

# print(b[2])
# print(b[3][2])
# print(b[3][2][3])
# print(b[3][1][3])
# print(b[4])

import requests

def fetch_movie():
        a=input("enter movie name")
        url = f"https://www.omdbapi.com/?t={a}&apikey=fd70a16f"
        response = requests.get(url)
        data = response.json()
        if data["Response"] == "True":
            return {
                        "Title": data["Title"],
                        "Year": data["Year"],
                        "Genre": data["Genre"],
                        "Director": data["Director"],
                        "Plot": data["Plot"],
                        "Poster": data["Poster"]
                    }
        else:
            return {"error": "Movie not found."}
movie=fetch_movie()
print(movie)
# print("Title:", movie["Title"])
# print("Year:", movie["Year"])
# print("Genre:", movie["Genre"])
# print("Director:", movie["Director"])
# print("Plot:", movie["Plot"])
# print("Poster URL:", movie["Poster"])
