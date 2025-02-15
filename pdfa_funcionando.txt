import os
import img2pdf
from PIL import Image
import subprocess

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
    ruta_pdfa = os.path.join(CARPETA_SALIDA, archivo.replace(".tif", "_pdfa.pdf"))

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

        # 📌 Convertir el PDF a PDF/A usando Ghostscript
        gs_command = [
            "gswin64c",  # Comando para Ghostscript en Windows
            "-dPDFA",
            "-dBATCH",
            "-dNOPAUSE",
            "-dNOOUTERSAVE",
            "-sProcessColorModel=DeviceRGB",
            "-sDEVICE=pdfwrite",
            "-dPDFACompatibilityPolicy=1",
            f"-sOutputFile={ruta_pdfa}",
            ruta_pdf
        ]
        subprocess.run(gs_command, check=True)

        print(f"✅ PDF/A de alta calidad (300 DPI, versión PDF/A) creado: {ruta_pdfa}")

    except Exception as e:
        print(f"❌ Error con {archivo}: {e}")

print("🎉 Conversión de TIFF a PDF/A con 300 DPI completada.")