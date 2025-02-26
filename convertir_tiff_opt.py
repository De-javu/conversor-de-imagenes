import os
import time
from PIL import Image
import PyPDF2
import subprocess

# Rutas
CARPETA_ENTRADA = r"D:\xampp\htdocs\pdf_2\imagenes_convertidas_optimizadas"
CARPETA_SALIDA_PDF = r"D:\xampp\htdocs\pdf_2\imagenes_convertidas_pdf"

# Asegurar que las carpetas de salida existen
os.makedirs(CARPETA_SALIDA_PDF, exist_ok=True)

# Buscar archivos .tif en la carpeta de entrada
archivos = [f for f in os.listdir(CARPETA_ENTRADA) if f.lower().endswith(".tif")]

if not archivos:
    print("No se encontraron archivos .tif para convertir.")
else:
    print(f"Convirtiendo {len(archivos)} archivos...")

# Tiempo total de conversión
tiempo_total_inicio = time.time()

# Procesar cada imagen
for archivo in archivos:
    ruta_tif = os.path.join(CARPETA_ENTRADA, archivo)
    ruta_pdf_temp = os.path.join(CARPETA_SALIDA_PDF, archivo.replace(".tif", "_temp.pdf"))
    ruta_pdf_final = os.path.join(CARPETA_SALIDA_PDF, archivo.replace(".tif", ".pdf"))

    try:
        with Image.open(ruta_tif) as img:
            # No realizar ninguna conversión que pueda afectar la orientación
            img.save(
                ruta_pdf_temp,
                "PDF",
                resolution=300.0,  # Resolución en DPI
                save_all=True,
                append_images=[],  # Para agregar más páginas (si es necesario)
                optimize=False,  # Puedes probar con True para optimizar el tamaño
            )

        # Agregar metadatos al PDF temporal
        with open(ruta_pdf_temp, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            # Agregar metadatos
            writer.add_metadata({
                "/Producer": "IMPERIO BYTE",
                "/Creator": "PIL",
                "/Title": archivo.replace(".tif", " "),
                "/Author": "IMPERIO BYTE",
                "/Subject": "CONVERSION DE MICROFILM A DIGITAL",
            })

            with open(ruta_pdf_temp, "wb") as output_pdf:
                writer.write(output_pdf)

        # Convertir el PDF temporal a PDF 1.7 usando Ghostscript
        gs_command = [
            "gswin64c",  # Comando para Ghostscript en Windows
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.7",
            "-o", ruta_pdf_final,
            ruta_pdf_temp
        ]
        result = subprocess.run(gs_command, capture_output=True, text=True)

        # Verificar si el comando se ejecutó correctamente
        if result.returncode != 0:
            print(f"Error con {archivo}: {result.stderr}")
        else:
            print(f"PDF de alta calidad (PDF 1.7) creado: {ruta_pdf_final}")

        # Eliminar el archivo PDF temporal
        os.remove(ruta_pdf_temp)

    except Exception as e:
        print(f"Error con {archivo}: {e}")

# Tiempo total de conversión
tiempo_total_fin = time.time()
tiempo_total = tiempo_total_fin - tiempo_total_inicio
tiempo_promedio = tiempo_total / len(archivos) if archivos else 0

print(f"Total de archivos convertidos: {len(archivos)}")
print(f"Conversión de TIFF a PDF 1.7 completada en {tiempo_total:.2f} segundos")
print(f"Tiempo promedio por archivo: {tiempo_promedio:.2f} segundos")



