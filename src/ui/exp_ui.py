from tkinter import ttk, constants, messagebox
from services.exp_service import exp_service
from tkinter import *
from tkcalendar import *
from dateutil.parser import parse

class ExpView:
    """Tuotteiden käsittelystä vastaava luokka."""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden tuotenäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
        """
        self.root = root
        self.frame = None
        self.lb = None
        self.tree = None
        self.count = 5
        self.add_frame = None
        self.options = None
        self.date = None
        self.cal = None
        self.date_window = None
        self.entry_box = None

        self.initialize()

    def pack(self):
        """Näyttää näkymän."""
        self.frame.pack(fill=constants.X)

    def initialize(self):
        """Alustaa näkymät"""
        self.frame = ttk.Frame(master=self.root)

        self.initialize_treeview()
        self.initialize_entrybox()
        self.initialize_menu()

    def initialize_treeview(self):
        self.tree = ttk.Treeview(self.root)

        self.tree['columns'] = ("ID","Product", "Expiry date")
        self.tree.column("#0", width=120, minwidth=25)
        self.tree.column("ID", anchor=W, width=120)
        self.tree.column("Product", anchor=W, width=120)
        self.tree.column("Expiry date", anchor=W, width=120)

        self.tree.heading("#0", text="Type", anchor=W)
        self.tree.heading("ID", text="ID",anchor=W)
        self.tree.heading("Product", text="Product", anchor=W)
        self.tree.heading("Expiry date", text="Expiry date", anchor=W)

        self.tree.insert(parent='', index='end', iid=0, text="Fridge", values=(1))
        self.tree.insert(parent='', index='end', iid=1, text="Freezer", values=(1))
        self.tree.insert(parent='', index='end', iid=2, text="Pantry", values=(1))
        self.tree.insert(parent='', index='end', iid=3, text="Expired", values=(1))
        self.tree.insert(parent='', index='end', iid=4, text="Used", values=(1))

        self.tree["displaycolumns"]=("Product","Expiry date")
        self.tree.pack(pady=20)

        products = exp_service.get_all_products()
        if products != None:
            for product in products:
                self.tree.insert(parent=product.type, index='end', iid=self.count, text="",
                                 values=(product.id, product.product, product.date))
                self.count += 1

    def initialize_entrybox(self):
        other_frame = Frame(self.root)
        other_frame.pack(pady=10)

        self.add_frame = Frame(self.root)
        self.add_frame.pack(pady=10)

        al = Label(self.add_frame, text="Add Product:",
                   font=("Helvetica", 16), width=30,anchor='c')

        pl = Label(self.add_frame,text="Product:",width=10)
        self.entry_box = Entry(self.add_frame, font="Courier, 10")

        tl = Label(self.add_frame,text="Type:",width=10)
        self.entry_box = Entry(self.add_frame, font="Courier, 10")
        self.options = StringVar(self.add_frame)
        self.options.set("Fridge") # Default option
        types = OptionMenu(self.add_frame, self.options,
                                "Fridge", "Freezer", "Pantry")

        dl = Label(self.add_frame,text="Expiry date:", width=10)
        self.date = Entry(self.add_frame,font="Courier, 10")
        self.date.insert(0,"dd-mm-yyyy")
        self.date.bind("<1>",self.date_picker)
        
        add_button = Button(self.add_frame, text="Add Product", command=self.add_product)
        del_button = Button(other_frame, text="Delete Product", command=self.delete_product)
        exp_button = Button(other_frame, text="Product Expired", command=self.set_expired)
        used_button = Button(other_frame, text="Product Used", command=self.set_used)

        al.grid(row=1,column=0,columnspan=4,pady=10)
        pl.grid(row=2,column=0)
        self.entry_box.grid(row=2,column=1)
        tl.grid(row=2,column=2)
        types.grid(row=2,column=3)
        dl.grid(row=3,column=0)
        self.date.grid(row=3,column=1)
        add_button.grid(row=3,column=2)

        del_button.grid(row=0,column=1)
        exp_button.grid(row=0,column=2,padx=10)
        used_button.grid(row=0,column=3)

    def date_picker(self, event):
        """Popup ikkuna kalenterille"""
        self.date_window = Toplevel(self.add_frame)
        self.date_window.title('Give Expiry Date')
        self.date_window.geometry('235x200')

        self.cal = Calendar(self.date_window, selectmode="day",
                            date_pattern="dd-mm-y")
        self.cal.grid(row=0,column=0)

        cal_button = Button(self.date_window, text="Submit",
                            command=self.give_date)
        cal_button.grid(row=1,column=0)

    def give_date(self):
        self.date.delete(0,END)
        self.date.insert(0,self.cal.get_date())
        self.date_window.destroy()

    def initialize_menu(self):
        """Currently doesn't do anything"""
        menu_ = Menu(self.root)
        self.root.config(menu=menu_)

        file_m = Menu(menu_, tearoff=False)
        menu_.add_cascade(label="File", menu=file_m)

        file_m.add_command(label="Delete All", command=self.delete_all)

    def add_product(self):

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
        else:
            p_type = 2

        p_date = self.date.get()
        try:
            parse(p_date, fuzzy=False)
            p = exp_service.add_product(p_name,p_date,p_type)
            self.tree.insert(parent=p_type, index='end', iid=self.count, text="",
                                    values=(p.id,p.product,p.date))
            self.count += 1

            self.entry_box.delete(0,END)
        except ValueError:
            messagebox.showerror('Entry Error', 'Error: Entered invalid date')
        
        self.date.delete(0,END)
        self.date.insert(0,"dd-mm-yyyy")

    def delete_product(self):
        dp = self.tree.selection()
        for i in dp:
            if int(i) > 4:
                dp_id = self.tree.item(i,'values')[0]
                exp_service.delete_product(dp_id)
                self.tree.delete(i)
        
    def set_expired(self):
        exp = self.tree.selection()
        for i in exp:
            if int(i) > 4:
                exp_id = self.tree.item(i,'values')[0]
                p = exp_service.set_product_expired(exp_id)
                self.tree.delete(i)
                self.tree.insert(parent=3, index='end', iid=i, text="",
                                values=(p.id,p.product,p.date))
            
    def set_used(self):
        up = self.tree.selection()
        for i in up:
            if int(i) > 4:
                up_id = self.tree.item(i,'values')[0]
                p = exp_service.set_product_used(up_id)
                self.tree.delete(i)
                self.tree.insert(parent=4, index='end', iid=i, text="",
                                values=(p.id,p.product,p.date))

    def delete_all(self):
        
        exp_service.delete_all()
        for i in range(5,self.count):
            self.tree.delete(i)
        self.count = 5

