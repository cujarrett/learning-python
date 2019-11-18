"The ball is red".endswith("red") # True

my_string = "The ball is red"
substring = "red"
my_string.endswith(substring) # True

"The ball is red".find("is") # 9

"The ball is red".find("foo") # -1

"The {0} is {1}".format("ball", "red") # "The ball is red"

"".join(["The ", "ball ", "is ", "red"]) # "The ball is red"

"Will     ".strip() # Will

# left side strip
"Will     ".lstrip() # Will
# right side strip
"Will     ".rstrip() # Will

# You can use the `dir` function on Python's CLI for more info on what API exists
# dir("foo")

# you can use the `help` function for help with a part of the API via the Python CLI
# help("foo".restrip)
