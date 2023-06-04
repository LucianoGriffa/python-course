# Iterate Sets - Iterar Conjuntos

# Iterating a set. (animals & numbers).
animals = {"cat", "dog", "lion", "tiger", "fish"}
for animal in animals:
  print(animal)

numbers = {10, 62, 42, 58}
for number in numbers:
  result = number * 10
  print(result)

# Iterating two or more set in only loop. (animals & numbers).
for number, animal in zip(numbers, animals):
  print(f"Iterating set 1: {number}")
  print(f"Iterating set 2: {animal}")

# Use range().
for num in range(5, 10):
  print(num)

# Optimal way to loop through a set.
for num in enumerate(numbers):
  index = num[0]
  value = num[1]
  print(f"The index is {index} and value is: {value}")

# Using else.
for number in numbers:
  print(f"Value: {number}")
else:
  print(f"The loop ended")