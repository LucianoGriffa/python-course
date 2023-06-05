import pandas as pd;
archive = pd.read_csv("CSV_Archives/data.csv", names=["name", "lastname", "age"]) # Usando read_csv para leer el archivo CSV.
archive2 = pd.read_csv("CSV_Archives/data.csv", names=["name", "lastname", "age"])

archive['age'] = archive['age'].astype(str) # Convertir a string los datos de una columna.

names = archive["name"] # Obteniendo los datos de la columna name.

cadena = "0123456789"
# print(cadena[2:8]) Con la tecnica Slaising, podemos decir que arranque en la posición 2 y termine en la posición 8.

sort_archive = archive.sort_values("age") # Ordenando el dataframe por la edad
sort_archive = archive.sort_values("age", ascending=False) # Ordenando de forma descendiente.

concat_archive = pd.concat([archive, archive2]) # Concatenando los 2 dataframes

archive['lastname'].replace("Dalto","Maestro",inplace=True) #Remplazando los datos "Dalto" por "Maestro"

archive = archive.dropna() # Eliminando las filas con datos faltantes

archive = archive.drop_duplicates() # Eliminando las filas repetidas

archive.to_csv("CSV_Archives/clean_data.csv") # Creando un CSV con el dataframe resultante (limpio)

primeras_filas = archive.head(3) # Accediendo a la primeras 3 filas con head()

ultimas_filas = archive.tail(3) # Accediendo a las últimas 3 filas con tail()

filas_totales,columnas_totales = archive.shape # Accediendo a la cantidad de filas y columnas con shape

archive_info = archive.describe() # Obteniendo data estadística del dataframe:

elemento_especifico_loc = archive.loc[1,"age"] # Accediendo a la edad de la fila 2

elemento_especifico_iloc = archive.iloc[2,2] # Accediendo a la edad de la fila 2 con iloc

apellidos_loc = archive.loc[:,"lastname"] # Accediendo a todos los apellidos con loc

apellidos = archive.iloc[:,1] # Accediendo a todos los apellidos con iloc

fila_3 = archive.loc[2,:] # Accediendo a la fila 3 con loc

fila_3 = archive.iloc[2,:] # Accediendo a la fila 3 con iloc

# mayor_que_30 = archive.loc[archive["age"]>30,:] # Accediendo a filas con edad mayor que 30 con loc