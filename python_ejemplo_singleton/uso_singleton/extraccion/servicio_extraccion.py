import pandas as pd
from modelo.objeto_almacenamiento import ObjetoAlmacenamiento

class ServicioExtraccion():

    def __init__(self) -> None:
        pass

    def extrar_datos_excel(self, ruta:str, nombre_archivo:str):
        df = pd.read_csv(f"{ruta}/{nombre_archivo}")
        obj = ObjetoAlmacenamiento()
        obj.asignar_dato(df)        
        

