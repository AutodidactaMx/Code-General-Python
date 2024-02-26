import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
from selenium.webdriver.chrome.options import Options
from conf.rutas import URL_TEMPERATURAS_LLUVIAS, RUTA_CONTROLADOR, RUTA_DESCARGA
import util.util_ventana as util
from pandastable import Table
import tkinter as tk
import glob
import datetime


class ExtraccionDatosClimaticosService():

    def __init__(self):
        self.driver = None
        self.url = URL_TEMPERATURAS_LLUVIAS
        self.ruta_controlador = RUTA_CONTROLADOR
        self.ruta_descarga = RUTA_DESCARGA
        self.vars = {}
        self.df = None

    def configurar_webdriver(self):
        # Crear opciones de Chrome
        chrome_options = Options()
        prefs = {"download.default_directory": self.ruta_descarga}
        chrome_options.add_experimental_option("prefs", prefs)
        # Inicializar el WebDriver (en este caso, para Chrome)
        self.driver = webdriver.Chrome(
            self.ruta_controlador, chrome_options=chrome_options)

    def esperar_ventana(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def convertir_mes(self, numero_mes):
        # Convertir el número de mes a su representación con dos dígitos
        numero_mes_formateado = "{:02d}.".format(numero_mes)

        # Obtener el nombre del mes en español
        nombres_meses = {
            "January": "Enero",
            "February": "Febrero",
            "March": "Marzo",
            "April": "Abril",
            "May": "Mayo",
            "June": "Junio",
            "July": "Julio",
            "August": "Agosto",
            "September": "Septiembre",
            "October": "Octubre",
            "November": "Noviembre",
            "December": "Diciembre"
        }

        nombre_mes = datetime.date(2000, numero_mes, 1).strftime('%B')
        nombre_mes_espanol = nombres_meses[nombre_mes]

        return f"{numero_mes_formateado} {nombre_mes_espanol}"

    def extraer_datos(self, anio, numero_mes, opcion):
        mes = self.convertir_mes(numero_mes)
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.ID, "N0").click()
        dropdown = self.driver.find_element(By.ID, "N0")
        dropdown.find_element(By.XPATH, f"option[. = '{anio}']").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "N1").click()
        dropdown = self.driver.find_element(By.ID, "N1")
        dropdown.find_element(By.XPATH, f"//option[. = '{mes}']").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "N2").click()
        dropdown = self.driver.find_element(By.ID, "N2")
        dropdown.find_element(By.XPATH, f"//option[. = '{opcion}']").click()
        time.sleep(10)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(
            By.CSS_SELECTOR, "#boton_descargar_datos > .btn").click()

        self.vars["winNueva"] = self.esperar_ventana(4000)
        self.vars["winRoot"] = self.driver.current_window_handle

        time.sleep(10)
        self.driver.close()

    def extraer_tabla(self, anio, numero_mes, opcion):
        self.configurar_webdriver()
        self.extraer_datos(anio, numero_mes, opcion)
        self.driver.quit()

    def cargar_tabla(self):
        # Encontrar todos los archivos CSV en el directorio
        archivos_csv = glob.glob(self.ruta_descarga + "\\*.csv")

        # Cargar todos los archivos CSV en un solo DataFrame
        dfs = []
        for archivo in archivos_csv:
            df_temporal = pd.read_csv(archivo, encoding='mbcs')
            dfs.append(df_temporal)

        self.df = pd.concat(dfs, ignore_index=True)

    def mostrar_tabla(self, opcion):
        if self.df is None:
            print("Error: No se ha extraído ninguna tabla.")
        root = tk.Tk()
        util.centrar_ventana(root, 900, 800)
        root.title(opcion)
        frame = tk.Frame(root)
        frame.pack(fill='both', expand=True)
        pt = Table(frame, dataframe=self.df)
        pt.show()
        root.mainloop()
