import os
import pikepdf  # Para modificar la versión del PDF
import img2pdf
from PIL import Image

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
            width, height = img.size

            # 📌 Convertir los valores de DPI a enteros
            dpi_x, dpi_y = map(int, img.info['dpi'])

            # 📌 Calcular el tamaño de la página en puntos basado en las dimensiones de la imagen
            page_width = width * 300 / dpi_x
            page_height = height * 300 / dpi_y

            # 📌 Convertir la imagen TIFF a PDF con 300 DPI usando img2pdf
            pdf_bytes = img2pdf.convert(
                ruta_tif,
                layout_fun=img2pdf.get_layout_fun((page_width, page_height)),
                dpi=300
            )
            with open(ruta_pdf, "wb") as f:
                f.write(pdf_bytes)

        # 📌 Cambiar la versión del PDF a 1.7 o 2.0
        with pikepdf.open(ruta_pdf) as pdf:
            pdf.save(ruta_pdf, version=pikepdf.PdfVersion.V1_7)  # Cambia a PDF 1.7
            # pdf.save(ruta_pdf, version=pikepdf.PdfVersion.V2_0)  # Si quieres PDF 2.0

        print(f"✅ PDF de alta calidad (300 DPI, versión 1.7) creado: {ruta_pdf}")

    except Exception as e:
        print(f"❌ Error con {archivo}: {e}")

print("🎉 Conversión de TIFF a PDF 1.7/2.0 con 300 DPI completada.")