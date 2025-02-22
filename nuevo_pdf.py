import os
from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter

# Rutas
CARPETA_ENTRADA = r"E:\64090N000174_GIRADO\42B"
CARPETA_SALIDA_PDF = r"E:\64090N000174_GIRADO\42BPDF"

# Asegurar que las carpetas de salida existen
os.makedirs(CARPETA_SALIDA_PDF, exist_ok=True)

# Buscar archivos .tif en la carpeta de entrada
archivos = [f for f in os.listdir(CARPETA_ENTRADA) if f.lower().endswith(".tif")]

if not archivos:
    print("No se encontraron archivos .tif para convertir.")
else:
    print(f"Convirtiendo {len(archivos)} archivos...")

# Procesar cada imagen
for archivo in archivos:
    ruta_tif_opt = os.path.join(CARPETA_ENTRADA, archivo)
    ruta_pdf = os.path.join(CARPETA_SALIDA_PDF, archivo.replace(".tif", ".pdf"))

    try:
        with Image.open(ruta_tif_opt) as img:
            img = img.convert("RGB")  # Convertir a RGB para compatibilidad

            # Crear el PDF usando PIL
            img.save(
                ruta_pdf,
                "PDF",
                resolution=300.0,  # Resolución en DPI
                save_all=True,
                append_images=[],  # Para agregar más páginas (si es necesario)
                optimize=False,  # Puedes probar con True para optimizar el tamaño
            )

        # Agregar metadatos al PDF
        pdf_reader = PdfFileReader(ruta_pdf)
        pdf_writer = PdfFileWriter()
        pdf_writer.appendPagesFromReader(pdf_reader)
        pdf_writer.addMetadata({
            '/Title': 'RCN_tv',
            '/Author': 'Imperio Byte',
            '/Creator': 'Andres Pardo',
            '/Producer': 'Image scan',
            '/Subject': '64090N000174',
            '/Keywords': 'Palabras clave del Documento'
        })

        with open(ruta_pdf, 'wb') as f:
            pdf_writer.write(f)

        print(f"PDF de alta calidad (300 DPI) creado con metadatos: {ruta_pdf}")

    except Exception as e:
        print(f"Error con {archivo}: {e}")

print("Conversión de TIFF optimizado a PDF con 300 DPI y metadatos completada.")