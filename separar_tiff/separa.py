import os

def agrupar_por_s(carpeta):
    # Listar todos los archivos en la carpeta, ordenados alfabéticamente
    archivos = sorted([f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))])
    print(f"Archivos encontrados: {archivos}")
    grupos = []
    grupo_actual = []

    for archivo in archivos:
        # Si el archivo contiene "-S", inicia un nuevo grupo
        if "-S" in archivo:
            if grupo_actual:
                grupos.append(grupo_actual)
            grupo_actual = [archivo]
        else:
            grupo_actual.append(archivo)

    if grupo_actual:
        grupos.append(grupo_actual)

    print(f"Grupos creados: {grupos}")
    return grupos

def main():
    # Ruta de la carpeta donde están los archivos
    carpeta = r"D:\pruebas_separacion"

    if not os.path.exists(carpeta):
        print(f"La carpeta {carpeta} no existe.")
        return

    # Prefijo personalizado para las carpetas
    prefijo = input("Introduce el prefijo para las carpetas (por ejemplo, 12345_74A): ")

    # Agrupar archivos por la aparición de "-S"
    grupos = agrupar_por_s(carpeta)

    # Crear carpetas y mover archivos
    for i, grupo in enumerate(grupos, start=1):
        carpeta_grupo = os.path.join(carpeta, f"{prefijo}_Grupo_{i}")
        os.makedirs(carpeta_grupo, exist_ok=True)

        for archivo in grupo:
            ruta_origen = os.path.join(carpeta, archivo)
            ruta_destino = os.path.join(carpeta_grupo, archivo)
            os.rename(ruta_origen, ruta_destino)
            print(f"Movido: {ruta_origen} -> {ruta_destino}")

    print("Archivos agrupados y movidos a sus respectivas carpetas.")

if __name__ == "__main__":
    main()