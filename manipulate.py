import json

file = open("data.txt", "r")    # gets the data from file
data = file.read()
data = json.loads(data)         # loads data into json format
file.close()
file = open("data2.txt", "w")
file.write("Dog Breads: \n")

for a in data:                  # gets each name field and writes to another file
    print(a["name"])
    file.write(a["name"])
    file.write("\n")

file.close()
