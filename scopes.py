def whoAmI():

  def localWhoAmI():
    i = "I am local groot"
    print(i) # I am local groot

  def nonlocalWhoAmI():
    nonlocal i
    i = "I am nonlocal groot"
    print(i) # I am nonlocal groot

  def globalWhoAmI():
    global i
    i = "I am global groot"
    print(i) # I am global groot

  i = "I am groot"
  print (i) # I am groot
  localWhoAmI()
  print (i) # I am groot
  nonlocalWhoAmI()
  print (i) # I am nonlocal groot
  globalWhoAmI()
  print (i) # I am nonlocal groot
whoAmI()
print(i) # I am global groot
