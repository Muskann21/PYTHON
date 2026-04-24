# import requests

# url = "https://ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com/chat"

# querystring = {"noqueue":"1"}

# payload = {
# 	"message": "What are common brain tumors?",
# 	"specialization": "neurosurgery",
# 	"language": "en"
# }
# headers = {
# 	"x-rapidapi-key": "72ad99f0b9msh50f7b335fe3f616p1c9898jsnf21b793b55b1",
# 	"x-rapidapi-host": "ai-doctor-api-ai-medical-chatbot-healthcare-ai-assistant.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }

# response = requests.post(url, json=payload, headers=headers, params=querystring)

# print(response.json())



import requests

url = "https://ai-food-recipe-generator-api-custom-diet-quick-meals.p.rapidapi.com/generate"

querystring = {"noqueue":"1"}

payload = {
	"ingredients": ["macaroni", "onion", "carrot","flour","milk"],
	"dietary_restrictions": ["vegetarian"],
	"cuisine": "italian",
	"meal_type": "lunch",
	"servings": 4,
	"lang": "en"
}
headers = {
	"x-rapidapi-key": "72ad99f0b9msh50f7b335fe3f616p1c9898jsnf21b793b55b1",
	"x-rapidapi-host": "ai-food-recipe-generator-api-custom-diet-quick-meals.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.json())