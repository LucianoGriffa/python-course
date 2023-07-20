# List(be modified) - Lista(Se pueden Modificar)
list = ["LucianoGriffa", "LucianoGriffa LucianoGriffa", True, 1.80]

# Tuple(cannot be modified) - Tupla(No se pueden Modificar)
tuple = ("LucianoGriffa", "LucianoGriffa LucianoGriffa", True, 1.80, "Tuple")

# Set (Elements are not accessed by index, does not store duplicate data) - Conjunto (No se accede a elementos por índice, no almacena datos duplicados)
set = {"LucianoGriffa", "LucianoGriffa LucianoGriffa", True, 1.80, "Set"}
#print(set[1]) -> (can't access element - no puede acceder al elemento)

#Dictionary (The structure is key: value) - Diccionario (La estructura es key: value)
dictionary = {
  'name': "LucianoGriffa",
  'lastname': "LucianoGriffa",
  'github': "@LucianoGriffa",
  'age': 17,
  'duplicate_lastname': "LucianoGriffa"
}
print(dictionary['age'])
