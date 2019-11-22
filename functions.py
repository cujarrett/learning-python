def say_name(name):
  """
  Returns name passed in as a parameter
  """
  return name

foo = say_name("Heisenberg")
print(foo)

#variables are block scoped
def add(number1 = 1, number2 = 2):
  return number1 + number2
number1 = add(1, 2)
print(number1) # 3

def madlibs(name, noun = "shoes", adjective = "red"):
  return "{0} has {1} {2}".format(name, adjective, noun)
madlib = madlibs("Will", adjective="black", noun="boots")
print(madlib) # Will has black boots