# Create Functions - Crear Funciones

# Creating a Simple Function
# def greet():
#  print("¡Hello Lucas!")
# greet()

# Creating a Function that has parameters
def greet(name, gender):
  gender = gender.lower()
  if(gender == 'femenino'):
    print(f"Hola {name}!, mi maestra, ¿Como estas?")
  elif(gender == 'masculino'):
    print(f"Hola {name}!, mi maestro, ¿Como estas?")
  else:
    print(f"Hola {name}!, crack, ¿Como estas?")

greet("Luciano", "Masculino")
greet("Camila", "Femenino")
greet("Julio", "No Binario")

# Creating a function that returns values
def create_password(num):
  characters = "abcdefghij"
  int_num = str(num)
  num = int(int_num[0])
  c1 = num - 2
  c2 = num
  c3 = num - 5
  password = f"{characters[c1]}{characters[c2]}{characters[c3]}{num*2}"
  return password, num

# Unpacket the Function
password, first_number = create_password(981)

print(f"Tu contraseña nueva es: {password}")
print(f"El nùmero utilizado para crearla fue: {first_number}")