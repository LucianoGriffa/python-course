# More iterations - Más Iteraciones

fruits = ["Banana", "Apple", "Pear", "Orange", "Peach"]

for fruit in fruits:
  if fruit == 'Apple':
    continue;
  print(f'Fruit: {fruit}')

for fruit in fruits:
  print(f'Fruit: {fruit}')
  if fruit == 'Pear':
    break;
print(f'Loop ended')

# Iterate a String
string = "Hello World!"
for letter in string:
  print(letter)

# Loop in only line
numbers = [2, 5, 8, 10]
numbers_duplicate = [x*2 for x in numbers] # Loop
print(numbers_duplicate)