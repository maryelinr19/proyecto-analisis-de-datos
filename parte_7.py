import pandas as pd
import matplotlib.pyplot as plt

# Cargar el DataFrame procesado desde el archivo CSV
df = pd.read_csv('datos_procesados.csv')

# Crear un nuevo DataFrame con las columnas relevantes
data = df[['sex', 'anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']]

# Reemplazar los valores numéricos de la columna 'sex' por etiquetas 'Hombres' y 'Mujeres'
data['sex'] = data['sex'].replace({0: 'Mujeres', 1: 'Hombres'})

# Agrupar por género y sumar las categorías
grouped_data = data.groupby('sex').sum()

# Graficar las categorías con hombres a la derecha y mujeres a la izquierda
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.35
bar_positions = range(len(grouped_data.columns))

# Graficar los datos de mujeres a la izquierda
ax.bar(bar_positions, grouped_data.loc['Hombres'], bar_width, label='Hombres', color='blue')

# Graficar los datos de hombres a la derecha
ax.bar([p + bar_width for p in bar_positions], grouped_data.loc['Mujeres'], bar_width, label='Mujeres', color='red')

ax.set_title('Cantidad de Pacientes por Categoría y Género')
ax.set_xlabel('Categoría')
ax.set_ylabel('Cantidad')
ax.set_xticks([p + bar_width/2 for p in bar_positions])
ax.set_xticklabels(grouped_data.columns)
ax.legend(title='Género')
plt.show()
