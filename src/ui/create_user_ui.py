from tkinter import ttk, StringVar, constants, messagebox
from services.exp_service import exp_service
from string import ascii_letters, digits
from tkinter import *


class CreateUserView:
    """Käyttäjän rekisteröitymisestä vastaava näkymä."""

    def __init__(self, root, handle_login_view):
        """Luokan konstruktori. Luo uuden rekisteröitymisnäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_login_view:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään kirjautumisnäkymään.
        """
        self._root = root
        self._handle_login_view = handle_login_view
        self._frame = None
        self.allowed_characters = ascii_letters + digits

        self.initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def initialize(self):

        self._frame = ttk.Frame(master=self._root)

        self.initialize_input()
        self.initialize_buttons()

    def initialize_input(self):

        input_frame = Frame(self._frame)
        input_frame.pack(padx=10,pady=10)

        h_label = ttk.Label(master=input_frame, text="== Create a user ==", font=("Helvetica", 14))

        u_label = ttk.Label(master=input_frame, text="Username:")
        self.u_entry = ttk.Entry(master=input_frame)

        h_label.grid(row=1,column=0,pady=10)
        u_label.grid(row=2,column=0)
        self.u_entry.grid(row=3,column=0)

    def initialize_buttons(self):

        button_frame = Frame(self._frame)
        button_frame.pack(padx=10,pady=10)

        c_button = ttk.Button(master=button_frame, text = "Create a User", command=self.add_user)
        l_button = ttk.Button(master=button_frame, text="Cancel",command=self.cancel)
        
        c_button.grid(row=0,column=0,padx=5)
        l_button.grid(row=0,column=1,padx=5)

    def add_user(self):

        username = self.u_entry.get() 
        self.u_entry.delete(0,END)

        if len(username) == 0 :
            messagebox.showerror('Entry Error', 'Error: Missing username')
            self.u_entry.delete(0,END)
            return
        
        if username == "data" or username == "test":
            messagebox.showerror('User Error', 'Error: Invalid username')
            return
        elif len(username) < 3:
            messagebox.showerror('User Error', 'Error: Username too short: min 3 characters')
            return
        elif len(username) > 20:
            messagebox.showerror('User Error', 'Error: Username too long: max 20 characters')
            return
        elif set(username).difference(self.allowed_characters):
            messagebox.showerror('User Error', 'Error: Username contains special letters')
            return 
        
        response = exp_service.create_user(username)
        
        if response is False:
            messagebox.showerror('User Error', 'Error: User already exists')
            return 
        
        self._handle_login_view()

    def cancel(self):

        self._handle_login_view()