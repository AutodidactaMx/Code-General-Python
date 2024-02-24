import os


def crear_carpeta_si_no_existe(ruta, nombre_carpeta):
    """
    Crea una carpeta en la ruta especificada si no existe.

    Args:
        ruta (str): La ruta donde se creará la carpeta.
        nombre_carpeta (str): El nombre de la carpeta a crear.

    Returns:
        str: Mensaje indicando si la carpeta se creó o si ya existía.
    """
    ruta_completa = os.path.join(ruta, nombre_carpeta)

    # Verificamos si la carpeta no existe antes de crearla
    if not os.path.exists(ruta_completa):
        os.makedirs(ruta_completa)
        return True, f"Se ha creado la carpeta '{nombre_carpeta}' en '{ruta}'"
    else:
        return False, f"La carpeta '{nombre_carpeta}' ya existe en '{ruta}'"
