from tkinter import ttk, constants

class ExpView:
    def __init__(self, root, test):         #Hyvin vaiheessa
        self.root = root
        self.frame = None
        self.create_exp = None
        self.exp_list_frame = None
        self.exp_list_view = None
        
        #self.initialize()

    def show_exp_view(self):
        self.frame = ttk.Frame(master=self.root)
        self.exp_list_frame = ttk.Frame(master=self.frame)

    def pack(self):
        self.frame.pack(fill=constants.X)