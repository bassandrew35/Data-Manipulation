import requests, json

dog = requests.get(
    'https://api.thedogapi.com/v1/breeds',
    headers={'x-api-key': '46b14ce1-ccf5-45a4-a200-66f2cebda9ed'}
)

file = open("data.txt", "w")

dog_json = json.loads(dog.text)

dog_json_str = json.dumps(dog_json, indent = 2)

print(dog_json_str)

file.write(dog_json_str)
