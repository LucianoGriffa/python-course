# Exercise 1.2 - Ejercicio 1.2

# Suponiendo que cada persona promedio habla 2 palabras por segundo.

# a) Pedirle al usuario que diga cualquier texto real y:
# - Calcular cuanto taradaría en decir esa frase.
# - ¿Cuantas palabras dijo?

# b) Si tarda más de 1 minuto:
# - Decirle: "para flaco tampoco te pedí un testamento".

# c) Cuanto tardaria Dalto en decirlo, ya que habla un 30% más rápido?

# a.1)
cadena = input("Ingrese cualquier frase o texto real: ")
convirtiendo_en_lista = cadena.split(" ")
cantidad_de_palabras = len(convirtiendo_en_lista)

# b)

if cantidad_de_palabras > 120:
  print("--------------------------------------------")
  print("[+] Para flaco tampoco te pedi un testamento")
  print("--------------------------------------------")
else:
  print("--------------------------------------------")
  # a.2)
  print(f"[+] Hubo {cantidad_de_palabras} palabras en la cadena que ingresaste, y tardarias {cantidad_de_palabras / 2} segundos en decirlo.")
  # c)
  print("--------------------------------------------")
  print(f"[+] Dalto lo diria en {cantidad_de_palabras / 2 * 1.3} segundos en decirlo.")
  print("--------------------------------------------")