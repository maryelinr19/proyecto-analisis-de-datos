import pandas as pd
import requests

def descargar_csv_desde_url(url, nombre_archivo):
    # Realizar una solicitud GET para descargar el archivo desde la URL
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Escribir la respuesta en un archivo de texto plano con extensión .csv
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)
        print(f"El archivo CSV se ha descargado y guardado como '{nombre_archivo}' exitosamente.")
    else:
        print("No se pudo descargar el archivo. Por favor, verifica la URL.")

def procesar_dataframe(df):
    # Verificar y eliminar valores faltantes
    if df.isnull().values.any():
        df = df.dropna()
        print("Se han eliminado los valores faltantes.")
    
    # Eliminar filas duplicadas
    if df.duplicated().any():
        df = df.drop_duplicates()
        print("Se han eliminado las filas duplicadas.")
    
    # Verificar y eliminar valores atípicos (puedes implementar tu lógica de detección de valores atípicos aquí)
    # Creamos la columna de categorización por edades
    bins = [0, 12, 19, 39, 59, float('inf')]
    labels = ['Niño', 'Adolescente', 'Joven Adulto', 'Adulto', 'Adulto Mayor']
    df['Categoría de Edad'] = pd.cut(df['age'], bins=bins, labels=labels)
    

    
    return df

# URL del archivo CSV a descargar
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

# Llamar a la función para descargar el archivo CSV desde la URL proporcionada
descargar_csv_desde_url(url, "heart_failure_clinical_records_dataset.csv")

# Cargar el archivo CSV en un dataframe
df = pd.read_csv("heart_failure_clinical_records_dataset.csv")

# Procesar el dataframe
df_procesado = procesar_dataframe(df)

# Guardar el resultado como un nuevo archivo CSV
df_procesado.to_csv('heart_failure_clinical_records_dataset_procesado.csv', index=False)
