import subprocess
import os

# Rutas a los scriptsss
script_opt = r"D:\xampp\htdocs\pdf_2\convertir_tiff_opt.py"
script_pdf = r"D:\xampp\htdocs\pdf_2\convertir_tiff_pdf.py"
script_pdfa = r"D:\xampp\htdocs\pdf_2\convertir_pdf_pdfa.py"

def ejecutar_script(script_path):
    try:
        print(f"Ejecutando el script: {script_path}")
        result = subprocess.run(["python", script_path], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Error al ejecutar {script_path}: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"Error inesperado al ejecutar {script_path}: {e}")
        return False

# Ejecutar el script para optimizar los archivos TIFF
print("Ejecutando la optimización de archivos TIFF...")
if not ejecutar_script(script_opt):
    exit(1)

# Ejecutar el script para convertir los archivos TIFF optimizados a PDF
print("Ejecutando la conversión de archivos TIFF a PDF...")
if not ejecutar_script(script_pdf):
    exit(1)

# Ejecutar el script para convertir los archivos PDF a PDF/A
print("Ejecutando la conversión de archivos PDF a PDF/A...")
if not ejecutar_script(script_pdfa):
    exit(1)

print("Todos los scripts se ejecutaron correctamente.")