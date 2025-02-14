from PIL import Image
import os
import subprocess

# 📂 Rutas
CARPETA_ENTRADA = r"D:\xampp\htdocs\pdf_2\imagenes_convertidas"
CARPETA_SALIDA = r"D:\xampp\htdocs\pdf_2\output"

# 📌 Asegurar que la carpeta de salida existe
os.makedirs(CARPETA_SALIDA, exist_ok=True)

# 🔍 Buscar archivos .tif en la carpeta de entrada
archivos = [f for f in os.listdir(CARPETA_ENTRADA) if f.lower().endswith(".tif")]

if not archivos:
    print("⚠ No se encontraron archivos .tif para convertir.")
else:
    print(f"🔄 Convirtiendo {len(archivos)} archivos...")

# 🔄 Procesar cada imagen
for archivo in archivos:
    ruta_tif = os.path.join(CARPETA_ENTRADA, archivo)
    ruta_tif_temp = os.path.join(CARPETA_ENTRADA, "temp_" + archivo)  # Imagen escalada
    ruta_pdf = os.path.join(CARPETA_SALIDA, archivo.replace(".tif", ".pdf"))

    try:
        with Image.open(ruta_tif) as img:
            # 📌 Convertir a RGB y calcular nuevo tamaño
            img = img.convert("RGB")

            # 📌 Forzar tamaño completo en A4 (sin márgenes grandes)
            A4_WIDTH = 595  # Tamaño en puntos de A4
            A4_HEIGHT = 842

            img = img.resize((A4_WIDTH, A4_HEIGHT), Image.LANCZOS)  
            img.save(ruta_tif_temp)  # Guardar la imagen temporal ajustada

        # 📌 Comando para convertir a PDF/A sin bordes extra
        comando = [
            "D:\\LibreOffice\\program\\soffice.exe",
            "--headless",
            "--convert-to", 'pdf:draw_pdf_Export:{"SelectPdfVersion":1}',
            ruta_tif_temp,
            "--outdir", CARPETA_SALIDA
        ]

        print(f"➡ Convirtiendo: {archivo}...")
        resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # 📌 Verificar si hubo error
        if "Error" in resultado.stderr:
            print(f"❌ Error con {archivo}: {resultado.stderr}")
        else:
            print(f"✅ Convertido: {ruta_pdf}")

        # ❌ Eliminar el archivo temporal
        os.remove(ruta_tif_temp)

    except Exception as e:
        print(f"⚠ Error inesperado con {archivo}: {e}")

print("🎉 Conversión completada.")



