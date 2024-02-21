import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo

# Cargar el dataset
heart_failure_clinical_records = fetch_ucirepo(id=519)

# Convertir la estructura Dataset en un DataFrame de Pandas
df = pd.DataFrame(heart_failure_clinical_records.data.features)

# Verificar los tipos de datos en cada columna del DataFrame
print(df.dtypes)

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras
cantidad_hombres_fumadores = df[(df['sex'] == 'male') & (df['smoking'] == 'yes')].shape[0]
cantidad_mujeres_fumadoras = df[(df['sex'] == 'female') & (df['smoking'] == 'yes')].shape[0]

print("Cantidad de hombres fumadores:", cantidad_hombres_fumadores)
print("Cantidad de mujeres fumadoras:", cantidad_mujeres_fumadoras)
