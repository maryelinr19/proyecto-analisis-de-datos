import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo

# Cargar el dataset
heart_failure_clinical_records = fetch_ucirepo(id=519)

# Convertir la estructura Dataset en un DataFrame de Pandas
df = pd.DataFrame(heart_failure_clinical_records.data.features)

# Agregar la columna 'is_dead' al DataFrame con valores aleatorios para este ejemplo
df['is_dead'] = np.random.choice([0, 1], df.shape[0])

# Verificar las columnas presentes en el DataFrame actualizado
print(df.columns)

# Separar el dataframe en dos según el valor de la columna 'is_dead'
if 'is_dead' in df.columns:
    df_perecidos = df[df['is_dead'] == 1]
    df_sobrevivientes = df[df['is_dead'] == 0]

    # Calcular los promedios de las edades de cada dataset
    promedio_edad_perecidos = np.mean(df_perecidos['age']).astype(int)
    promedio_edad_sobrevivientes = np.mean(df_sobrevivientes['age']).astype(int)

    # Imprimir los promedios de las edades como enteros
    print("El promedio de edad de las personas que perecieron es:", promedio_edad_perecidos, "años")
    print("El promedio de edad de las personas que sobrevivieron es:", promedio_edad_sobrevivientes, "años")
else:
    print("La columna 'is_dead' no está presente en el DataFrame.")

