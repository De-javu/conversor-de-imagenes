import os
import subprocess
import config  # Importar el archivo de configuración
import time

def convertir_pdf_a_pdfa():
    # Asegurar que las carpetas de salida existen
    os.makedirs(config.CARPETA_SALIDA_PDFA, exist_ok=True)

    # Buscar archivos .pdf en la carpeta de entrada
    archivos = [f for f in os.listdir(config.CARPETA_ENTRADA) if f.lower().endswith(".pdf")]

    if not archivos:
        print("No se encontraron archivos .pdf para convertir.")
        return

    print(f"Convirtiendo {len(archivos)} archivos...")

    # Tiempo total de conversión
    tiempo_total_inicio = time.time()

    # Procesar cada archivo PDF
    for archivo in archivos:
        ruta_pdf = os.path.join(config.CARPETA_ENTRADA, archivo)
        ruta_pdfa_temp = os.path.join(config.CARPETA_SALIDA_PDFA, archivo.replace(".pdf", "_pdfa.pdf"))
        ruta_pdfa_final = os.path.join(config.CARPETA_SALIDA_PDFA, archivo)

        try:
            # Convertir el PDF a PDF/A usando PDF/A Manager
            pdfa_command = [
                config.PDF_A_MANAGER_PATH,  # Ruta completa al ejecutable de PDF/A Manager
                "-o", config.CARPETA_SALIDA_PDFA,  # Especificar la carpeta de salida
                "--convert",  # Convertir a PDF/A
                "--suffix", "_pdfa",  # Sufijo para los archivos convertidos
                ruta_pdf
            ]
            print(f"Ejecutando comando: {' '.join(pdfa_command)}")
            result = subprocess.run(pdfa_command, capture_output=True, text=True, shell=True, cwd=os.path.dirname(config.PDF_A_MANAGER_PATH))

            # Verificar si el comando se ejecutó correctamente
            if result.returncode != 0:
                print(f"Error con {archivo}: {result.stderr}")
                print(f"Comando ejecutado: {' '.join(pdfa_command)}")
            else:
                # Renombrar el archivo convertido para mantener el nombre original
                os.rename(ruta_pdfa_temp, ruta_pdfa_final)
                print(f"PDF/A de alta calidad creado: {ruta_pdfa_final}")

        except Exception as e:
            print(f"Error con {archivo}: {e}")

    # Tiempo total de conversión
    tiempo_total_fin = time.time()
    tiempo_total = tiempo_total_fin - tiempo_total_inicio
    print(f"Conversión de PDF a PDF/A completada en {tiempo_total:.2f} segundos")

if __name__ == "__main__":
    convertir_pdf_a_pdfa()