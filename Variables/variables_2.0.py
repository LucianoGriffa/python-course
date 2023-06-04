# Unpack - Desempaquetar

# Creating the data - Creando los datos
data_in_tuple = ("Lucas", "Dalto", 10000000) # Tuple - Tupla
data_in_list = [22, "Argentina", "Soy Dalto"] # List - Lista

# Unpacked - Desenpaquetado
name, lastname, subscribers = data_in_tuple
age, live, channel = data_in_list

print(name, lastname, subscribers) # Lucas Dalto 10000000
print(age, live, channel) # 22, "Argentina", "Soy Dalto"