from tkinter import ttk, constants
from ui.exp_ui import ExpView

class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def start(self):

        #self.show_exp_view()
        self.show_test_view()

    '''def show_exp_view(self):
        self.hide_current_view()

        a = ttk.Label(master=self.root, text = "Heipä hei, tämä on testi :)")
        heading_label = ttk.Label(master=self.root, text="Login")

        username_label = ttk.Label(master=self.root, text="Username")
        username_entry = ttk.Entry(master=self.root)

        password_label = ttk.Label(master=self.root, text="Password")
        password_entry = ttk.Entry(master=self.root)

        button = ttk.Button(master=self.root, text="Click Click")
        b = ttk.Label(master=self.root, text="Tää ei vielä tee mitään, koska en osaa yhdistää koodiin ^^")
        c = ttk.Label(master=self.root, text="(Ja en ole aloittanut käyttäjä osuutta)")
        a.pack()
        heading_label.pack()
        username_entry.pack()
        username_label.pack()
        password_entry.pack()
        password_label.pack()
        button.pack()
        b.pack()
        c.pack()
        #self.current_view = ExpView(self.root, self.show_exp_view)

        #self.current_view.pack() '''
    
    def show_test_view(self):
        self.hide_current_view()

        self.current_view = ExpView(self.root)

        self.current_view.pack()

    def hide_current_view(self):

        #if self.current_view != None:
        #    self.current_view.destroy()

        self.current_view = None