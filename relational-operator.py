# Basics
5 == 5 # True
5 == 4 # False
5 != 4 # True
5 > 3 # True
3 < 5 # True
5 >= 3 # True
5 >= 5 # True
[1,2,4] > [1,2,3] # True
1 < 2 and 5 > 4 # True
(1 < 2) and (5 > 4) # True
1 > 2 or 5 > 4 # True

#Chainging
x = 4
x > 3 and x < 5 # True
3 < x < 5 # True

# isinstance
isinstance("Will", str) # True
isinstance("Will", int) # False
isinstance(4.0, float) # True

# is operator checks for exact match
a = True
b = True
a is b # True, the id for a and b are the same

x = [1,2,3]
y = [1,2,3]
x is y # False, the id for x and y are different

# in
x = [1,2,3]
3 in x # True
5 in x # False

x = [1,2,3]
for value in x:
  if (value == 2):
    print("Value is 2") # Value is 2

car = { "model": "chevy", "year": 1970, "color": "red" }
if ("model" in car):
  print("This is a {0}".format(car["model"])) # This is a chevy
