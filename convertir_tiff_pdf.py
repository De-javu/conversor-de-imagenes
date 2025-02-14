from PIL import Image
import os
import pikepdf  # Para modificar la versión del PDF

# 📂 Rutas
CARPETA_ENTRADA = r"D:\xampp\htdocs\pdf_2\images"
CARPETA_SALIDA = r"D:\xampp\htdocs\pdf_2\imagenes_convertidas_pdf"

# 📌 Asegurar que la carpeta de salida existe
os.makedirs(CARPETA_SALIDA, exist_ok=True)

# 🔍 Buscar archivos .tif en la carpeta de entrada
archivos = [f for f in os.listdir(CARPETA_ENTRADA) if f.lower().endswith(".tif")]

for archivo in archivos:
    ruta_tif = os.path.join(CARPETA_ENTRADA, archivo)
    ruta_pdf = os.path.join(CARPETA_SALIDA, archivo.replace(".tif", ".pdf"))
    
    try:
        with Image.open(ruta_tif) as img:
            img = img.convert("RGB")  # Convertir a RGB para compatibilidad

            # 📌 Reducir el peso sin perder mucha calidad
            img.save(ruta_pdf, "PDF", resolution=200, quality=85)

            # 📌 Cambiar la versión del PDF a 1.7 o 2.0
            with pikepdf.open(ruta_pdf) as pdf:
                pdf.save(ruta_pdf, pdf_version=pikepdf.PdfVersion.PDF_1_7)  # Cambia a 1.7
                # pdf.save(ruta_pdf, pdf_version=pikepdf.PdfVersion.PDF_2_0)  # Si quieres 2.0

            print(f"✅ PDF optimizado creado: {ruta_pdf}")

    except Exception as e:
        print(f"❌ Error con {archivo}: {e}")

print("🎉 Conversión de TIFF a PDF 1.7/2.0 optimizada completada.")
