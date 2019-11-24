f = open("sample-file.csv")

for line in f:
  print(line)
f.close()

# Automically close file after use
with open("sample-file.csv") as f:
  print(f.read())

# CSV example
import csv
with open("sample-file.csv") as f:
  animals = csv.reader(f)
  for row in animals:
    if(row[-1] == "True"):
      print("{0} is a {1} and is housebroken".format(row[0], row[1]))
    elif(row[-1] == "False"):
      print("{0} is a {1} and is not housebroken".format(row[0], row[1]))

# JSON example
import json
with open("sample-file.json") as f:
  data = json.load(f)
  for row in data:
    print(row["name"])
