from Ventana import *
from tkinter import *


def main():
    root = Tk()
    root.wm_title("CRUD")
    global app
    app = Ventana(root)
    app.mainloop()


if __name__ == "__main__":
    main()