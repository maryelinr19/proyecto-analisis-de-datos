import pandas as pd
import matplotlib.pyplot as plt

# Cargar el DataFrame procesado desde el archivo CSV
df = pd.read_csv('datos_procesados.csv')

# Crear una figura y ejes para los subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Contar la cantidad de valores para cada categoría
anemicos_counts = df['anaemia'].value_counts()
diabeticos_counts = df['diabetes'].value_counts()
fumadores_counts = df['smoking'].value_counts()
muertos_counts = df['DEATH_EVENT'].value_counts()

# etiquetas 
anemicos_labels = ['No', 'Sí']
diabeticos_labels = ['No', 'Sí']
fumadores_labels = ['No', 'Sí']
muertos_labels = ['No', 'Sí']

# Crear las gráficas de torta para cada categoría con las nuevas etiquetas
axs[0, 0].pie(anemicos_counts, labels=anemicos_labels, autopct='%1.1f%%', startangle=90)
axs[0, 0].set_title('Distribución de Anémicos')

axs[0, 1].pie(diabeticos_counts, labels=diabeticos_labels, autopct='%1.1f%%', startangle=90)
axs[0, 1].set_title('Distribución de Diabéticos')

axs[1, 0].pie(fumadores_counts, labels=fumadores_labels, autopct='%1.1f%%', startangle=90)
axs[1, 0].set_title('Distribución de Fumadores')

axs[1, 1].pie(muertos_counts, labels=muertos_labels, autopct='%1.1f%%', startangle=90)
axs[1, 1].set_title('Distribución de Muertos')

plt.tight_layout()
plt.show()
