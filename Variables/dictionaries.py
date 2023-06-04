# Dictionaries - Diccionarios

# Create dictionary with dict().
dictionary_one = dict(name="Lucas", lastname="Dalto")

# Lists cannot be keys, only tuples, and in the case of sets we use frozenset.
dictionary_two = {("Dalto", "Lucas"): "Jajaj"}
dictionary_three = {frozenset(["Dalto", "Lucas"]): "Jajaj"}

# Creating dictionaries with fromkeys(), default value: none
dictionary_four = dict.fromkeys(["name", "lastname"])

# Created dictionaries with fromkeys(), changing the default value to "Jajaj"
dictionary_five = dict.fromkeys(["name", "lastname"], "Jajaj")

print(dictionary_five)