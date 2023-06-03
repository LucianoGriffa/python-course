# Inputs
# Siempre nos va a devolver un texto/string.

# Obtener una cadena de texto desde el usuario:
texto = input("Ingresa una cadena de texto: ")
print("El texto que ingresaste es:", texto)

# Obtener un float o número decimal desde el usuario
numero_decimal = float(input("Ingresa un número decimal: "))
print("El número decimal que ingresaste es:", numero_decimal)

# Obtener un int o número entero desde el usuario
number = int(input("Ingresa un número entero: "))
print("El número entero que ingresaste es:", number)

# Obtener varios valores en una sola línea separados por espacios y almacenarlos en una lista:
valores = input("Ingresa varios valores separados por espacios: ").split()
print("Los valores que ingresaste son:", valores)

# Obtener varios números en una sola línea separados por comas y almacenarlos en una lista de enteros:
numeros = [int(x) for x in input("Ingresa varios números separados por comas: ").split(",")]
print("Los números que ingresaste son:", numeros)