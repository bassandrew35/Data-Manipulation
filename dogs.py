import requests, json

#loads all data from dog api
dog = requests.get(
    'https://api.thedogapi.com/v1/breeds',
    headers={'x-api-key': ''} #needs key
)

#formats data and writes it to a file
file = open("data.txt", "w")
dog_json = json.loads(dog.text)
dog_json_str = json.dumps(dog_json, indent = 2)
print(dog_json_str)
file.write(dog_json_str)
file.close()
