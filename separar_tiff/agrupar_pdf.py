import os
from PIL import Image
from PyPDF2 import PdfWriter
from io import BytesIO

def agrupar_archivos_en_pdf(ruta_carpeta, ruta_salida, nombre_carpeta):
    """
    Agrupa todos los archivos TIFF en una carpeta en un único archivo PDF.
    El archivo PDF se guarda en la ruta de salida con el nombre de la carpeta.
    """
    # Crear un objeto PdfWriter
    writer = PdfWriter()

    # Recorrer todos los archivos en la carpeta
    archivos_tiff = [archivo for archivo in sorted(os.listdir(ruta_carpeta)) if archivo.lower().endswith((".tiff", ".tif"))]
    for archivo in archivos_tiff:
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        try:
            with Image.open(ruta_archivo) as img:
                # Convertir cada página TIFF a RGB y agregarla al PDF
                for page in range(img.n_frames):
                    img.seek(page)
                    pdf_page = img.convert("RGB")
                    # Guardar la página en memoria usando BytesIO
                    pdf_bytes = BytesIO()
                    pdf_page.save(pdf_bytes, format="PDF")
                    pdf_bytes.seek(0)
                    writer.append(pdf_bytes)
            print(f"Procesado: {ruta_archivo}")
        except Exception as e:
            print(f"Error al procesar {ruta_archivo}: {e}")

    # Guardar el archivo PDF combinado en la ruta de salida
    salida_pdf = os.path.join(ruta_salida, f"{nombre_carpeta}.pdf")
    if writer.pages:  # Verificar si hay páginas para combinar
        os.makedirs(ruta_salida, exist_ok=True)  # Crear la ruta de salida si no existe
        with open(salida_pdf, "wb") as f:
            writer.write(f)
        print(f"PDF combinado creado: {salida_pdf}")
    else:
        print(f"No se encontraron archivos TIFF en la carpeta: {ruta_carpeta}")

def main():
    """
    Solicita la ruta principal y procesa cada carpeta dentro de ella.
    """
    # Solicitar la ruta principal
    ruta_principal = input("Introduce la ruta principal donde buscar las carpetas: ").strip()
    ruta_salida = os.path.join(ruta_principal, "pdf_generados")

    if not os.path.exists(ruta_principal):
        print(f"La ruta {ruta_principal} no existe.")
        return

    # Crear la carpeta de salida "pdf_generados" dentro de la ruta principal
    os.makedirs(ruta_salida, exist_ok=True)

    # Recorrer todas las carpetas dentro de la ruta principal
    for carpeta_raiz, subcarpetas, archivos in os.walk(ruta_principal):
        if archivos:  # Si la carpeta contiene archivos
            nombre_carpeta = os.path.basename(carpeta_raiz)  # Obtener el nombre de la carpeta
            print(f"Procesando carpeta: {carpeta_raiz}")
            agrupar_archivos_en_pdf(carpeta_raiz, ruta_salida, nombre_carpeta)

if __name__ == "__main__":
    main()