# Exercise 2.2 - Ejercicio 2.2

# Crea una funcion que cuando le pasemos un numero, nos de numeros primos hasta llegar al numero ingresado.

def numeros_primos(num):
  for i in range(2,num-1):
    if num%i==0: return False;
  return True;

def primos_hasta(num):
  primos = []
  for i in range(3,num+1):
    resultado = numeros_primos(i)
    if resultado == True: primos.append(i)
  return primos;


resultado = primos_hasta(40)
print(resultado)