# Andrew Bass
# 6/17/21

import json

# opens dog data file and loads data into variable
file = open("data.txt", "r")
text = file.read()
json_str = json.loads(text)

# finds the data for beagle and changes the ID for the beagle
for a in json_str:
    if a["name"] == "Beagle":
        a["id"] = 99999

# opens output file
file.close()
file = open("data2.txt", "w")

# formats data
json_str = json.dumps(json_str, indent = 2)

# outputs changed data
print(json_str)
file.write(json_str)
