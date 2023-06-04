# Exercise One - Ejercicio Uno

# El timing para ver los conceptos vistos en python en un curso de corrido es de 
# 2.5hs como Mínimo, 7hs como Máximo y 4hs en Promedio. Este curso lo logro en 1.5hs.

# a) Cuánta diferencia en porcentaje entre el curso actual y:
# - El más rápido de otros cursos.
# - El más lento de otros cursos.
# - El promedio de los cursos.

# Teniendo en cuenta que el crudo de los demás cursos es de 5hs y con edición lo convierten en 4hs
# y el crudo de este curso 3.5hs y se redujo a 1.5hs
# b) Qué porcentaje de material inservible que se reduce en:
# - El promedio de los cursos.
# - El curso actual (este curso).

# c) Ver 10hs de este curso a cuantas de otros cursos equivalen?

mínimo = 2.5
máximo = 7
promedio = 4
este_curso = 1.5

# a)
print("-----------------------")
print("[+] Ejercicio 1 - (a):")

diferencia_uno = 100 - (este_curso / mínimo) * 100
print(f"El curso de dalto dura {diferencia_uno}% menos, que el más rapido de los otros cursos.")

diferencia_dos = 100 - este_curso * 1000 // máximo / 10
print(f"El curso de dalto dura {diferencia_dos}% menos, que el más lento de los otros cursos.")

diferencia_tres = 100 - (este_curso / promedio) * 100
print(f"El curso de dalto dura {diferencia_tres}% menos, que el promedio de los otros cursos.")

print("-----------------------")
# b)
print("[+] Ejercicio 1 - (b):")

crudo_promedio = 5
crudo_este_curso = 3.5
edicion_promedio = 4
edicion_este_curso = 1.5

promedio_cursos = 100 - (edicion_promedio / crudo_promedio) * 100
print(f"El crudo promedio se reduce un {promedio_cursos}%.")

este_cursos = 100 - edicion_este_curso * 1000 // crudo_este_curso / 10
print(f"El curso de dalto se reduce un {este_cursos}%.")

print("-----------------------")
# c)
print("[+] Ejercicio 1 - (c):")

print(f"Ver 10 horas de este curso equivale a ver {edicion_promedio * 100 // edicion_este_curso / 10 } horas de otros cursos.")

print(f"Ver 10 horas de otros cursos equivale a ver {edicion_este_curso * 100 // edicion_promedio / 10 } horas de este curso.")

print("-----------------------")