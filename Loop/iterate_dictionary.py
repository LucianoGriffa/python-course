# Iterate Dictionary - Iterar Diccionario

dictionary = {
  "name": "Lucas",
  "lastname":"Dalto",
  "subs": 1000000
}

# Looping through the dictionary to get the keys
for key in dictionary:
  key
  print(f"The key is: {key}")

# Iterating dictionary with items() to get keys and values
for data in dictionary.items():
  key = data[0]
  value = data[1]
  print(f"The key is: {key} and the value is: {value}")