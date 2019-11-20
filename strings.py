name = "will"
my_ball = "will's ball"

print(my_ball) # will's ball
multiline_var = """Will's ball
is red
and bouncy!"""

print(multiline_var) # Will's ball\nis red\nand bouncy!

item = "ball"
color = "red"
print("Will's %s is %s." % (item, color)) # Will's ball is red.
print("Will's {0} is {1}.".format(item,color)) # Will's ball is red.
print("Will's {1} is {1}.".format(item,color)) # Will's red is red.
