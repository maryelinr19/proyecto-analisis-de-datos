import sys
import pandas as pd
import requests
import io

def descargar_datos_desde_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Error al descargar los datos. Por favor, verifica la URL.")
        sys.exit(1)

def procesar_datos_y_exportar_csv(datos):
    df = pd.read_csv(io.BytesIO(datos))  # Convierte los datos en un DataFrame
   
    # Exportar el DataFrame procesado a un archivo CSV
    df.to_csv('datos_procesados.csv', index=False)
    print("Procesamiento completado. Los datos procesados se han guardado en 'datos_procesados.csv'.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Por favor, proporcione la URL como argumento al ejecutar el script.")
        sys.exit(1)

    url = sys.argv[1]
    datos_descargados = descargar_datos_desde_url(url)
    procesar_datos_y_exportar_csv(datos_descargados)

