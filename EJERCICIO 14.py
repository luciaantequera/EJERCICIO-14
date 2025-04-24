## COGER LOS DATOS Y GUARDALOS EN UNA TABLA  UNA BASE DE DATOS SQLITE3
import requests

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
response = requests.get(url)
data = response.json()

import sqlite3
import pandas as pd

# Convertir los datos a un DataFrame
df = pd.DataFrame([data])

# Conectar a la base de datos SQLite
conn = sqlite3.connect('nasa_apod.db')

# Guardar el DataFrame en la base de datos
df.to_sql('apod', conn, if_exists='replace', index=False)

conn.close()

print(data)



##  CONSUMIR ESTOS DATOS 
conn = sqlite3.connect('nasa_apod.db')

# Leer los datos de la tabla
df = pd.read_sql_query("SELECT * FROM apod", conn)

# Mostrar algunos detalles específicos de la imagen astronómica del día
print(df[['title', 'explanation']])

conn.close()


## MODIFICAR ALGUNOS DE LOS DATOS CON INPUT
conn = sqlite3.connect('nasa_apod.db')

# Cambiar el título de la imagen
df.at[0, 'title'] = 'Nuevo Título'

# Guardar los cambios en la base de datos
df.to_sql('apod', conn, if_exists='replace', index=False)

# Mostrar el DataFrame modificado
print(df.head())

conn.close()


## HACER EL ANÁLISIS DE EFICIENCIA Y COMPARAR EL TIEMPO QUE TARDA EN ITERAR TODOS LOS ELEMENTOS IRECTAMENTE DESDE LA API COMPARÁNDOLO CON LO QUE SE TARDA EN LA BASE DE DATOS 
import time

# Medir el tiempo de iteración desde la API
start_time_api = time.time()
for key, value in data.items():
    pass
end_time_api = time.time()
api_duration = end_time_api - start_time_api

# Medir el tiempo de iteración desde la base de datos
conn = sqlite3.connect('nasa_apod.db')
start_time_db = time.time()
for index, row in df.iterrows():
    pass
end_time_db = time.time()
db_duration = end_time_db - start_time_db
conn.close()

# Comparar los tiempos
print(f"Tiempo de iteración desde la API: {api_duration} segundos")
print(f"Tiempo de iteración desde la base de datos: {db_duration} segundos")

