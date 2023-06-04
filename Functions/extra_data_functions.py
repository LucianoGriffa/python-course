
# Creating function from 3 parametres
def frase(name, lastname, adj):
  return print(f'Hola {name} {lastname}, sos muy {adj}')

# Using keyword arguments
frase_resultante = frase(lastname="Dalto", name="Lucas", adj="capo")


# Creating the same function with an optional parameter and a default value
def frase(name, lastname, adj="Tonto"):
  return print(f'Hola {name} {lastname}, sos muy {adj}')

# Using keyword arguments
frase_resultante = frase("Lucas", "Dalto", "capo")