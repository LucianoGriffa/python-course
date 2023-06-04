# Parameters args

# Non-optimal way of adding values
# def sum(list):
#    num_sum = 0
#    for num in list:
#        num_sum = num_sum + num
#    return num_sum

# Result = sum([5,3,9,10,20,3])

# Optimal way to add values
def sum_total(num):
  return sum([*num])
result = sum_total([5,3,9,10,20,3])

# Same as above but using the * operator as parameter (*args)
def suma(name,*num):
  return print(f"{name}, la suma de tus numeros es: {sum(num)}")
result = suma("Lucas",5,9,10,20,3)
