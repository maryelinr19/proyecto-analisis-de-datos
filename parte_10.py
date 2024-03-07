import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar el DataFrame procesado desde el archivo CSV
df = pd.read_csv('datos_procesados.csv')


# Eliminar las columnas DEATH_EVENT, age y categoria_edad del dataframe
X = df.drop(columns=['DEATH_EVENT', 'age'])

# Crea el vector Y con la columna age
y = df['age']

# Ajusta una regresión lineal sobre las columnas restantes
model = LinearRegression()
model.fit(X, y)

# Predice las edades
edades_predichas = model.predict(X)

# Compara las edades reales con las edades predichas
error_cuadratico_medio = mean_squared_error(y, edades_predichas)

# Muestra las edades reales y predichas
resultados = pd.DataFrame({'Edad Real': y, 'Edad Predicha': edades_predichas})
print(resultados)

print("Error cuadrático medio:", error_cuadratico_medio)
