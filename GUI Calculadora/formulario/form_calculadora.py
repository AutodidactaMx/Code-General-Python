import tkinter as tk
from tkinter import font
import util.util_ventana as util_ventana
from config import constantes as cons


class FormularioCalculadora(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config_window()
        self.construir_widget()
        self.construir_widget_toggle()

    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Python GUI Calculadora')
        # Configurar el color de fondo y hacer transparente la ventana
        self.configure(bg=cons.COLOR_DE_FONDO_DARK)
        self.attributes('-alpha', 0.96)
        w, h = 370, 570
        util_ventana.centrar_ventana(self, w, h)

    def construir_widget(self):
        # Etiqueta para mostrar la operación solicitada
        self.operation_label = tk.Label(self, text="", font=(
            'Arial', 16), fg=cons.COLOR_DE_TEXTO_DARK, bg=cons.COLOR_DE_FONDO_DARK, justify='right')
        self.operation_label.grid(
            row=0, column=3, padx=10, pady=10)  # Añadido columnspan

        # Pantalla de operacion
        self.entry = tk.Entry(self, width=12, font=(
            'Arial', 40), bd=0, fg=cons.COLOR_DE_TEXTO_DARK, bg=cons.COLOR_CAJA_TEXTO_DARK, justify='right')
        self.entry.grid(row=1, column=0, columnspan=4,
                        padx=10, pady=10)  # Añadido padding

        # Lista de Botones
        buttons = [
            'C', '%', '<', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=',
        ]

        row_val = 2  # Ajustado para dejar espacio para la etiqueta de operación
        col_val = 0

        # Configurar la tipografía "Roboto" para Botones
        roboto_font = font.Font(family="Roboto", size=16)

        for button in buttons:
            # Establecer el color de fondo de los botones especiales
            if button in ['=', '*', '/', '-', '+', 'C', '<', '%']:
                color_fondo = cons.COLOR_BOTONES_ESPECIALES_DARK
                # Ajustar el tamaño de la fuente solo para estos botones
                button_font = font.Font(size=16, weight='bold')
            else:
                color_fondo = cons.COLOR_BOTONES_DARK
                button_font = roboto_font

            # Ajuste para que el botón de '=' abarque dos columnas en una fila
            if button == '=':
                tk.Button(self, text=button, width=11, height=2, 
                          bg=color_fondo, fg=cons.COLOR_DE_TEXTO_DARK, relief=tk.FLAT, font=button_font, padx=5, pady=5, bd=0, borderwidth=0, highlightthickness=0,
                          overrelief='flat').grid(row=row_val, column=col_val, columnspan=2, pady=5)  # Añadido columnspan
                col_val += 1
            else:
                tk.Button(self, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b),
                          bg=color_fondo, fg=cons.COLOR_DE_TEXTO_DARK, relief=tk.FLAT, font=button_font, padx=5, pady=5, bd=0, borderwidth=0, highlightthickness=0,
                          overrelief='flat').grid(row=row_val, column=col_val, pady=5)  # Añadido padding
                col_val += 1

            if col_val > 3:
                col_val = 0
                row_val += 1

    def construir_widget_toggle(self):
        # Iniciar con el tema oscuro
        self.dark_theme = True
        # Configurar la fuente FontAwesome
        font_awesome = font.Font(family='FontAwesome', size=12)
        # Botón para cambiar de tema
        self.theme_button = tk.Button(self, text="Modo Oscuro \uf186", width=13, font=font_awesome,  bd=0, borderwidth=0,
                                      highlightthickness=0, relief=tk.FLAT, command=self.toggle_theme, bg=cons.COLOR_BOTONES_ESPECIALES_LIGHT)
        self.theme_button.grid(row=0, column=0, columnspan=2,
                               pady=0, padx=0, sticky="nw")  # Añadido padx y sticky

    def toggle_theme(self):
        # Cambiar entre temas oscuro y claro
        if self.dark_theme:
            self.configure(bg=cons.COLOR_DE_FONDO_LIGHT)
            self.entry.config(fg=cons.COLOR_DE_TEXTO_LIGHT,
                              bg=cons.COLOR_CAJA_TEXTO_LIGHT)
            self.operation_label.config(
                fg=cons.COLOR_DE_TEXTO_LIGHT, bg=cons.COLOR_DE_FONDO_LIGHT)
            self.theme_button.configure(
                text="\uf185  Modo Claro", relief=tk.SUNKEN,  bg=cons.COLOR_BOTONES_ESPECIALES_LIGHT)
        else:
            self.configure(bg=cons.COLOR_DE_FONDO_DARK)
            self.entry.config(fg=cons.COLOR_DE_TEXTO_DARK,
                              bg=cons.COLOR_CAJA_TEXTO_DARK)
            self.operation_label.config(
                fg=cons.COLOR_DE_TEXTO_DARK, bg=cons.COLOR_DE_FONDO_DARK)
            self.theme_button.configure(
                text="Modo Oscuro \uf186", relief=tk.RAISED, bg=cons.COLOR_BOTONES_ESPECIALES_LIGHT)

        # Invertir el tema
        self.dark_theme = not self.dark_theme

    def on_button_click(self, value):
        if value == '=':
            try:
                expression = self.entry.get().replace('%', '/100')
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                # Mostrar la operación en la etiqueta, excluyendo el signo '='
                operation = expression + " " + value
                self.operation_label.config(text=operation)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.operation_label.config(text="")
        elif value == 'C':
            self.entry.delete(0, tk.END)
            self.operation_label.config(text="")
        elif value == '<':
            current_text = self.entry.get()
            if current_text:
                new_text = current_text[:-1]  # Eliminar el último carácter
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, new_text)
                # Actualizar la etiqueta de operación
                self.operation_label.config(text=new_text + " ")
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)
            # Actualizar la etiqueta de operación solo cuando se presiona '='
            if value == '=':
                self.operation_label.config(text="")
