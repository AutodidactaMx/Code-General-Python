# Tutorial de Aplicación CRUD con Python y SQLAlchemy

Este proyecto tutorial tiene como objetivo enseñarte a crear una aplicación CRUD que te permita insertar, modificar, eliminar y consultar registros en una tabla de una base de datos. Además, proporciona el código necesario para crear la tabla requerida para consumir esta base de datos.

## Requisitos

- Python 3.9 o superior
- Paquete SQLAlchemy==2.0.27

Puedes instalar los requisitos con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Descripción

Este tutorial te introduce a una arquitectura básica de capas, donde separamos la lógica en diferentes componentes:

1. **Capa de Presentación:** Utilizamos Tkinter para la interfaz gráfica de usuario.
2. **Capa de Servicio o Aplicación:** Aquí se encuentra la lógica de la aplicación.
3. **Capa de Persistencia:** Utilizamos SQLAlchemy para interactuar con la base de datos.

Al separar la aplicación en estas tres capas, facilitamos la comprensión y mantenimiento del código, además de permitir una distribución más eficiente.

## Instalación y Uso

1. Clona este repositorio en tu máquina local.
2. Instala los requisitos con `pip install -r requirements.txt`.
3. Ejecuta la aplicación con `python main.py`.

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/feature-name`).
3. Haz tus cambios y realiza commit (`git commit -am 'Add new feature'`).
4. Haz push a la rama (`git push origin feature/feature-name`).
5. Crea un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
