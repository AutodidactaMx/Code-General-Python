import sqlalchemy as db  # Importamos SQLAlchemy para interactuar con la base de datos
import util.generico as gen  # Importamos un módulo personalizado para funcionalidades genéricas
import dominio.modelos as modelos  # Importamos los modelos de la base de datos

# Nombre de la carpeta que deseas crear para almacenar la base de datos
nombre_carpeta = "bd"
# Ruta donde deseas crear la carpeta para almacenar la base de datos
ruta = "./"

# Creamos la carpeta si no existe
gen.crear_carpeta_si_no_existe(ruta, nombre_carpeta)

# Creamos una conexión al motor de la base de datos SQLite
# Especificamos el nombre y la ubicación del archivo de la base de datos
engine = db.create_engine('sqlite:///bd/tienda.sqlite', echo=True, future=True)

# Creamos todas las tablas definidas en nuestros modelos en la base de datos
modelos.Base.metadata.create_all(engine)
