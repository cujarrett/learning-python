# Tuples are immutable

t = "dog", "cat", 12345
print(t) # ("dog", "cat", 12345)
print(t[0]) # "dog"
print(t[1]) # "cat"

print(id(t)) # 4368894304 (could be any number)
t = "dog", "cat", 12345, "foo"
print(id(t)) # 4368535472 (note, it's different than the previous id)
