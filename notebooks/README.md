Notebooks de análisis

Abrir Jupyter en http://localhost:8888 con token 'ecotoken'.

El notebook principal `analysis.ipynb` muestra cómo conectarse a la base de datos MongoDB, leer encuestas y hacer análisis simples con pandas y matplotlib.

Ejemplo (en una celda):

from pymongo import MongoClient
client = MongoClient('mongodb://mongo:27017')
db = client['eco_db']
import pandas as pd
rows = list(db.surveys.find())
df = pd.DataFrame(rows)
print(df.head())
