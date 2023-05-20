<div align='center'>
  <img height="60" src="https://th.bing.com/th/id/R.c5e3c2f5e09713ea7bc42a4231401a16?rik=AyVL7zVsBfoOBw&pid=ImgRaw&r=0">
  <h1>Curso de Python desde cero y en Español</h1>
  
  <i>Curso impartido en YouTube por [@SoyDalto](https://www.youtube.com/@soydalto)</i>
  <i>y repositorio detallado por [@lucianogriffa](https://github.com/lucianogriffa)</i>
  
  <i><sup>Deja tu :star: si te gusta el proyecto.</sup></i>
</div>
 
## Indice 
- [Indice](#indice)  
  - [¿Qué es Python?](#qué-es-python)
  - [Características](#características)
  - [Primer Hello World](#primer-hello-world)
  - [Tipos de Datos](#tipos-de-datos)
    - [Datos Simples](#datos-simples)
  - [Variables](#variables)

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
