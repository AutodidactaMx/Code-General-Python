import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import util.util_ventana as util_ventana

COLOR_FONDO = "#dee6f1"


class FormularioRegistroDesign(tk.Tk):

    def __init__(self):
        super().__init__()
        self.config_window()
        self.crear_paneles()
        self.crear_controles()

    def config_window(self):
        self.title('Python CRUD')
        w, h = 800, 500
        util_ventana.centrar_ventana(self, w, h)
        self.configure(bg=COLOR_FONDO)

    def obtener_conf_btn_pack(self):
        return {"side": tk.RIGHT, "padx": 10, "pady": 10}

    def crear_paneles(self):
        self.marco_titulo = tk.Frame(
            self, bg=COLOR_FONDO, height=50)
        self.marco_titulo.pack(side=tk.TOP, fill='both')

        self.marco_registro = tk.Frame(
            self, bg=COLOR_FONDO, height=50)
        self.marco_registro.pack(side=tk.TOP, fill='both')

        self.marco_acciones = tk.Frame(
            self, bg=COLOR_FONDO, height=50)
        self.marco_acciones.pack(side=tk.TOP,  padx=20, fill='both')

        self.marco_productos = tk.Frame(
            self, bg=COLOR_FONDO)
        self.marco_productos.pack(
            side=tk.TOP, fill='both', padx=20, pady=15, expand=True)

    def crear_controles(self):

        title = tk.Label(self.marco_titulo, text="REGISTRO DE PRODUCTO", font=(
            'Roboto', 20), fg="#000000", bg=COLOR_FONDO, pady=20)
        title.pack(expand=True, fill=tk.BOTH)

        etiqueta_id = tk.Label(self.marco_registro, text="Id:", font=(
            'Times', 14), fg="#666a88", bg=COLOR_FONDO, width=5)
        etiqueta_id.pack(side="left", padx=5, pady=10)

        self.campo_id = ttk.Entry(self.marco_registro, font=(
            'Times', 14), state="readonly", width=5)
        self.campo_id.pack(side="left", padx=5, pady=10)

        etiqueta_nombre = tk.Label(self.marco_registro, text="Producto:", font=(
            'Times', 14), fg="#666a88", bg=COLOR_FONDO)
        etiqueta_nombre.pack(side="left", padx=5, pady=10)
        self.campo_nombre = ttk.Entry(self.marco_registro, font=('Times', 14))
        self.campo_nombre.pack(side="left", padx=5, pady=10)

        etiqueta_precio = tk.Label(self.marco_registro, text="Precio:", font=(
            'Times', 14), fg="#666a88", bg=COLOR_FONDO)
        etiqueta_precio.pack(side="left", padx=5, pady=10)
        self.campo_precio = ttk.Entry(self.marco_registro, font=('Times', 14))
        self.campo_precio.pack(side="left", padx=5, pady=10)

        self.btn_registro = tk.Button(self.marco_acciones, text="Registrar", font=(
            'Times', 13), bg='#51aded', bd=0, fg="#fff", padx=15, command=self.registrar_producto)
        self.btn_registro.pack(**self.obtener_conf_btn_pack())
        self.btn_registro.bind(
            "<Return>", (lambda event: self.registrar_producto()))

        self.btn_eliminar = tk.Button(self.marco_acciones, text="Eliminar", font=(
            'Times', 13), bg='#ed5153', bd=0, fg="#fff", padx=15, command=self.eliminar_producto)
        self.btn_eliminar.pack(**self.obtener_conf_btn_pack())
        self.btn_eliminar.bind(
            "<Return>", (lambda event: self.eliminar_producto()))
        self.btn_eliminar.pack_forget()

        self.btn_modificar = tk.Button(self.marco_acciones, text="Modificar", font=(
            'Times', 13), bg='#536270', bd=0, padx=15, fg="#fff", command=self.modificar_producto)
        self.btn_modificar.pack(**self.obtener_conf_btn_pack())
        self.btn_modificar.bind(
            "<Return>", (lambda event: self.modificar_producto()))
        self.btn_modificar.pack_forget()

        self.btn_limpiar_campos = tk.Button(self.marco_acciones, text="Limpiar Campos", font=(
            'Times', 13), bg='#e39531', bd=0, padx=15, fg="#fff", command=self.limpiar_campos)
        self.btn_limpiar_campos.pack(**self.obtener_conf_btn_pack())
        self.btn_limpiar_campos.bind(
            "<Return>", (lambda event: self.limpiar_campos()))

        # Table        

        style = ttk.Style(self) 
        style.theme_use("clam") # set theam to clam
        style.configure("Treeview", background="#eafbea", 
                foreground="#000")
        style.configure('Treeview.Heading', background="#6f9a8d", foreground="#fff")
        
        tree_scroll =  ttk.Scrollbar(self.marco_productos)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(self.marco_productos,
                                 show='headings', yscrollcommand=tree_scroll.set)
        self.tree['columns'] = ('Id', 'Nombre', 'Precio')
        self.tree.column('#0')
        self.tree.column('Id')
        self.tree.column('Nombre')
        self.tree.column('Precio')

        self.tree.heading('#0', text='')
        self.tree.heading('Id', text='Id')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Precio', text='Precio')
        self.tree.pack(expand=True, fill='both')
        self.tree.bind("<<TreeviewSelect>>", self.al_seleccionar_treeview)
        
        self.tree.tag_configure('oddrow', background='#ffffe0')
        self.tree.tag_configure('evenrow', background='#eafbea')                        

        self.actualizar_lista()

    def al_seleccionar_treeview(self, event):
        pass

    def registrar_producto(self):
        pass

    def actualizar_lista(self):
        pass

    def eliminar_producto(self):
        pass

    def modificar_producto(self):
        pass

    def limpiar_campos(self):
        try:
            self.campo_nombre.delete(0, 'end')
            self.campo_precio.delete(0, 'end')
            self.campo_id.config(state="normal")
            self.campo_id.delete(0, 'end')
            self.campo_id.config(state="readonly")
            self.btn_registro.pack(**self.obtener_conf_btn_pack())
            self.btn_eliminar.pack_forget()
            self.btn_modificar.pack_forget()
        except Exception as e:
            messagebox.showerror("Error", f" Error en la limpieza: {e}")
