from tkinter import ttk, constants, messagebox
from services.exp_service import exp_service
from string import ascii_letters, digits
from tkinter import *

class LoginView:

    def __init__(self, root, handle_login, handle_create_user):
        self.root = root
        self.frame = None
        self.handle_login = handle_login
        self.handle_create_user = handle_create_user

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

        self.initialize_input()
        self.initialize_buttons()

    def initialize_input(self):

        input_frame = Frame(self.frame)
        input_frame.pack(padx=10,pady=10)

        h_label = ttk.Label(master=input_frame, text="===== Login =====", font=("Helvetica", 14))

        u_label = ttk.Label(master=input_frame, text="Username:")
        self.u_entry = ttk.Entry(master=input_frame)

        p_label = ttk.Label(master=input_frame, text="Password:")
        self.p_entry = ttk.Entry(master=input_frame)

        h_label.grid(row=1,column=0,pady=10)
        u_label.grid(row=2,column=0)
        self.u_entry.grid(row=3,column=0)
        p_label.grid(row=4,column=0)
        self.p_entry.grid(row=5,column=0)
    
    def initialize_buttons(self):

        button_frame = Frame(self.frame)
        button_frame.pack(padx=10,pady=10)

        c_button = ttk.Button(master=button_frame, text = "Create a User", command=self.add_user)
        l_button = ttk.Button(master=button_frame, text="Login",command=self.login)
        
        c_button.grid(row=0,column=0,padx=5)
        l_button.grid(row=0,column=1,padx=5)


    def login(self):
        username = self.u_entry.get()
        password = self.p_entry.get()
        if len(username) == 0 or len(password) == 0:
            messagebox.showerror('Entry Error', 'Error: Missing username and/or password')
            return
        
        response = exp_service.login(username,password)
        
        if response == 0:
            messagebox.showerror('User Error', 'Error: User does not exists')
            return
        elif response == 1:
            messagebox.showerror('User Error', 'Error: Invalid password')
            return
        elif response == 2:
            messagebox.showinfo('!User!', "Your old products couldn't be found: Created a new folder ")
        
        self.u_entry.delete(0,END)
        self.p_entry.delete(0,END)

        self.handle_login(username)

    def add_user(self):

        self.handle_create_user()