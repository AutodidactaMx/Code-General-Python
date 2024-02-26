from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import tkinter as tk
from pandastable import Table
import time
from conf.rutas import URL_HIDROESTIMADOR, RUTA_CONTROLADOR
import  util.util_ventana as util

class ExtraccionTablaHidroestimadorService():
    def __init__(self):
        self.url = URL_HIDROESTIMADOR
        self.ruta_controlador = RUTA_CONTROLADOR
        self.df = None

    def extraer_tabla(self):
        # Inicializar el WebDriver (en este caso, para Chrome)
        driver = webdriver.Chrome(self.ruta_controlador)

        # Abrir la página en el navegador
        driver.get(self.url)

        # Esperar a que la tabla cargue completamente
        driver.implicitly_wait(10)  # Espera implícita de 10 segundos
        time.sleep(5)
        driver.switch_to.frame(0)
        # Encontrar la tabla por su etiqueta y clase
        tabla = driver.find_element(By.XPATH, '//*[@id="tbllistado"]')

        # Obtener el HTML de la tabla
        html_tabla = tabla.get_attribute("outerHTML")

        # Usar Pandas para leer la tabla y convertirla en un DataFrame
        self.df = pd.read_html(html_tabla)[0]

        # Cerrar el navegador al finalizar
        driver.quit()

    def mostrar_tabla(self):
        if self.df is None:
            print("Error: No se ha extraído ninguna tabla.")
            return        
        root = tk.Tk()
        util.centrar_ventana(root,700,800)
        root.title('Tabla Extraída')

        frame = tk.Frame(root)
        frame.pack(fill='both', expand=True)

        pt = Table(frame, dataframe=self.df)
        pt.show()

        root.mainloop()