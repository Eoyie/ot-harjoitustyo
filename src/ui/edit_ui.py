from tkinter import ttk, constants, messagebox
from services.exp_service import exp_service
from tkinter import *
from tkcalendar import *
from datetime import datetime

class EditView:

    def __init__(self, root, handle_return, user, p_id):

        self.root = root
        self.frame = None
        self.handle_return = handle_return

        self.user = user
        self.p_id = p_id
        self.product = None

        self.update_file_path(self.user)
        self.bring_product(self.p_id)
        self.initialize()

    def destroy(self):
        """"Tuhoaa näkymän."""
        self.frame.destroy()

    def pack(self):
        """Näyttää näkymän."""
        self.frame.pack(fill=constants.X)

    def update_file_path(self, username):
         '''Päivittää repositorille oikean reitin'''
         exp_service.update_file_path(username)

    def bring_product(self, p_id):

        self.product = exp_service.get_one_product(p_id)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.initialize_entrybox()
        self.initialize_buttons()

    def initialize_entrybox(self):

        self.add_frame = Frame(self.frame)
        self.add_frame.pack(padx=10)

        al = Label(self.add_frame, text="Edit Product:",
                   font=("Helvetica", 16), width=30,anchor='c')

        pl = Label(self.add_frame,text="Product:",width=10)
        self.entry_box = Entry(self.add_frame, font="Courier, 10")
        self.entry_box.insert(0,self.product.product)

        tl = Label(self.add_frame,text="Type:",width=10)
        self.options = StringVar(self.add_frame)

        if self.product.type == "0": type_str = "Fridge"
        elif self.product.type == "1": type_str = "Freezer"
        elif self.product.type == "2": type_str = "Pantry"
        elif self.product.type == "3": type_str = "Expired"
        else: type_str = "Used"

        self.options.set(type_str)
        types = OptionMenu(self.add_frame, self.options,
                                "Fridge", "Freezer", "Pantry", "Expired", "Used")

        dl = Label(self.add_frame,text="Expiry date:", width=10)
        self.date_entry = DateEntry(self.add_frame,selectmode="day",
                            date_pattern="dd-mm-y")
        self.date_entry.set_date(self.product.date)
        
        ql = Label(self.add_frame,text="Quantity:",width=10)
        self.quantity_box = Entry(self.add_frame,font="Courier, 10", width=5)
        self.quantity_box.insert(0, self.product.qty)
        
        al.grid(row=1,column=0,columnspan=4,pady=10)
        pl.grid(row=2,column=0)
        self.entry_box.grid(row=2,column=1)
        tl.grid(row=2,column=2)
        types.grid(row=2,column=3)
        dl.grid(row=3,column=0)
        self.date_entry.grid(row=3,column=1)
        ql.grid(row=3,column=2)
        self.quantity_box.grid(row=3,column=3)

    def initialize_buttons(self):

        self.button_frame = Frame(self.frame)
        self.button_frame.pack(pady=10)

        save_button = Button(self.button_frame, text="Save Changes", command=self.save_changes)
        cancel_button = Button(self.button_frame, text="Cancel Changes", command=self.cancel_changes)

        save_button.grid(row=0,column=0,padx=10)
        cancel_button.grid(row=0,column=1)

    def save_changes(self):

        p_name = self.entry_box.get()

        if p_name is None:
            messagebox.showerror('Entry Error', 'Error: Not entered product')
            return
        elif len(p_name) < 3:
            messagebox.showerror('Entry Error', 'Error: Product name length at least 3 characters')
            return
        elif len(p_name) > 14:
            messagebox.showerror('Entry Error', 'Error: Product name is too long')
            return
        
        p_type = self.options.get()
        if p_type == "Fridge":
            p_type = 0
        elif p_type == "Freezer":
            p_type = 1
        elif p_type == "Pantry":
            p_type = 2
        elif p_type == "Expired":
            p_type = 3
        else:
            p_type = 4

        p_qty = self.quantity_box.get()
        if p_qty is None:
            messagebox.showerror('Entry Error', 'Error: Not entered quantity')
            return
        elif p_qty.isnumeric():
            if len(p_qty) > 1000:
                messagebox.showerror('Entry Error', 'Error: Entered quantity is too big')
                return
            elif len(p_qty) < 1:
                messagebox.showerror('Entry Error', 'Error: Entered quantity is 0 or negative')
                return
        else: 
            messagebox.showerror('Entry Error', 'Error: Invalid quantity')
            return

        p_date = self.date_entry.get_date()
        p_date = p_date.strftime('%d-%m-%Y')
        today = datetime.today().strftime('%d-%m-%Y')
        if p_date < today and p_type < 3:
            answer = messagebox.askquestion("Confirm","Already Expired: Do you still want to add the product? (Type will be changed to 'Expired')")
            if answer == "no":
                return
            p_type = 3

        exp_service.update_one(p_name, p_date, p_qty, p_type ,self.p_id)

        self.entry_box.delete(0,END)

        self.handle_return(self.user)

    def cancel_changes(self):
        self.handle_return(self.user)