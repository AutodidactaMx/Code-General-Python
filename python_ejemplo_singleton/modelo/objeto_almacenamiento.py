from singleton_decorator import singleton
import pandas as pd

@singleton
class ObjetoAlmacenamiento:
    def __init__(self) -> None:
        self.__data_frame: pd.DataFrame = pd.DataFrame()
    
    def obtener_dato(self) -> pd.DataFrame:
        return self.__data_frame 

    def asignar_dato(self, objeto: pd.DataFrame) -> None:
        self.__data_frame = objeto
