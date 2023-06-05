# Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("ResolveProblems/datos.csv")

# Convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

# Mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))

# Remplazando los datos "dalto" por "Maestro"
df['apellido'].replace("dalto","maestro",inplace=True)

# Eliminando las filas con datos faltantes
df = df.dropna()

# Eliminando las filas repetidas
df = df.drop_duplicates()

# Creando un CSV con el dataframe resultante (limpio)
df.to_csv("ResolveProblems/datos_limpios.csv")