# List Methods - Métodos de Listas

lista = [1, 3, 5, 7, 9]

# list(): Crea una lista a partir de un objeto iterable
nueva_lista = list("Hola")  # ['H', 'o', 'l', 'a']

# len(): Devuelve la longitud (cantidad de elementos) de la lista
print(len(lista))  # 5

# append(): Agrega un elemento al final de la lista
lista.append(11)
print(lista)  # [1, 3, 5, 7, 9, 11]

# insert(): Inserta un elemento en una posición específica de la lista
lista.insert(2, 4)
print(lista)  # [1, 3, 4, 5, 7, 9, 11]

# extend(): Agrega los elementos de otra lista al final de la lista actual
lista.extend([13, 15])
print(lista)  # [1, 3, 4, 5, 7, 9, 11, 13, 15]

# pop(): Elimina y devuelve el último elemento de la lista (o un elemento en una posición específica)
elemento_eliminado = lista.pop()
print(elemento_eliminado)  # 15
print(lista)  # [1, 3, 4, 5, 7, 9, 11, 13]

# remove(): Elimina la primera aparición de un elemento en la lista
lista.remove(4)
print(lista)  # [1, 3, 5, 7, 9, 11, 13]

# clear(): Elimina todos los elementos de la lista
lista.clear()
print(lista)  # []

# sort(): Ordena los elementos de la lista en orden ascendente
otra_lista = [9, 2, 7, 4, 1]
otra_lista.sort()
print(otra_lista)  # [1, 2, 4, 7, 9]

# reverse(): Invierte el orden de los elementos en la lista
otra_lista.reverse()
print(otra_lista)  # [9, 7, 4, 2, 1]
