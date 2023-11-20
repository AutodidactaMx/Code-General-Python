import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
from formulario.form_maestra_design import FormMestroDesign


class FormMestro(FormMestroDesign):

    def __init__(self) -> None:
        super().__init__()

    def on_entry_focus_in(self, event):
        if self.entrada_texto.get() == self.placeholder_text:
            self.entrada_texto.delete(0, tk.END)

    def on_entry_focus_out(self, event):
        if not self.entrada_texto.get():
            self.entrada_texto.insert(0, self.placeholder_text)

    def generar_qr_con_forma(self, texto):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(texto)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        return img

    def on_button_click_mostrar_qr(self):
        texto = self.entrada_texto.get()        
        qr_image = self.generar_qr_con_forma(texto)
        img_tk = ImageTk.PhotoImage(qr_image)
        self.etiqueta_qr.config(image=img_tk)
        self.etiqueta_qr.image = img_tk
        self.qr_guardado = qr_image

    def on_button_click_guardar_qr(self):
        archivo = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("Archivos PNG", "*.png")])
        if archivo:
            self.qr_guardado.save(archivo)
