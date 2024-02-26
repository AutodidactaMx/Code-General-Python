import argparse
from servicio.extraccion_tabla_service import ExtraccionTablaHidroestimadorService
from servicio.extraccion_datos_climaticos_service import ExtraccionDatosClimaticosService
# Crear el parser de argumentos
parser = argparse.ArgumentParser(
    description="Programa para extraer datos climáticos o tabulares")
# Agregar argumentos para las diferentes opciones
parser.add_argument('-o', '--opcion',  required=True, choices=[
                    'datos_hidroestimador', 'datos_climaticos'], help="Opción a ejecutar ('datos_hidroestimador' o 'datos_climaticos')")
parser.add_argument('-a', '--anio', required=False, type=int, help="Año de búsqueda")
parser.add_argument('-m', '--mes',  required=False, type=int, help="Mes de búsqueda")
parser.add_argument('-t', '--opciontemp',  required=False, choices=[
                    'Temperatura Media', 'Temperatura Máxima', 'Temperatura Mínima'],
                    help="Opción a ejecutar ('Temperatura Media', 'Temperatura Máxima','Temperatura Mínima')")


# Parsear los argumentos de la línea de comandos
args = parser.parse_args()
# Según la opción seleccionada, ejecutar el servicio correspondiente

if args.opcion == 'datos_hidroestimador':
    # Crear una instancia de la clase ExtraccionTabla
    extraccion = ExtraccionTablaHidroestimadorService()
    # Extraer y mostrar la tabla
    extraccion.extraer_tabla()
    extraccion.mostrar_tabla()
elif args.opcion == 'datos_climaticos':
    # Ejecutar el servicio de extracción de datos climáticos
    # Crear una instancia de la clase ExtraccionDatosClimaticos
    extraccion = ExtraccionDatosClimaticosService()
    extraccion.extraer_tabla(args.anio, args.mes, args.opciontemp )
    extraccion.cargar_tabla()
    extraccion.mostrar_tabla( args.opciontemp )
