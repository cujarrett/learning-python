animals = { "monkey", "bear", "dog", "monkey", "cat", "bear", "gorilla" }
print(animals) # {"bear", "dog", "monkey", "cat", "gorilla"}

"monkey" in animals # True
"shark" in animals # False

# You can only make an empty set with set()
fish = set()
fish.add("shark")
fish.add("guppy")
fish.add("whale")
print(fish) # {"whale", "guppy", "shark"}

fish.remove("whale")
print(fish) # {"guppy", "shark"}

combined_animals = fish.union(animals)
print(combined_animals) # {"gorilla", "monkey", "bear", "guppy", "shark", "cat", "dog"} ƒ
