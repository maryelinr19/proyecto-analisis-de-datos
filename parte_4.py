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

# URL del archivo CSV a descargar
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

# Llamar a la función para descargar el archivo CSV desde la URL proporcionada
descargar_csv_desde_url(url, "heart_failure_clinical_records_dataset.csv")
