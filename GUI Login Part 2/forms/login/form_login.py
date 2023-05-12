from tkinter import messagebox
from forms.master.form_master import MasterPanel
from persistence.repository.auth_user_repository import AuthUserRepositroy
import util.encoding_decoding as end_dec
from persistence.model import Auth_User
from forms.login.form_login_designer import FormLoginDesigner
from forms.registration.form import FormRegister


class FormLogin(FormLoginDesigner):

    def __init__(self):
        self.auth_repository = AuthUserRepositroy()
        super().__init__()

    def verificar(self):
        user_db: Auth_User = self.auth_repository.getUserByUserName(
            self.usuario.get())
        if(self.isUser(user_db)):
            self.isPassword(self.password.get(), user_db)

    def userRegister(self):
        FormRegister().mainloop()

    def isUser(self, user: Auth_User):
        status: bool = True
        if(user == None):
            status = False
            messagebox.showerror(
                message="El usuario no existe por favor registrese", title="Mensaje",parent=self)
            messagebox.showinfo("title", "message",parent=self)   
        return status

    def isPassword(self, password: str, user: Auth_User):
        b_password = end_dec.decrypt(user.password)
        if(password == b_password):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(
                message="La contraseña no es correcta", title="Mensaje")
