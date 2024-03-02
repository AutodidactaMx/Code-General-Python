from extraccion.servicio_extraccion import ServicioExtraccion
from visualizacion.servicio_exposicion import ServicioExposicionDatos
from config import RUTA, NOMBRE_ARCHIVO
extraccion = ServicioExtraccion()
extraccion.extrar_datos_excel(RUTA, NOMBRE_ARCHIVO)
visualizar = ServicioExposicionDatos()
visualizar.visualizar_datos_excel()
