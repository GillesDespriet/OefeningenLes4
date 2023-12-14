import requests
import webbrowser
from PIL import Image
from io import BytesIO

api_url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(api_url)
result = response.json()
result = result["message"]
print(result)
webbrowser.open(result)

output = requests.get(result)
local_path = "c:\\users\{user}\desktop\image.jpg"
image = Image.open(BytesIO(output.content))
image.save(local_path)