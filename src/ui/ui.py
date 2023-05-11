from tkinter import ttk, constants
from ui.exp_ui import ExpView
from ui.login_ui import LoginView

class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root):
        """Luokan konstruktori, joka luo uuden käyttöliittymästä vastaavan luokan.
        
        Args:
            root: 
                TKinter-elementti, jonka sisään käyttöliittymä alustetaan.
        """
        self.root = root
        self.current_view = None

    def start(self):
        """Aloittaa käyttöliittymän."""

        self.show_login_view()

    def show_login_view(self):
        """Näyttää kirjaitumis näkymän"""

        self.hide_current_view()

        self.current_view = LoginView(self.root, self.show_exp_view)

        self.current_view.pack()
    
    def show_exp_view(self, username):
        """Näyttää pääohjelman näkymän"""

        self.hide_current_view()

        self.current_view = ExpView(self.root, self.show_login_view, username)

        self.current_view.pack()

    def hide_current_view(self):
        if self.current_view != None:
            self.current_view.destroy()

        self.current_view = None