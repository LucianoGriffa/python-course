<div align='center'>
  <img height="60" src="https://th.bing.com/th/id/R.c5e3c2f5e09713ea7bc42a4231401a16?rik=AyVL7zVsBfoOBw&pid=ImgRaw&r=0">
  <h1>Curso de Python Desde Cero</h1>
  
  <i>Curso impartido en YouTube por [@SoyDalto](https://www.youtube.com/@soydalto)</i>
  
  <i><sup>Deja tu :star: si te gusta el proyecto.</sup></i>
</div>
 
## Indice 
- [Indice](#indice)  
  - [¿Qué es Python?](#qué-es-python)
  - [Características](#características)
  - [Primer Hello World](#primer-hello-world)
  - [Tipos de Datos](#tipos-de-datos)
    - [Datos Simples](#datos-simples)
    - [Datos Compuestos](#datos-compuestos)
  - [Variables](#variables)
  - [Operadores](#operadores)
    - [Operadores Aritméticos](#operadores-aritméticos)
    - [Operadores de Comparación](#operadores-de-comparación)
    - [Operadores Lógicos](#operadores-lógicos)
  - [Condicionales](#condicionales)
  - [Métodos](#métodos)
    - [Métodos de Cadenas](#métodos-de-cadenas)
    - [Métodos de Listas](#métodos-de-listas)
    - [Métodos de Diccionario](#métodos-de-diccionario)
  - [Inputs](#inputs)
  - [Ejercicio 1.0](#ejercicios-1)
    - Ejercicio 1.1
    - Ejercicio 1.2

---

#### ¿Qué es Python?
**Python es un lenguaje de programación de alto nivel y de código abierto. Es conocido por su sintaxis sencilla y legible, lo que lo hace ideal para principiantes en programación.** 

Se destaca por su amplia biblioteca estándar y su enfoque en la legibilidad del código. Es utilizado en diversos ámbitos, como desarrollo web, análisis de datos, inteligencia artificial y automatización de tareas. 

Fue creado por Guido van Rossum en 1991 y desde entonces ha ganado popularidad debido a su facilidad de uso y versatilidad.

---

#### Características:
- **Lenguaje de Propósito General**: Puede ser utilizado para cualquier actividad.(Web, Aplicaciones, etc.)

- **Lenguaje de Alto Nivel**: Esto lo hace más legible, ya que se parece más a un lenguaje natural.

- **Fácil de Aprender**: Por la similitud con el lenguaje humano, y la gran comunidad, para resolver problemas y dudas.

- **Lenguaje de Tipado Dinámico**: La variable se adapta según el tipo de dato que le pasemos. Ejemplo:
~~~Python
name = "luciano"
year = 2023
~~~
- **Lenguaje Orientado a Objeto**: Es un estilo de programación en el que trabajamos con objetos que representan entidades y tienen características y comportamientos definidos. Los objetos se crean a partir de clases y agrupan datos y funciones relacionadas. Esto facilita la organización del código, la reutilización y la flexibilidad en el desarrollo de software.
- **Lenguaje Interpretado**: Es un lenguaje interpretado porque ejecuta el código fuente directamente, sin necesidad de compilarlo previamente, lo que permite una mayor flexibilidad y facilidad de uso en el desarrollo y la ejecución de programas. 

---

#### Primer Hello World

Para correr tu primer programa "Hello World" en Python, sigue estos pasos:

1. Abre tu editor de texto o IDE favorito y crea un nuevo archivo con la extensión `.py`. Por ejemplo, [`helloworld.py`](./helloworld.py).

2. Abre el archivo y escribe el siguiente código en él:

```python
print("Hello World")
``` 
3. Guarda el archivo.

4. Abre una terminal o línea de comandos en tu sistema operativo.

5. Navega hasta el directorio donde guardaste el archivo [`helloworld.py`](./helloworld.py) utilizando el comando cd.

6. Ejecuta el siguiente comando en la terminal para correr el programa:

```bash
python helloworld.py
``` 
![image](https://github.com/lucianogriffa/python-soydalto/assets/73656863/682c05bf-91d1-4e0c-a70f-f102b4fb0518)

7. Verás que se imprime "Hello World" en la terminal.

---

### [Tipos de Datos](./DataTypes)
#### [Datos Simples](./DataTypes/simple-data.py)
- String - Texto
```python
"Luciano"

'Griffa' 

"""Your data is:
name: luciano
lastname: griffa"""

'''Your data is:
name: luciano
lastname: griffa'''
``` 
- Int & Float - Números Enteros & Números Flotantes/Decimales
```python
10 # Int

10.2 # Float
``` 
- Boolean - Booleano
```python 
True
False
``` 
#### [Datos Compuestos](./DataTypes/composite-data.py)
- List (Lista):
```python 
list = ["Luciano", "Luciano Griffa", True, 1.80]
``` 
Las listas en Python son estructuras de datos que pueden ser modificadas, lo que significa que se pueden agregar, eliminar o modificar elementos después de su creación.

- Tuple (Tupla):
```python 
tuple = ("Luciano", "Luciano Griffa", True, 1.80, "Tuple")
``` 
Aquí, se define una tupla llamada `tuple` que contiene varios elementos. Las tuplas son similares a las listas, pero a diferencia de ellas, las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.

- Set (Conjunto):
```python 
set = {"Luciano", "Luciano Griffa", True, 1.80, "Set"}
``` 
Se crea un conjunto llamado `set`. Los conjuntos son colecciones no ordenadas de elementos únicos. No se accede a los elementos por índice como en las listas y las tuplas. Los conjuntos no permiten elementos duplicados, por lo que si intentas agregar un elemento duplicado, no se almacenará en el conjunto.

- Dictionary (Diccionario):
```python 
dictionary = {
  'name': "Luciano",
  'lastname': "Griffa",
  'github': "@lucianogriffa",
  'age': 17,
  'duplicate_lastname': "Griffa"
}
print(dictionary['age'])
``` 
Aquí, se crea un diccionario llamado `dictionary` que contiene pares de `key: value`. Los diccionarios en Python son estructuras de datos que almacenan elementos asociados a una `key`. Cada elemento en el diccionario se compone de una `key` y un `value` separados por dos puntos (`:`).

Para acceder a un valor en el diccionario, se utiliza la `key` correspondiente. Por ejemplo, `dictionary['age']` devuelve el valor 17.

---

#### [Variables](./Variables/variables.py)
1. Definición de una variable con **camelCase**:
```python 
fullName = "Luciano Griffa"
``` 
En este caso, se define una variable llamada `fullName` utilizando la convención de nombres **camelCase**. Esto significa que la primera letra de la primera palabra está en minúscula y las primeras letras de las palabras subsiguientes están en mayúscula.

2. Definición de una variable con **snake_case**:
```python 
full_name = "Luciano Griffa"
``` 
Aquí, se define una variable llamada `full_name` utilizando la convención de nombres **snake_case**. En esta convención, todas las letras están en minúscula y las palabras se separan con guiones bajos (_).

3. Concatenación con el operador **+**:
```python 
welcome = "Hello " + " ¿How are you?"
``` 
Se realiza una concatenación de cadenas utilizando el operador **+**. En este caso, se concatenan las cadenas `"Hello"` y `" ¿How are you?"` y se guarda el resultado en la variable `welcome`.

4. Concatenación con **f-strings**:
```python 
welcome = f"Hello {full_name} ¿How are you?"
``` 
Aquí, se utiliza la sintaxis de **f-strings** para realizar una interpolación de cadenas. La variable `full_name` se inserta en la cadena utilizando llaves `{}` y el prefijo `f`. Esto permite combinar de manera fácil y legible las variables con el texto dentro de la cadena.

5. **Operadores de pertenencia** (in / not in):
```python 
print("Luciano" in welcome)  # True
print("Luciano" not in welcome)  # False
``` 
Se utilizan los **operadores de pertenencia** para verificar si la subcadena `"Luciano"` está presente en la cadena `welcome`. El operador in devuelve `True` si la subcadena se encuentra en la cadena y `False` en caso contrario. Por otro lado, el operador `not in` devuelve `True` si la subcadena no está presente y `False` si está presente.

---

#### [Operadores](./Operators/)

#### [Operadores Aritméticos](./Operators/arithmetic_operators.py)

Addition - Suma (+)

```python
addition = 2 + 2 # Result 4
```

Subtraction - Resta (-)

```python
subtraction = 4 - 2 # Result: 2
```

Multiplication - Multiplicación (*)

```python
multiplication = 2 * 3 # Result: 6
```

Division - División (/)

**Se utiliza para dividir un valor por otro y devuelve un resultado decimal o de tipo float.**

```python
division = 10 / 5 # Result: 2.0
```

Exponentiation - Exponenciación (**)

**Se utiliza para elevar un valor a una potencia y devuelve el resultado.**

```python
exponentiation = 3 ** 5 # Result: 243
```

Floor division - División baja (//)

**Se utiliza para realizar una división entera y devuelve un resultado entero(int) redondeado hacia abajo.**

```python
floor_division = 12 // 7 # Result: 1
```

Modulus - Módulo o Resto (%)

**Se utiliza para obtener el resto de una división y devuelve el resultado.**

```python
modulus = 18 % 10 # Result: 8
```

---

#### [Operadores de Comparación](./Operators/comparison_operators.py)

Equal - Igual que
```python
x == y 
```

Not equal - Distinto de
```python
x != y
```

Greater than - Mayor que
```python
x > y
```

Less than - Menor que
```python
x < y
```

Greater than or equal to - Mayor que o igual que
```python
x >= y 
```

Less than or equal to - Menor que o igual que
```python
x <= y
```

---

#### [Operadores Lógicos](./Operators/logical_operators.py)

Operador `and`: **Devuelve True si ambas expresiones son verdaderas, de lo contrario, devuelve False. Se puede usar `&` o `and`.** 

Ejemplos:
```python
Resultado = True & True # Devolver True
Resultado2 = False and True # Devolver Falso
Resultado3 = True & False # Devolver Falso
Resultado4 = False and False # Devolver Falso
```

Operador `or`: **Devuelve True si al menos una de las expresiones es verdadera, de lo contrario, devuelve False. Se puede usar `|` o `or`.** 

Ejemplos:
```python
Resultado5 = True or True #Devolver True
Resultado6 = False | True #Devolver True
Resultado7 = True or False #Devolver True
Resultado8 = False | False #Devolver Falso
```

Operador `not`: **Devuelve True si la expresión es falsa, y False si la expresión es verdadera. Es un operador unario, ya que solo actúa sobre una expresión.** 

Ejemplos:
```python
Resultado9 = not True #Devolver Falso
Resultado10 = not False #Devolver True
```

---

#### [Condicionales](./Conditionals/conditionals.py)

**`if`** se utiliza para ejecutar un bloque de código si una condición es verdadera.

**`else`** se utiliza para ejecutar un bloque de código **cuando todas las condiciones anteriores son falsas**.

**`elif`** se utiliza para evaluar múltiples condiciones y ejecutar el bloque de código correspondiente al primer elif cuya condición sea verdadera, siempre y cuando las condiciones anteriores sean falsas.

Ejemplo:
```python
age = 20
if age < 18:
    print("Eres menor de edad")
elif age >= 18 and age < 65:
    print("Eres adulto")
else:
    print("Eres un adulto mayor")
```
En este ejemplo, se define una variable `age` con el valor de 18. Luego, se utilizan las estructuras condicionales `if`, `elif`  y `else` para determinar en qué categoría de edad se encuentra la persona.

- **Si la edad es menor a 18, se imprimirá "Eres menor de edad".**

- **Si la edad es igual o mayor a 18 y menor a 65, se imprimirá "Eres adulto".**

- **Si la edad es igual o mayor a 65, se imprimirá "Eres un adulto mayor".**

En este caso, como la edad es 20, se imprimirá "Eres adulto". Puedes modificar el valor de la variable `age` para probar diferentes resultados.

---

#### [Métodos](./Methods/)

---

#### [Métodos de Cadenas](./Methods/string_method.py)

```python
cadena = "Hola, Maquina! ¿Cómo Estás?"
```

`dir()`: **Muestra los atributos y métodos disponibles para un objeto.**
```python
print(dir(cadena))
```

`lower()`: **Convierte la cadena a minúsculas.**
```python
print(cadena.lower())  # "hola, maquina! ¿cómo estás?"
```

`upper()`: **Convierte la cadena a mayúsculas.**
```python
print(cadena.upper())  # "HOLA, MAQUINA! ¿CÓMO ESTÁS?"
```

`capitalize()`: **Convierte la primera letra de la cadena a mayúscula y el resto a minúsculas.**
```python
print(cadena.capitalize())  # "Hola, maquina! ¿cómo estás?"
```

`isalpha()`: **Verifica si la cadena contiene solo caracteres alfabéticos.(Únicamente A-Z)**
```python
print(cadena.isalpha())  # False
```

`split()`: **Divide la cadena en una lista de subcadenas utilizando un delimitador.**
```python
print(cadena.split())  # ['Hola,', 'Maquina!', '¿Cómo', 'Estás?']
```

`replace()`: **Reemplaza una subcadena por otra en la cadena original.**
```python
print(cadena.replace("Estás", "Hola"))  # "Hola, Maquina! ¿Cómo Hola?"
```

`endswith()`: **Verifica si la cadena termina con una subcadena específica.**
```python
print(cadena.endswith("?"))  # True
```

`startswith()`: **Verifica si la cadena comienza con una subcadena específica.**
```python
print(cadena.startswith("Hola"))  # True
```

`len()`: **Devuelve la longitud (cantidad de caracteres) de la cadena.**
```python
print(len(cadena))  # 23
```

`count()`: **Cuenta las ocurrencias de una subcadena en la cadena.**
```python
print(cadena.count("a"))  # 4
```

`isnumeric()`: **Verifica si la cadena contiene solo caracteres numéricos.**
```python
print(cadena.isnumeric())  # False
```

`index()`: **Devuelve la posición de la primera aparición de una subcadena en la cadena.**
```python
print(cadena.index("Maquina"))  # 6
```

`find()`: **Busca la primera aparición de una subcadena en la cadena y devuelve su posición (-1 si no se encuentra).**
```python
print(cadena.find("¿"))  # 16
```

---

#### [Métodos de Listas](./Methods/list_methods)

```python
lista = [1, 3, 5, 7, 9]
```

`list()`: **Crea una lista a partir de un objeto iterable.**
```python
nueva_lista = list("Hola")  # ['H', 'o', 'l', 'a']
```

`len()`: **Devuelve la longitud (cantidad de elementos) de la lista.**
```python
print(len(lista))  # 5
```

`append()`: **Agrega un elemento al final de la lista.**
```python
lista.append(11)
print(lista)  # [1, 3, 5, 7, 9, 11]
```

`insert()`: **Inserta un elemento en una posición específica de la lista.**
```python
lista.insert(2, 4)
print(lista)  # [1, 3, 4, 5, 7, 9, 11]
```

`extend()`: **Agrega los elementos de otra lista al final de la lista actual.**
```python
lista.extend([13, 15])
print(lista)  # [1, 3, 4, 5, 7, 9, 11, 13, 15]
```

`pop()`: **Elimina y devuelve el último elemento de la lista (o un elemento en una posición específica).**
```python
elemento_eliminado = lista.pop()
print(elemento_eliminado)  # 15
print(lista)  # [1, 3, 4, 5, 7, 9, 11, 13]
```

`remove()`: **Elimina la primera aparición de un elemento en la lista.**
```python
lista.remove(4)
print(lista)  # [1, 3, 5, 7, 9, 11, 13]
```

`clear()`: **Elimina todos los elementos de la lista.**
```python
lista.clear()
print(lista)  # []
```

`sort()`: **Ordena los elementos de la lista en orden ascendente.**
```python
otra_lista = [9, 2, 7, 4, 1]
otra_lista.sort()
print(otra_lista)  # [1, 2, 4, 7, 9]
```

`reverse()`: **Invierte el orden de los elementos en la lista.**
```python
otra_lista.reverse()
print(otra_lista)  # [9, 7, 4, 2, 1]
```

---

#### [Métodos de Diccionario](./Methods/dictionary_methods.py)

```python
diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
```

`get()`: **Obtiene el valor asociado a una clave, devuelve None si la clave no existe.**
```python
print(diccionario.get("nombre"))  # "Juan"
print(diccionario.get("altura"))  # None
```

`keys()`: **Devuelve una lista con todas las claves del diccionario.**
```python
print(diccionario.keys())  # ["nombre", "edad", "ciudad"]
```

`clear()`: **Elimina todos los elementos del diccionario.**
```python
diccionario.clear()
print(diccionario)  # {}
```

`pop()`: **Elimina y devuelve el valor asociado a una clave específica.**
```python
valor_eliminado = diccionario.pop("edad")
print(valor_eliminado)  # 30
print(diccionario)  # {"nombre": "Juan", "ciudad": "Madrid"}
```

`items()`: **Devuelve una lista de tuplas (clave, valor) de todos los elementos del diccionario.**
```python
print(diccionario.items())  # [("nombre", "Juan"), ("ciudad", "Madrid")]
```

---

#### [Inputs](./Inputs/inputs.py)

`input()` se utiliza para obtener la entrada del usuario, y **los valores ingresados se tratan como cadenas de texto**. Puedes convertirlos a otros tipos de datos según sea necesario, con `int()` y `float()`.

Obtener una cadena de texto desde el usuario:
```python
texto = input("Ingresa una cadena de texto: ")
print("El texto que ingresaste es:", texto)
```

Obtener un float o número decimal desde el usuario
```python
numero_decimal = float(input("Ingresa un número decimal: "))
print("El número decimal que ingresaste es:", numero_decimal)
```

Obtener un int o número entero desde el usuario
```python
number = int(input("Ingresa un número entero: "))
print("El número entero que ingresaste es:", number)
```

Obtener varios valores en una sola línea separados por espacios y almacenarlos en una lista:
```python
valores = input("Ingresa varios valores separados por espacios: ").split()
print("Los valores que ingresaste son:", valores)
```

Obtener varios números en una sola línea separados por comas y almacenarlos en una lista de enteros:
```python
numeros = [int(x) for x in input("Ingresa varios números separados por comas: ").split(",")]
print("Los números que ingresaste son:", numeros)
```

---

#### [Ejercicios 1](./Exercises/.py)

#### [Ejercicio 1.1](./Exercises/.py):

El timing para ver los conceptos vistos en python en un curso de corrido es de **2.5hs como Mínimo, 7hs como Máximo y 4hs en Promedio**. **Este curso lo logro en 1.5hs**.

**a**) Cuánta diferencia en porcentaje entre el curso actual y:
   - El más rápido de otros cursos.
   - El más lento de otros cursos.
   - El promedio de los cursos.

Teniendo en cuenta que **el crudo de los demás cursos es de 5hs y con edición lo convierten en 4hs y el crudo de este curso 3.5hs y se redujo a 1.5hs.**

**b**) Qué porcentaje de material inservible que se reduce en:
  - El promedio de los cursos.
  - El curso actual (este curso).

**c**) Ver 10hs de este curso a cuantas de otros cursos equivalen?

#### [Ejercicio 1.2](./Exercises/.py): 

[Resolución Ejercicio 1.1](./Exercises/exercise_1.1.py)
[Resolución Ejercicio 1.2](./Exercises/exercise_1.1.py)
