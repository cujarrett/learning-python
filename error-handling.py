import sys
try:
  print(int(sys.argv[1]) / int(sys.argv[2]))
except ValueError as error:
  print("You must enter a valid number")
except ZeroDivisionError as error:
  print("You can't divide by zero")
