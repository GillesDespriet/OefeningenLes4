import requests

api_url = "https://jsonplaceholder.typicode.com/todos/4"
response = requests.get(api_url)
result = response.json()
print(result["title"])

result_status = result["completed"]
if result_status == False:
    print("Er moet nog werk worden gedaan.")
else:
    print("Goed gedaan!")