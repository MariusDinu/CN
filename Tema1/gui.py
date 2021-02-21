from tkinter import ttk

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import test
from PIL import Image, ImageTk


def start_gui():
    global val, w, root
    root = Tk()
    root.resizable(False, False)
    top = Notepad_gui(root)  # aici sa seteza setarile pt layout
    test.init(root, top)
    root.mainloop()


w = None

firstPrecision = test.minimnumber()

class Notepad_gui:
    def __init__(self, top=None):
        _backgroundColor = '#969696'
        _foregroundColor = '#000000'
        _selectedColor = '#d9d9d9'
        _selectColor = '#EA67EA'

        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_backgroundColor)
        self.style.configure('.', foreground=_foregroundColor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _selectedColor), ('active', _selectColor)])

        top.geometry("600x450")
        top.title("CALCULE NUMERICE")
        top.configure(highlightcolor="black")

        self.TopNotebook = ttk.Notebook(top)
        self.TopNotebook.place(relx=0.02, rely=0.02, relheight=0.85, relwidth=0.97)  # setez pozitia la top list
        self.TopNotebook.configure(width=582)

        self.TopNotebook_t0 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t0, padding=3)
        self.TopNotebook.tab(0, text="TEMA1 EX.1", compound="none", underline="-1", )

        self.TopNotebook_t1 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t1, padding=3)
        self.TopNotebook.tab(1, text="TEMA1 EX.2.A", compound="none", underline="-1", )

        self.TopNotebook_t2 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t2, padding=3)
        self.TopNotebook.tab(2, text="TEMA1 EX.2.B", compound="none", underline="-1", )

        self.TopNotebook_t3 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t3, padding=3)
        self.TopNotebook.tab(3, text="TEMA1 EX.3", compound="none", underline="-1", )

        self.LabelCreate = Label(self.TopNotebook_t0)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 30))
        self.LabelCreate.configure(text="cel mai mic numar")

        self.LabelCreate = Label(self.TopNotebook_t0)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 30))
        self.LabelCreate.configure(text=test.minimnumber())

        self.LabelCreate = Label(self.TopNotebook_t1)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 18))
        self.LabelCreate.configure(text="Suma este neasociativa pentru A,B,C:")

        self.LabelCreate = Label(self.TopNotebook_t1)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=test.neasociativeOp(firstPrecision))

        self.LabelCreate = Label(self.TopNotebook_t2)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 15))
        self.LabelCreate.configure(text="Produsul este neasociativa pentru A,B,C:")

        self.LabelCreate = Label(self.TopNotebook_t2)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=test.exProdusNeasociativ(firstPrecision))

if __name__ == '__main__':
    start_gui()