from tkinter import ttk, constants, messagebox
from string import ascii_letters, digits
from services.exp_service import exp_service
from tkinter import *

class LoginView:

    def __init__(self, root, handle_login, handle_create_user):
        self.root = root
        self.frame = None
        self.handle_login = handle_login
        self.handle_create_user = handle_create_user

        self.allowed_characters = ascii_letters + digits 
        self.count = 0

        self.initialize()

    def destroy(self):
        """"Tuhoaa näkymän."""
        self.frame.destroy()

    def pack(self):
        """Näyttää näkymän."""
        self.frame.pack(fill=constants.X)

    def initialize(self):

        self.frame = ttk.Frame(master=self.root)

        self.initialize_treeview()
        self.initialize_input()
        self.initialize_buttons()

    def initialize_treeview(self):
        self.tree = ttk.Treeview(self.frame)

        self.tree['columns'] = ("User")
        self.tree.column("#0", width=1, minwidth=1)
        self.tree.column("User", anchor=W, width=120)

        self.tree.heading("#0", text="-", anchor=W)
        self.tree.heading("User", text="User",anchor=W)

        self.tree["displaycolumns"]=("User")
        self.tree.pack(pady=20,padx=20)

        user_list = exp_service.get_all_users()
        if user_list != None:
            for user in user_list:
                if user != "test":
                    self.tree.insert(parent='', index='end', iid=self.count, text="",
                                    values=(user))
                    self.count += 1

    def initialize_input(self):

        input_frame = Frame(self.frame)
        input_frame.pack(padx=10,pady=10)

        h_label = ttk.Label(master=input_frame, text="===== Pick User =====", font=("Helvetica", 14))

        h_label.grid(row=1,column=0,pady=5)
    
    def initialize_buttons(self):

        button_frame = Frame(self.frame)
        button_frame.pack(padx=10,pady=10)

        c_button = ttk.Button(master=button_frame, text = "Create a User", command=self.add_user)
        d_button = ttk.Button(master=button_frame, text="Delete User",command=self.delete)
        l_button = ttk.Button(master=button_frame, text="Login",command=self.login)
        
        c_button.grid(row=0,column=0,)
        d_button.grid(row=0,column=1,padx=5)
        l_button.grid(row=0,column=2,)


    def login(self):
        username = self.tree.selection()
        username = self.tree.item(0,'values')[0]

        self.handle_login(username)

    def add_user(self):

        self.handle_create_user()

    def delete(self):
        answer = messagebox.askquestion("Confirm","Are you sure you want to delete user")
        if answer == "no":
            return
        user = self.tree.selection()
        username = self.tree.item(0,'values')[0]
        self.tree.delete(user)

        exp_service.delete_user(username)