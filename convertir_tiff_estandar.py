from PIL import Image
import os

# 📂 Rutas de entrada y salida
CARPETA_ENTRADA = r"D:\xampp\htdocs\pdf_2\images"  # 📌 Cambia esto si es necesario
CARPETA_SALIDA = r"D:\xampp\htdocs\pdf_2\imagenes_convertidas"

# 📌 Asegurar que la carpeta de salida existe
os.makedirs(CARPETA_SALIDA, exist_ok=True)

# 🔄 Procesar archivos TIFF
for archivo in os.listdir(CARPETA_ENTRADA):
    if archivo.lower().endswith(".tif"):
        ruta_tif = os.path.join(CARPETA_ENTRADA, archivo)
        ruta_convertida = os.path.join(CARPETA_SALIDA, archivo)

        try:
            with Image.open(ruta_tif) as img:
                img = img.convert("RGB")  # Convertir a RGB estándar
                img.save(ruta_convertida, "TIFF", compression="none")  # Sin compresión
                print(f"✅ Convertido: {ruta_convertida}")
        except Exception as e:
            print(f"❌ Error con {archivo}: {e}")

print("🎉 Conversión de TIFF completada.")
