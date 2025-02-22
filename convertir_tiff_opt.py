from PIL import Image, ImageEnhance, ImageFilter
import os

# Rutas
CARPETA_ENTRADA = r"E:\imagenes"
CARPETA_SALIDA_TIFF = r"E:\imagenes_convertidas_pdfa"

# Asegurar que las carpetas de salida existen
os.makedirs(CARPETA_SALIDA_TIFF, exist_ok=True)

# Buscar archivos .tif en la carpeta de entrada
archivos = [f for f in os.listdir(CARPETA_ENTRADA) if f.lower().endswith(".tif")]

if not archivos:
    print("No se encontraron archivos .tif para convertir.")
else:
    print(f"Convirtiendo {len(archivos)} archivos...")

# Procesar cada imagen
for archivo in archivos:
    ruta_tif = os.path.join(CARPETA_ENTRADA, archivo)
    ruta_tif_opt = os.path.join(CARPETA_SALIDA_TIFF, archivo)  # Imagen optimizada

    try:
        with Image.open(ruta_tif) as img:
            # Convertir a RGB para compatibilidad
            img = img.convert("RGB")

            # Ajustar el contraste
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.5)  # Ajustar el factor según sea necesario

            # Reducir el ruido
            img = img.filter(ImageFilter.MedianFilter(size=3))

            # Guardar la imagen optimizada sin cambiar el tamaño
            img.save(ruta_tif_opt, format='TIFF', compression='tiff_deflate')  # Usar compresión TIFF Deflate para optimización

        print(f"Imagen optimizada: {ruta_tif_opt}")

    except Exception as e:
        print(f"Error inesperado con {archivo}: {e}")

print("Optimización de imágenes TIFF completada.")



