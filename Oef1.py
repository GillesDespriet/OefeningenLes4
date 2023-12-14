import requests
import webbrowser
from PIL import Image
from io import BytesIO
import os
import time

api_url = "https://jsonplaceholder.typicode.com/todos/4"
response = requests.get(api_url)
result = response.json()
print(result["title"])

result_status = result["completed"]
if result_status == False:
    print("Er moet nog werk worden gedaan.")
else:
    print("Goed gedaan!")

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

options = ['nsfw', 'religious', 'political', 'racist', 'sexist', 'explicit']
user_input = ''
input_message = "Pick an option:\n"
for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'
input_message += 'Your choice: '
while user_input.lower() not in options:
    user_input = input(input_message)
print('You picked: ' + user_input)

api_url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=" + user_input
response = requests.get(api_url)
result = response.json()
joke = result["setup"]
punchline = result["delivery"]
print(joke)
time.sleep(3)
print(punchline)