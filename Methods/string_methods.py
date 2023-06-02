# String Methods - Métodos de Cadenas

cadena = "Hola, Maquina! ¿Cómo Estás?"

# dir(): Muestra los atributos y métodos disponibles para un objeto
print(dir(cadena))

# lower(): Convierte la cadena a minúsculas
print(cadena.lower())  # "hola, maquina! ¿cómo estás?"

# upper(): Convierte la cadena a mayúsculas
print(cadena.upper())  # "HOLA, MAQUINA! ¿CÓMO ESTÁS?"

# capitalize(): Convierte la primera letra de la cadena a mayúscula y el resto a minúsculas
print(cadena.capitalize())  # "Hola, maquina! ¿cómo estás?"

# isalpha(): Verifica si la cadena contiene solo caracteres alfabéticos
print(cadena.isalpha())  # False

# split(): Divide la cadena en una lista de subcadenas utilizando un delimitador
print(cadena.split())  # ['Hola,', 'Maquina!', '¿Cómo', 'Estás?']

# replace(): Reemplaza una subcadena por otra en la cadena original
print(cadena.replace("Estás", "Hola"))  # "Hola, Maquina! ¿Cómo Hola?"

# endswith(): Verifica si la cadena termina con una subcadena específica
print(cadena.endswith("?"))  # True

# startswith(): Verifica si la cadena comienza con una subcadena específica
print(cadena.startswith("Hola"))  # True

# len(): Devuelve la longitud (cantidad de caracteres) de la cadena
print(len(cadena))  # 23

# count(): Cuenta las ocurrencias de una subcadena en la cadena
print(cadena.count("a"))  # 4

# isnumeric(): Verifica si la cadena contiene solo caracteres numéricos
print(cadena.isnumeric())  # False

# index(): Devuelve la posición de la primera aparición de una subcadena en la cadena
print(cadena.index("Maquina"))  # 6

# find(): Busca la primera aparición de una subcadena en la cadena y devuelve su posición (-1 si no se encuentra)
print(cadena.find("¿"))  # 16
