import json

with open("metadado.json") as my_json:
    data = json.load(my_json)

print(data)