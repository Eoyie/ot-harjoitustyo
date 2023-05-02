from tkinter import Tk
from ui.ui import UI

def main():
    """Sovelluksen aloittava luokka."""
    window = Tk()
    window.title("Expire application (test stage)")
    window.geometry("500x450")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()
