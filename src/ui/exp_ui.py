from tkinter import ttk, constants
from services.exp_service import exp_service
from tkinter import *

class ExpView:              
    def __init__(self, root):
        self.root = root
        self.frame = None
        self.lb = None
        self.entry_box = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.initialize_listbox()
        self.initialize_entrybox()
        self.initialize_menu()

    def initialize_listbox(self):

        lb_frame = Frame(self.root)
        lb_frame.pack(pady=10)

        self.lb = Listbox(
            lb_frame,
            font=("Carier",10),
            width=20,
            height=20,
            bg="#F0F0F0",
            bd=3,
            fg="#464646",
            highlightthickness=0,
            selectbackground="#a6a6a6",
            activestyle="none"
            )
        lb_scrollbar = Scrollbar(lb_frame)
        
        self.lb.pack(side=LEFT,fill=BOTH)
        lb_scrollbar.pack(side=RIGHT,fill=BOTH)

        self.lb.config(yscrollcommand=lb_scrollbar.set)
        lb_scrollbar.config(command=self.lb.yview)
        
        products = exp_service.get_ok_products()
        if products != None:
            for product in products:
                self.lb.insert(END,product[0])
    
    def initialize_entrybox(self):
        self.entry_box = Entry(self.root, font="Courier, 14")
        self.entry_box.pack(pady=20)

        e_button_frame = Frame(self.root)
        e_button_frame.pack(pady=10)

        add_button = Button(e_button_frame, text="Add Product", command=self.add_product)
        del_button = Button(e_button_frame, text="Delete Product", command=self.delete_product)
        exp_button = Button(e_button_frame, text="Product Expired", command=self.set_product_expired)

        add_button.grid(row=0,column=0)
        del_button.grid(row=0,column=1, padx=20)
        exp_button.grid(row=0,column=2)

    def initialize_menu(self):
        menu_ = Menu(self.root)
        self.root.config(menu=menu_)

        file_m = Menu(menu_, tearoff=False)
        menu_.add_cascade(label="File", menu=file_m)

        file_m.add_command(label="Save List", command=self.save_list)

    def add_product(self):
        p_name = self.entry_box.get()
        self.lb.insert(END,p_name)
        exp_service.add_product(p_name)
        self.entry_box.delete(0,END)

    def delete_product(self):
        for item in self.lb.curselection():
            product_num = item
        exp_service.delete_product(product_num)
        self.lb.delete(ANCHOR)

    def set_product_expired(self):
        pass

    def save_list(self):
        pass
