import sqlalchemy as db
from sqlalchemy.orm import Session
from dominio.modelos import ProductoModel
from typing import List  # Asegúrate de importar List de typing
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class ServicioProducto():
    
    def __init__(self):        
        self.engine = db.create_engine('sqlite:///bd/tienda.sqlite', echo=True, future=True)

    def register(self, nombre, precio):
        producto = ProductoModel()
        producto.nombre = nombre
        producto.precio = precio
        with Session(self.engine) as session:
            session.add(producto)
            session.commit()
    
    def modificar(self, nombre, precio, producto_id):
        try:
            # Buscar el producto en la base de datos
            with Session(self.engine) as session:
                producto = session.query(ProductoModel).filter_by(id=producto_id).one()

                # Actualizar los atributos del producto
                producto.nombre = nombre
                producto.precio = precio

                # Confirmar los cambios en la base de datos
                session.commit()
                print(f"Producto con ID {producto_id} actualizado correctamente.")
                return True
        except NoResultFound:
            print(f"No se encontró ningún producto con ID {producto_id}. No se realizó ninguna modificación.")
            return False
        except Exception as e:
            print(f"Error al actualizar el producto: {e}")
            return False
 
    def obtener_productos(self) -> List[ProductoModel]:  
        productos: ProductoModel = None
        with Session(self.engine) as session:
            productos = session.query(ProductoModel).all()
        return productos
    
    def eliminar(self, producto_id):
        with Session(self.engine) as session:
            producto = session.query(ProductoModel).filter_by(id=producto_id).first()
            if producto:
                try:
                    session.delete(producto)
                    session.commit()
                    print(f"Producto con ID {producto_id} eliminado correctamente.")
                except IntegrityError as e:
                    session.rollback()
                    print(f"No se pudo eliminar el producto con ID {producto_id}. Error: {e}")
            else:
                print(f"No se encontró ningún producto con ID {producto_id}.")