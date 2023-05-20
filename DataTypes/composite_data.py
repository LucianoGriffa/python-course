# List(be modified) - Lista(Se pueden Modificar)
list = ["Luciano", "Luciano Griffa", True, 1.80]

# Tuple(cannot be modified) - Tupla(No se pueden Modificar)
tuple = ("Luciano", "Luciano Griffa", True, 1.80, "Tuple")

# Set (Elements are not accessed by index, does not store duplicate data) - Conjunto (No se accede a elementos por índice, no almacena datos duplicados)
set = {"Luciano", "Luciano Griffa", True, 1.80, "Set"}
#print(set[1]) -> (can't access element - no puede acceder al elemento)

#Dictionary (The structure is key: value) - Diccionario (La estructura es key: value  )
dictionary = {
  'name': "Luciano",
  'lastname': "Griffa",
  'github': "@lucianogriffa",
  'age': 17,
  'duplicate_lastname': "Griffa"
}
print(dictionary['age'])