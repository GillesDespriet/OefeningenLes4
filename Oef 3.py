import requests
import time


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