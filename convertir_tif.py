import os
import subprocess
import shlex
from PIL import Image

# 📂 Rutas de entrada y salida
CARPETA_ENTRADA = r"D:\xampp\htdocs\pdf_2\imagenes_convertidas"  # Carpeta con los archivos .tif
CARPETA_SALIDA = r"D:\xampp\htdocs\pdf_2\output"  # Carpeta donde se guardarán los PDFs

# 📌 Asegurar que la carpeta de salida existe
os.makedirs(CARPETA_SALIDA, exist_ok=True)

# 🔍 Buscar archivos .tif en la carpeta de entrada
archivos = [f for f in os.listdir(CARPETA_ENTRADA) if f.lower().endswith(".tif")]

if not archivos:
    print("⚠ No se encontraron archivos .tif para convertir.")
else:
    print(f"🔄 Convirtiendo {len(archivos)} archivos...")

# 🔄 Procesar cada archivo
for archivo in archivos:
    ruta_tif = os.path.join(CARPETA_ENTRADA, archivo)
    ruta_temp = os.path.join(CARPETA_ENTRADA, f"temp_{archivo}")  # Imagen temporal
    ruta_pdf = os.path.join(CARPETA_SALIDA, archivo.replace(".tif", ".pdf"))

    # 📌 Redimensionar la imagen al tamaño A4 (595x842 puntos en PDF)
    try:
        with Image.open(ruta_tif) as img:
            img = img.convert("L")  # Convertir a escala de grises (mejor para PDF/A)
            img = img.resize((595, 842))  # Ajuste a tamaño A4
            img.save(ruta_temp, "TIFF")  # Guardamos la nueva imagen temporalmente
    except Exception as e:
        print(f"⚠ Error al redimensionar {archivo}: {e}")
        continue

    # 📌 Comando para convertir a PDF/A
    comando = f'soffice --headless --convert-to "pdf:writer_pdf_Export:{{\\"SelectPdfVersion\\":1,\\"ReduceTransparency\\":true}}" {shlex.quote(ruta_temp)} --outdir {shlex.quote(CARPETA_SALIDA)}'

    try:
        print(f"➡ Convirtiendo: {archivo}...")
        resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # 📌 Verificar si la conversión fue exitosa
        if "Error" in resultado.stderr:
            print(f"❌ Error con {archivo}: {resultado.stderr}")
        else:
            print(f"✅ Convertido: {ruta_pdf}")

        # ❌ Borrar el archivo temporal
        os.remove(ruta_temp)

    except Exception as e:
        print(f"⚠ Error inesperado con {archivo}: {e}")

print("🎉 Conversión completada.")



