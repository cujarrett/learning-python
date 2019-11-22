#!/usr/bin/env python
name = input("Name: ")
occupation = input("Occupation: ")
location = input("Location: ")
print("Hello {0}, being a {1} in {2} must be exciting.".format(name, occupation, location))

response = input("Is it?")
if (response in ("yes", "y", "yeah")):
  print("How exciting.")
elif (response in ("no", "n", "nope")):
  print("That's too bad.")
else:
  print("Yeah, I thought so.")

number1 = input("Enter a number: ")
number2 = input("Enter another number: ")
print(int(number1) + int(number2))
