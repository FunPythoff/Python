import requests
import pprint

response = requests.get('https://jsonplaceholder.typicode.com/posts/11')

if (response.status_code != requests.codes.ok):
    print("As far as I see - something went wrong.")
else:
    print(pprint.pprint(response.json()))


requestBody = {
    'title' : "Its my title",
    'body' : "Here is my text in body",
    'userId' : 2

}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=requestBody)

if (response.status_code != requests.codes.created):
    print("As far as I see - something went wrong.")
else:
    print(pprint.pprint(response.json()))

