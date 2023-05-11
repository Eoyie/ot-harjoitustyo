from tkinter import ttk, constants, messagebox
from services.exp_service import exp_service
from string import ascii_letters, digits
from tkinter import *

class LoginView:

    def __init__(self, root, handle_login):
        self.root = root
        self.frame = None
        self.handle_login = handle_login

        self.u_entry = None
        self.p_entry = None
        self.allowed_characters = ascii_letters + digits

        self.initialize()

    def destroy(self):
        """"Tuhoaa näkymän."""
        self.frame.destroy()

    def pack(self):
        """Näyttää näkymän."""
        self.frame.pack(fill=constants.X)

    def initialize(self):

        self.frame = ttk.Frame(master=self.root)

        a = ttk.Button(master=self.frame, text = "Create a User", command=self.add_user)
        h_label = ttk.Label(master=self.frame, text="Login")

        u_label = ttk.Label(master=self.frame, text="Username")
        self.u_entry = ttk.Entry(master=self.frame)

        p_label = ttk.Label(master=self.frame, text="Password")
        self.p_entry = ttk.Entry(master=self.frame)

        button = ttk.Button(master=self.frame, text="Login",command=self.login)
        b = ttk.Label(master=self.frame, text="Tää ei vielä tee mitään, koska en osaa yhdistää koodiin ^^")
        c = ttk.Label(master=self.frame, text="(Ja en ole aloittanut käyttäjä osuutta)")

        a.grid(row=0,column=0)
        h_label.grid(row=1,column=0)
        u_label.grid(row=2,column=0)
        self.u_entry.grid(row=3,column=0)
        p_label.grid(row=4,column=0)
        self.p_entry.grid(row=5,column=0)
        button.grid(row=6,column=0)
        b.grid(row=7,column=0)
        c.grid(row=8,column=0)

    def username_error_checker(self, username):

        if username == "data":
            messagebox.showerror('User Error', 'Error: Invalid username')
            return False
        elif len(username) < 3:
            messagebox.showerror('User Error', 'Error: Username too short: min 3 characters')
            return False
        elif len(username) > 20:
            messagebox.showerror('User Error', 'Error: Username too long: max 20 characters')
            return False
        elif set(username).difference(self.allowed_characters):
            messagebox.showerror('User Error', 'Error: Username contains special letters')
            return False
        
        return True

    def login(self):
        username = self.u_entry.get()
        self.u_entry.delete(0,END)
        
        if self.username_error_checker(username) == False:
            return
            
        response = exp_service.login(username)
        if response == False:
            messagebox.showerror('User Error', 'Error: User does not exists')
            return
        
        self.handle_login(username)

    def add_user(self):
        username = self.u_entry.get()
        self.u_entry.delete(0,END)

        response = exp_service.ensure_user_folder_exists(username)
        if response == True:
            messagebox.showerror('User Error', 'Error: Username is already taken')
            return

        if self.username_error_checker(username) == False:
            return

        exp_service.make_user_folder(username)