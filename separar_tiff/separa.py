import os

def agrupar_por_s(carpeta):
    # Listar todos los archivos en la carpeta, ordenados alfabéticamente
    archivos = sorted([f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))])
    grupos = []
    grupo_actual = []

    for i, archivo in enumerate(archivos):
        # Si el archivo contiene "-S", inicia un nuevo grupo
        if "-S" in archivo:
            # Si ya hay un grupo actual, lo agregamos a la lista de grupos
            if grupo_actual:
                grupos.append(grupo_actual)
            # Iniciar un nuevo grupo con el archivo actual
            grupo_actual = [archivo]
        else:
            # Agregar el archivo al grupo actual
            grupo_actual.append(archivo)

    # Agregar el último grupo si no está vacío
    if grupo_actual:
        grupos.append(grupo_actual)

    return grupos

def main():
    # Ruta de la carpeta donde están los archivos
    carpeta = r"D:\pruebas_separacion"

    if not os.path.exists(carpeta):
        print(f"La carpeta {carpeta} no existe.")
        return

    # Agrupar archivos por la aparición de "-S"
    grupos = agrupar_por_s(carpeta)

    # Crear carpetas y mover archivos
    for i, grupo in enumerate(grupos, start=1):
        carpeta_grupo = os.path.join(carpeta, f"Grupo_{i}")
        os.makedirs(carpeta_grupo, exist_ok=True)  # Crear la carpeta si no existe

        for archivo in grupo:
            ruta_origen = os.path.join(carpeta, archivo)
            ruta_destino = os.path.join(carpeta_grupo, archivo)
            os.rename(ruta_origen, ruta_destino)  # Mover el archivo
            print(f"Movido: {ruta_origen} -> {ruta_destino}")

    print("Archivos agrupados y movidos a sus respectivas carpetas.")

if __name__ == "__main__":
    main()