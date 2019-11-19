# Lists can be made of single or mixed types
a = [1, 2, 3]
b = [1, "cat", 7, {"car": "Honda"}]

b[0] # 1
b[1] # "cat"

pets = []
pets.append("cat")
pets.append("dog")
pets.append("bear")
pets.append("shark")
print(pets) # "cat", "dog", "bear", "shark"

pets.remove("dog")
print(pets) # "cat", "bear", "shark"

# pop removes the last element of the list
pets.pop()
print(pets) # "cat", "bear"

# pop takes an optional argument detailing what element to remove
pets(0)
print(pets) # "bear"

pets = ["cat", "dog", "bear", "shark"]
pers.sort()
print(pets) # "bear", "cat", "dog", "shark"

pets.reverse()
print(pets) # "shark", "dog", "cat", "bear"

len(pets) # 4

pets.count("bear") # 1
