# List(be modified) - Lista(Se pueden Modificar)
list = ["G3kSec", "G3kSec G3kSec", True, 1.80]

# Tuple(cannot be modified) - Tupla(No se pueden Modificar)
tuple = ("G3kSec", "G3kSec G3kSec", True, 1.80, "Tuple")

# Set (Elements are not accessed by index, does not store duplicate data) - Conjunto (No se accede a elementos por índice, no almacena datos duplicados)
set = {"G3kSec", "G3kSec G3kSec", True, 1.80, "Set"}
#print(set[1]) -> (can't access element - no puede acceder al elemento)

#Dictionary (The structure is key: value) - Diccionario (La estructura es key: value)
dictionary = {
  'name': "G3kSec",
  'lastname': "G3kSec",
  'github': "@G3kSec",
  'age': 17,
  'duplicate_lastname': "G3kSec"
}
print(dictionary['age'])
