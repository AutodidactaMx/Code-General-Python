from tkinter import messagebox
from aplicacion.servicio_producto import ServicioProducto
from form.registro_from_design import FormularioRegistroDesign


class FormularioRegistro(FormularioRegistroDesign):

    def __init__(self):
        self.servicio_producto = ServicioProducto()
        super().__init__()

    def al_seleccionar_treeview(self, event):
        seleccion = event.widget.selection()
        if seleccion:
            item = event.widget.item(seleccion[0], 'values')
            if item:
                self.limpiar_campos()
                self.campo_id.config(state="normal")
                self.campo_id.insert(0, item[0])
                self.campo_id.config(state="readonly")
                self.campo_nombre.insert(0, item[1])
                self.campo_precio.insert(0, item[2])                   
                self.btn_eliminar.pack(**self.obtener_conf_btn_pack())
                self.btn_modificar.pack(**self.obtener_conf_btn_pack())
                self.btn_registro.pack_forget()

    def registrar_producto(self):
        nombre = self.campo_nombre.get()
        precio = self.campo_precio.get()

        if not nombre or not precio:
            messagebox.showerror(
                "Error", "Por favor ingrese el nombre y el precio del producto.")

        try:
            precio = float(precio)
        except ValueError:
            messagebox.showerror(
                "Error", "El precio debe ser un número válido.")

        try:
            self.servicio_producto.register(nombre, precio)
            messagebox.showinfo("Éxito", "Producto registrado exitosamente.")
            self.actualizar_lista()
        except Exception as e:
            messagebox.showerror(
                "Error", f"No se pudo registrar_producto el producto: {e}")
        finally:
            self.limpiar_campos()

    def actualizar_lista(self):
        registros = self.tree.get_children()
        for registro in registros:
            self.tree.delete(registro)
        productos = self.servicio_producto.obtener_productos()
        for ref, producto in enumerate(productos):                  
            color = ('evenrow',) if ref % 2 else ('oddrow',)    
            self.tree.insert(parent='', index=ref, iid=ref, text='', tags = color, values=(
                producto.id, producto.nombre, producto.precio))

    def eliminar_producto(self):
        try:
            id = self.tree.item(self.tree.selection())["values"][0]
            self.servicio_producto.eliminar(id)
            self.actualizar_lista()
        except IndexError as e:
            messagebox.showerror(
                "Error", f"Por favor selecciona una fila: {e}")

    def modificar_producto(self):
        try:
            id = self.tree.item(self.tree.selection())["values"][0]
            nombre = self.campo_nombre.get()
            precio = self.campo_precio.get()
            self.servicio_producto.modificar(nombre, precio, id)
            self.limpiar_campos()
            self.actualizar_lista()
        except IndexError as e:
            messagebox.showerror(
                "Error", f"Por favor selecciona una fila: {e}")
