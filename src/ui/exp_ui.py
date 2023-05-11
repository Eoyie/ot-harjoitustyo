from tkinter import ttk, constants, messagebox
from services.exp_service import exp_service
from tkinter import *
from tkcalendar import *
from datetime import datetime

class ExpView:
    """Tuotteiden käsittelystä vastaava luokka."""

    def __init__(self, root, handle_logout, user):
        """Luokan konstruktori. Luo uuden tuotenäkymän.

        Args:
            root: 
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_logout: 
                Kutsuttava-arvo, jota kutsutaan kun käyttäjä kirjautuu pois.
        """
        self.root = root
        self.frame = None
        self.handle_logout = handle_logout
        self.user = user

        self.lb = None
        self.tree = None
        self.count = 5

        self.add_frame = None
        self.options = None
        self.date_entry = None
        self.cal = None
        self.date_window = None
        self.entry_box = None

        self.update_file_path(self.user)
        self.initialize()

    def destroy(self):
        """"Tuhoaa näkymän."""
        self.frame.destroy()

    def pack(self):
        """Näyttää näkymän."""
        self.frame.pack(fill=constants.X)

    def update_file_path(self, username):
         
         exp_service.update_file_path(username)

    def initialize(self):
        """Alustaa näkymät"""
        self.frame = ttk.Frame(master=self.root)
        exp_service.set_user(self.user)

        self.initialize_treeview()
        self.initialize_buttons()
        self.initialize_entrybox()
        self.initialize_menu()

    def initialize_treeview(self):
        self.tree = ttk.Treeview(self.frame)

        self.tree['columns'] = ("ID","Product","Qty","Expiry date")
        self.tree.column("#0", width=120, minwidth=25)
        self.tree.column("ID", anchor=W, width=120)
        self.tree.column("Product", anchor=W, width=120)
        self.tree.column("Qty", anchor=W, width=50)
        self.tree.column("Expiry date", anchor=W, width=120)

        self.tree.heading("#0", text="Type", anchor=W)
        self.tree.heading("ID", text="ID",anchor=W)
        self.tree.heading("Product", text="Product", anchor=W)
        self.tree.heading("Qty", text="Qty", anchor=W)
        self.tree.heading("Expiry date", text="Expiry date", anchor=W)

        self.tree.insert(parent='', index='end', iid=0, text="Fridge", values=(1))
        self.tree.insert(parent='', index='end', iid=1, text="Freezer", values=(1))
        self.tree.insert(parent='', index='end', iid=2, text="Pantry", values=(1))
        self.tree.insert(parent='', index='end', iid=3, text="Expired", values=(1))
        self.tree.insert(parent='', index='end', iid=4, text="Used", values=(1))

        self.tree["displaycolumns"]=("Product","Qty","Expiry date")
        self.tree.pack(pady=20,padx=20)

        exp_service.automatic_expire()

        products = exp_service.get_all_products()
        if products != None:
            for product in products:
                self.tree.insert(parent=product.type, index='end', iid=self.count, text="",
                                 values=(product.id, product.product,"1234", product.date))
                self.count += 1

    def initialize_buttons(self):
        other_frame = Frame(self.frame)
        other_frame.pack(pady=10)

        del_button = Button(other_frame, text="Delete Product", command=self.delete_product)
        exp_button = Button(other_frame, text="Product Expired", command=self.set_expired)
        used_button = Button(other_frame, text="Product Used", command=self.set_used)

        del_button.grid(row=0,column=1)
        exp_button.grid(row=0,column=2,padx=10)
        used_button.grid(row=0,column=3)


    def initialize_entrybox(self):
        self.add_frame = Frame(self.frame)
        self.add_frame.pack(pady=10)

        al = Label(self.add_frame, text="Add Product:",
                   font=("Helvetica", 16), width=30,anchor='c')

        pl = Label(self.add_frame,text="Product:",width=10)
        self.entry_box = Entry(self.add_frame, font="Courier, 10")

        tl = Label(self.add_frame,text="Type:",width=10)
        self.entry_box = Entry(self.add_frame, font="Courier, 10")
        self.options = StringVar(self.add_frame)
        self.options.set("Fridge")
        types = OptionMenu(self.add_frame, self.options,
                                "Fridge", "Freezer", "Pantry")

        dl = Label(self.add_frame,text="Expiry date:", width=10)
        self.date_entry = DateEntry(self.add_frame,selectmode="day",
                            date_pattern="dd-mm-y")
        
        ql = Label(self.add_frame,text="Quantity:",width=10)
        self.quantity_box = Entry(self.add_frame,font="Courier, 10", width=5)
        self.quantity_box.insert(0, 1)
        
        add_button = Button(self.add_frame, text="Add Product", command=self.add_product)

        al.grid(row=1,column=0,columnspan=4,pady=10)
        pl.grid(row=2,column=0)
        self.entry_box.grid(row=2,column=1)
        tl.grid(row=2,column=2)
        types.grid(row=2,column=3)
        dl.grid(row=3,column=0)
        self.date_entry.grid(row=3,column=1)
        ql.grid(row=3,column=2)
        self.quantity_box.grid(row=3,column=3)
        add_button.grid(row=4,column=0,columnspan=4,pady=10)

    def initialize_menu(self):
        menu_ = Menu(self.frame)
        self.root.config(menu=menu_)

        u_menu = Menu(menu_, tearoff=False)
        e_menu = Menu(menu_, tearoff=False)

        menu_.add_cascade(label="User settings", menu=u_menu)
        menu_.add_cascade(label="Extra commands", menu=e_menu)

        u_menu.add_command(label="Logout", command=self.logout)

        e_menu.add_command(label="Delete All", command=self.delete_all)
        e_menu.add_command(label="Calendar View", command=self.see_cal_view)


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

        p_qty = self.quantity_box.get()
        if p_qty is None:
            messagebox.showerror('Entry Error', 'Error: Not entered quantity')
            return
        elif p_qty.isnumeric():
            if len(p_name) > 1000:
                messagebox.showerror('Entry Error', 'Error: Entered quantity is too big')
                return
        else: 
            messagebox.showerror('Entry Error', 'Error: Invalid quantity')
            return

        p_date = self.date_entry.get_date()
        p_date = p_date.strftime('%d-%m-%Y')
        today = datetime.today().strftime('%d-%m-%Y')
        if p_date < today:
            answer = messagebox.askquestion("Confirm","Already Expired: Do you still want to add the product?")
            if answer == "no":
                return
            p_type = 3
        p = exp_service.add_product(p_name,p_date,p_qty,p_type)
        self.tree.insert(parent=p_type, index='end', iid=self.count,
                         text="", values=(p.id,p.product,p.qty,p.date))
        self.count += 1

        self.entry_box.delete(0,END)

        self.update()

    def delete_product(self):
        dp = self.tree.selection()
        for i in dp:
            if int(i) > 4:
                dp_id = self.tree.item(i,'values')[0]
                exp_service.delete_product(dp_id)
        
        self.update()
        
    def set_expired(self):
        exp = self.tree.selection()
        for i in exp:
            if int(i) > 4:
                exp_id = self.tree.item(i,'values')[0]
                exp_service.set_product_expired(exp_id)
        
        self.update()

    def set_used(self):
        up = self.tree.selection()
        for i in up:
            if int(i) > 4:
                up_id = self.tree.item(i,'values')[0]
                exp_service.set_product_used(up_id)

        self.update()

    def delete_all(self):
        
        answer = messagebox.askquestion("Confirm","Are you sure you want to delete all products")
        if answer == "no":
            return
        
        exp_service.delete_all()
        for i in range(5,self.count):
            self.tree.delete(i)
        self.count = 5

    def update(self):

        for i in range(5,self.count):
            self.tree.delete(i)
        self.count = 5
    
        products = exp_service.get_all_products()
        if products != None:
            for product in products:
                self.tree.insert(parent=product.type, index='end', iid=self.count, text="",
                                 values=(product.id, product.product, product.qty,product.date))
                self.count += 1
    
    def see_cal_view(self):

        cal_v = Toplevel(self.frame)
        cal_v.title("Expire Calendar")
        cal_v.geometry('500x320')
        cal = Calendar(cal_v, selectmode='none')

        today = datetime.today()
        products = exp_service.get_all_products()
        for product in products:
            p_date = datetime.strptime(product.date, "%d-%m-%Y")
            if product.type == "3":
                if p_date > today:
                    p = cal.calevent_create(p_date, product.product, 'E_Expired')
                    cal.calevent_lower(p)
                else:
                    cal.calevent_create(p_date, product.product, 'N_Expired')
            elif product.type == "4":
                p = cal.calevent_create(p_date, product.product, 'Used')
                cal.calevent_lower(p)
            else:
                p = cal.calevent_create(p_date, product.product, 'Ok')
                cal.calevent_raise(p)

        cal.tag_config('E_Expired', background='orange', foreground='yellow')
        cal.tag_config('N_Expired', background='red', foreground='yellow')
        cal.tag_config('Used', background='green', foreground='yellow')

        cal.pack(fill="both", expand=True)

    def logout(self):

        self.handle_logout()