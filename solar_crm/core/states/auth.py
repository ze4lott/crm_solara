import reflex as rx

class AuthState(rx.State):
    user: str = ""
    password: str = ""
    is_authenticated: bool = False
    error: str = ""
    show_password: bool = False

    def set_user(self, value: str): self.user = value
    def set_password(self, value: str): self.password = value
    def toggle_password(self): self.show_password = not self.show_password

    def login(self):
        if not self.user.strip() or not self.password:
            self.error = "Ingresa usuario y contraseña para continuar."
            return
        self.is_authenticated = True
        self.error = ""
        self.password = ""
        return rx.redirect("/dashboard")

    def require_auth(self):
        if not self.is_authenticated:
            return rx.redirect("/login")

    def logout(self):
        self.user = ""
        self.password = ""
        self.is_authenticated = False
        self.error = ""
        return rx.redirect("/login")
