# Lambda Functions - Funciones Lambda

numbers = [1,2,3,4,5,6,7,8,9]

# Creating a function to multiply by two
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(10))

# Creating a function that tells if a number is even or not
def es_par(num):
  if(num % 2 == 2):
    return True

# Using filter with a common function
numeros_pares = filter(es_par, numbers)

# Creating the same but with lambda
numeros_pares = filter(lambda numero:numero % 2 == 0, numbers)

print(list(numeros_pares))
