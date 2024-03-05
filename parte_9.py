import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px

# Cargar el DataFrame procesado desde el archivo CSV
df = pd.read_csv('datos_procesados.csv')

# Eliminar la columna objetivo DEATH_EVENT y la columna categoria_edad
X = df.drop(columns=['DEATH_EVENT', 'age']).values

# Exportar un array unidimensional de solo la columna objetivo DEATH_EVENT
y = df['DEATH_EVENT'].values

# Ejecutar la reducción de dimensionalidad usando TSNE
X_embedded = TSNE(n_components=3, learning_rate='auto', init='random', perplexity=3).fit_transform(X)

# Crear un gráfico de dispersión 3D con Plotly
fig = px.scatter_3d(x=X_embedded[:,0], y=X_embedded[:,1], z=X_embedded[:,2], color=y, labels={'color': 'DEATH_EVENT'})
fig.update_layout(scene=dict(xaxis_title='Componente 1', yaxis_title='Componente 2', zaxis_title='Componente 3'))
fig.show()
