from tkinter import Tk
from ui.ui import UI

def main():
    """Sovelluksen aloittava luokka."""
    window = Tk()
    window.title("Expire application")


    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()
