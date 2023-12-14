import requests
import webbrowser
from PIL import Image
from io import BytesIO

user_input = input("Geef een onderwerp op: ")
api_url = "https://newsapi.org/v2/everything?q=" + user_input +"&apiKey=304e485e2bc54d22a286e48671851384"
response = requests.get(api_url)
data = response.json()
results = data["articles"]
for article in results:
    print("Titel: ", article["title"])