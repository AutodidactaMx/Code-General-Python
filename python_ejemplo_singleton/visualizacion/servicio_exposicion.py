from modelo.objeto_almacenamiento import ObjetoAlmacenamiento


class ServicioExposicionDatos():
    def __init__(self) -> None:
        pass

    def visualizar_datos_excel(self):
        obj = ObjetoAlmacenamiento()
        print(obj.obtener_dato())