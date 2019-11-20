zoo_animals = ["giraffe", "monkey", "elephant", "lion", "bear", "pig", "horse", "aadvark"]
my_animals = ["monkey", "bear", "pig"]

not_my_animals = []
for animal in zoo_animals:
  if (animal not in my_animals):
    not_my_animals.append(animal)
print(not_my_animals) # ["giraffe", "elephant", "lion", "horse", "aadvark"]


other_animals = [animal for animal in zoo_animals if animal not in my_animals]
print(other_animals) # ["giraffe", "elephant", "lion", "horse", "aadvark"]

sales = [3.14, 7.99, 10.99, 0.99, 1.24]
sales_with_tax = []
for sale in sales:
  sales_with_tax.append(sale * 1.07) # [3.3598000000000003, 8.5493, 11.759300000000001, 1.0593000000000001, 1.3268]
print(sales_with_tax)

sales_with_tax = [sale * 1.07 for sale in sales]
print(sales_with_tax) # [3.3598000000000003, 8.5493, 11.759300000000001, 1.0593000000000001, 1.3268]

new2 = [
  animal
  for animal in zoo_animals
  if (animal not in my_animals)
]
print(new2) # ["giraffe", "elephant", "lion", "horse", "aadvark"]