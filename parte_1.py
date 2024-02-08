import numpy as np
from ucimlrepo import fetch_ucirepo

# Cargar el dataset
heart_failure_clinical_records = fetch_ucirepo(id=519)

# Obtener la lista de edades
edades = heart_failure_clinical_records.data.features['age']

# Convertir la lista de edades a un arreglo de NumPy
edades_array = np.array(edades)

# Calcular el promedio de edad
promedio_edad = np.mean(edades_array)

print("El promedio de edad de las personas participantes en el estudio es:", promedio_edad)
