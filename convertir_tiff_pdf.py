import os
from PIL import Image

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
    print(f" Convirtiendo {len(archivos)} archivos...")

# Procesar cada imagen
for archivo in archivos:
    ruta_tif_opt = os.path.join(CARPETA_ENTRADA, archivo)
    ruta_pdf = os.path.join(CARPETA_SALIDA_PDF, archivo.replace(".tif", ".pdf"))

    try:
        with Image.open(ruta_tif_opt) as img:
            img = img.convert("RGB")  # Convertir a RGB para compatibilidad

            # Tamaño de página A4 en puntos (595 x 842)
            page_size = (595, 842)

            # Crear el PDF usando PIL
            img.save(
                ruta_pdf,
                "PDF",
                resolution=300.0,  # Resolución en DPI
                save_all=True,
                append_images=[],  # Para agregar más páginas (si es necesario)
                optimize=False,  # Puedes probar con True para optimizar el tamaño
            )

        print(f" PDF de alta calidad (300 DPI) creado: {ruta_pdf}")

    except Exception as e:
        print(f"Error con {archivo}: {e}")

print("Conversión de TIFF optimizado a PDF con 300 DPI completada.")