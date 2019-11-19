pets = ["cat", "dog", "elephant"]

for pet in pets:
  print(pet)
# cat\ndog\nelephant

for i in range(5):
  print(i)
# 0\n1\n2\n3\n4

for i in range(10, 15):
  print(i)
# 0\n10\n11\n12\n13\14

for i in range(0, 10, 2):
  print(i) # 0\n2\n4\n6\n8

for i in range(10, 0, -1):
  print(i)
# 10\n9\n8\n7\n6\n5\n4\n3\n2\n1

x = 1
while x < 10:
  print(x)
  x = x + 1
# 1\n2\n3\n4\n5\n6\n7\n8\n9

for pet in pets:
  if (pet == "dog"):
    print("dog found")
    break
  else:
    print("Found a {0}, but no dog".format(pet))
# Found a cat, but no dog\ndog found
