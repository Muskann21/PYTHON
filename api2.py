import requests

def fetch_movie(title):
	url = f"https://www.omdbapi.com/?t={title}&apikey=fd70a16f"
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
movie=fetch_movie("Dangal")
print("Title:", movie["Title"])
print("Year:", movie["Year"])
print("Genre:", movie["Genre"])
print("Director:", movie["Director"])
print("Plot:", movie["Plot"])
print("Poster URL:", movie["Poster"])