# w write mode creates the file from scratch every time
# a write mode appends to the current file every time
f = open("sample-output-file.txt", "w")
cars = ["Chevy", "Tesla", "Ford"]
for car in cars:
  f.write(car + "\n")
f.close()

# Can create a with block to automically close the file when done
with open("sample-output-file.txt", "w") as f:
  cars = ["Chevy", "VW", "Mazda"]
  for car in cars:
    f.write(car + "\n")

# Note the closing of a file is when it's written out to

cars = [
  { "make": "Chevy" },
  { "make": "Tesla" },
  { "make": "Porsche" }
]

import json
with open("sample-output.json", "w") as f:
  json.dump(cars, f)
