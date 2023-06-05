# Exercise 2.2 - Ejercicio 2.2

# Hacer una sucesion de Fibonacci

def fibonacci(num):
  a,b = 0,1
  fibonacciList = [0]
  for i in range(num):
    if b > num: return fibonacciList;
    else: 
      fibonacciList.append(b)
      a,b = b,a+b
  return fibonacciList;

result = fibonacci(40)
print(result)