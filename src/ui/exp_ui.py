from tkinter import ttk, constants
from services.exp_service import exp_service

class ExpView:
    def __init__(self, root):         #Hyvin vaiheessa
        self.root = root
        self.frame = None
        self.create_product_entry = None
        self.product_type = None
        self.product_date = None
        self.exp_list_frame = None
        self.exp_list_view = None
        
        self.initialize()

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def initialize(self):

        self.frame = ttk.Frame(master=self.root)
        self.exp_list_frame = ttk.Frame(master=self.frame)

        self.initialize_header()
        self.initialize_product_list()
        self.initialize_footer()

        self.exp_list_frame.grid(
            row = 1,
            column = 0,
            columnspan = 2,
            sticky = constants.EW
        )

        self.frame.grid_columnconfigure(0, weight=1, minsize=400)
        self.frame.grid_columnconfigure(1, weight=0)
   
    def initialize_header(self):
        nothing_label = ttk.Label(
            master = self.frame,
            text = "There is nothing important up here yet :)"
        )

        nothing_button = ttk.Button( 
            master = self.frame,
            text = "Useless button"
            )

        nothing_label.grid(
            row=0, 
            column=0, 
            padx=5, 
            pady=5, 
            sticky=constants.W
        )

        nothing_button.grid(
            row=0,
            column=4,
            padx=5,
            pady=5,
            sticky=constants.EW
        )
    
    def initialize_product_list(self):
        if self.exp_list_view:
            self.exp_list_view.destroy()

        products = exp_service.get_ok_products()

        self.exp_list_view = ExpListView(
            self.exp_list_frame,
            products,
            self.handle_set_product_expired
        )

        self.exp_list_view.pack()

    def handle_set_product_expired(self, exp_id):
        exp_service.set_product_expired(exp_id)
        self.initialize_product_list()

    def initialize_footer(self):
        self.create_product_entry = ttk.Entry(master = self.frame)
        #self.product_type = ttk.Entry(master = self.frame)
        #self.product_date = ttk.Entry(master = self.frame)

        add_product_button = ttk.Button(
            master = self.frame,
            text = "Add Product",
            command = self.handle_add_product
        )
        
        self.create_product_entry.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )
        '''self.product_type.grid(
            row=2,
            column=2,
            padx=5,
            pady=5,
            sticky=constants.EW
        )
        self.product_date.grid(
            row=2,
            column=3,
            padx=5,
            pady=5,
            sticky=constants.EW
        )
        '''
        add_product_button.grid(
            row=2,
            column=4,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def handle_add_product(self):
        p_name = self.create_product_entry.get()
        #p_type = self.product_type.get()
        #p_date = self.product_date.get()

        if p_name:#and p_type and p_date:
            exp_service.add_product(p_name)
            self.initialize_product_list()
            self.create_product_entry.delete(0,constants.END)
            #self.product_type.delete(0,constants.END)
            #self.product_date.delete(0,constants.END)

    def show_exp_view(self):
        self.frame = ttk.Frame(master=self.root)
        self.exp_list_frame = ttk.Frame(master=self.frame)




class ExpListView:
    
    def __init__(self, root, products, handle_set_product_expired):
        self.root = root
        self.products = products
        self.handle_set_product_expired = handle_set_product_expired
        self.frame = None

        self.initialize()
    
    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def initialize(self):
        self.frame = ttk.Frame(master = self.root)

        for product in self.products:
            self.initialize_product(product)

    def initialize_product(self, product):
        product_frame = ttk.Frame(master = self.frame)
        label = ttk.Label(master=product_frame, text=product.content)

        set_expired_button = ttk.Button(
            master = product_frame,
            text = "Expired/Used",
            command = lambda: self.handle_set_product_expired(product.id)
        )
        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        set_expired_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        product_frame.grid_columnconfigure(0, weight=1)
        product_frame.pack(fill=constants.X)
