age = {}
age["Will"] = 42
age["Bob"] = 17
age["John"] = 20
print(age) # {"Will": 42, "Bob": 17, "John": 20}

print(age["Will"]) # 42
print(age["Bob"]) #17

"Will" in age # True
"Foo" in age # False

print(age.get("Will", "Will wasn't found")) # 42
print(age.get("Foo", "Foo wasn't found")) # Foo wasn't found

del age["Will"]
print(age.get("Will", "Will wasn't found")) # Will wasn't found

for key, value in age.items():
  print(key, value) # Bob 17\nJohn 20
