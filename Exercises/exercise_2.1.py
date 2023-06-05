# Exercise 2.1 - Ejercicio 2.1

# Hoy falto el profesor de clase y los chicos se organizaron para armar la suya propia.
# 1 Alumno va a ser el profesor.
# 1 Alumno va a ser su asistente.

# a) Pedir el nombre y la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor.

# b) El mayor de la clase es el profesor y el menor es el asistente: ¿Quién es quien?

def get_students(students_quantity):
  students = []
  for i in range(students_quantity):
    name = input("Ingrese el nombre de tu compañero: ")
    age = int(input("Ingrese la edad de tu compañero: "))
    student = (name, age)
    students.append(student)
  students.sort(key=lambda x:x[1])
  assitant = students[0][0]
  teacher = students[-1][0]
  return assitant,teacher

while True:
  inputInitial = int(input("Ingrese la cantidad de alumnos: "))
  assitant,teacher = get_students(inputInitial)
  print(f"El asistente es {assitant}")
  print(f"El profesor es {teacher}")
else:
  print("¡Ingrese un número!")