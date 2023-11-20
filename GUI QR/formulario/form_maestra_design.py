import tkinter as tk
from tkinter import ttk
import util.util_ventana as util_ven
from PIL import Image, ImageTk, ImageDraw
import util.util_imagenes as util_img
import config as conf


class FormMestroDesign(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.qr_guardado = None
        self.qr_img_base = util_img.leer_imagen("./imagenes/qr_base.png", (330, 330))
        self.qr_mensaje = util_img.leer_imagen("./imagenes/escanea_me.png", (300, 200))
        self.config_window()
        self.paneles()
        self.widget_panel_superior()
        self.widget_panel_inferior()

    def config_window(self):
        self.title('QR Diseño de Código')
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 800, 450
        util_ven.centrar_ventana(self, w, h)

    def paneles(self):

        self.barra_superior = tk.Frame(self,)
        self.barra_superior.pack(side=tk.TOP, fill='both', expand=True)

        self.barra_superior_izq = tk.Frame(
            self.barra_superior, bg=conf.COLOR_BARRA_SUPERIOR_IZQ)
        self.barra_superior_izq.pack(side=tk.LEFT, fill='both', expand=True)
        self.barra_superior_der = tk.Frame(
            self.barra_superior, bg=conf.COLOR_BARRA_SUPERIOR_DER)
        self.barra_superior_der.pack(side=tk.RIGHT, fill='both', expand=True)

        self.barra_inferior = tk.Frame(
            self, bg=conf.COLOR_BARRA_INFERIOR, height=50)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='x', expand=False)

    def widget_panel_superior(self):

        self.labelTitulo = tk.Label(
            self.barra_superior_izq, text="QR Diseño de Código", bg=conf.COLOR_BARRA_SUPERIOR_IZQ)
        self.labelTitulo.config(fg="#000000", font=(
            "Roboto", 18, "bold"), pady=10, width=16)
        self.labelTitulo.pack(side=tk.TOP, expand=False, pady=20)

        estilo = ttk.Style()
        estilo.configure("EstiloEntry.TEntry", padding=(
            10, 5, 10, 5), relief="flat")

        self.entrada_texto = ttk.Entry(
            self.barra_superior_izq, width=50, style="EstiloEntry.TEntry")
        self.entrada_texto.pack(side=tk.TOP, expand=False, pady=20)

        self.placeholder_text = "https://autodidacta.mx/"
        self.entrada_texto.insert(0, self.placeholder_text)
        self.entrada_texto.bind("<FocusIn>", self.on_entry_focus_in)
        self.entrada_texto.bind("<FocusOut>", self.on_entry_focus_out)                   

        self.etiqueta_mensaje = ttk.Label(self.barra_superior_izq, image=self.qr_mensaje, border=100)
        self.etiqueta_mensaje.pack(side=tk.TOP, expand=True, pady=20, padx=20)

        self.etiqueta_qr = ttk.Label(self.barra_superior_der,image=self.qr_img_base)
        self.etiqueta_qr.pack(side=tk.TOP, expand=True, pady=20, padx=20)
        

    def on_entry_focus_in(self, event):
        pass

    def on_entry_focus_out(self, event):
        pass

    def widget_panel_inferior(self):

        self.boton_generar = tk.Button(self.barra_inferior, text="Generar Codigo", width=15, height=2,
                                       bg=conf.COLOR_BOTON, fg=conf.COLOR_TEXTO_BOTON, relief=tk.FLAT, padx=5, pady=5, bd=0, borderwidth=0, highlightthickness=0,
                                       overrelief='flat', command=self.on_button_click_mostrar_qr)
        self.boton_generar.pack(side=tk.RIGHT, expand=False, padx=10, pady=10)

        self.boton_descargar = tk.Button(self.barra_inferior, text="Descargar Codigo", width=15, height=2,
                                         bg=conf.COLOR_BOTON, fg=conf.COLOR_TEXTO_BOTON, relief=tk.FLAT, padx=5, pady=5, bd=0, borderwidth=0, highlightthickness=0,
                                         overrelief='flat', command=self.on_button_click_guardar_qr)
        self.boton_descargar.pack(
            side=tk.RIGHT, expand=False, padx=10, pady=10)

    def on_button_click_mostrar_qr(self):
        pass

    def on_button_click_guardar_qr(self):
        pass
