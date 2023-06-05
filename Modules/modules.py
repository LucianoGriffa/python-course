import good_functions.greet_modules as greet;
name = "Dalto"
print(f"{greet.greetRari(name)}, Modulo: {greet.__name__}")

# Cuando el modulo esta fuera de la carpeta. "O para atras".
# import sys
# Para agregar una ruta a sys.path. Seria: sys.path.append("c:\\tata\\tata\\tata\\tata").
# Para importar la ruta agragada. Directamente con import [modulo].