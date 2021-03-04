from tkinter import ttk

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import json
import numpy
from functions import det,descLLT,tliber,subst,norma,inversa
from lu import LU_factorization, determinant_L, solve_system, check_solution

def start_gui():
    global val, w, root
    root = Tk()
    root.resizable(False, False)
    top = CN_gui(root)  # aici sa seteza setarile pt layout
    root.mainloop()

def load_input(file_name=r'config'):
    with open(file_name, 'r') as file_handler:
        return json.load(file_handler)

w = None

data = load_input()
A_init = numpy.matrix(data[0])
b = numpy.array(data[1])
x = numpy.array([])
n = len(A_init)
epsilon = 1e-16
desc = descLLT(A_init, n)
detA = det(desc, n)
substA = subst(desc, n, b)
normaA = norma(A_init, n, substA, tliber)
invers = inversa(A_init, n, detA)
luA = LU_factorization(A_init.copy(), n)
det_l = determinant_L(luA, n, print_determinant=True)
xA = solve_system(luA, n, b, x)
check = check_solution(A_init, b, xA, n)


class CN_gui:
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
        self.TopNotebook.tab(0, text="TEMA2 EX.1", compound="none", underline="-1", )

        self.TopNotebook_t1 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t1, padding=3)
        self.TopNotebook.tab(1, text="TEMA2 EX.2", compound="none", underline="-1", )

        self.TopNotebook_t2 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t2, padding=3)
        self.TopNotebook.tab(2, text="TEMA2 EX.3", compound="none", underline="-1", )

        self.TopNotebook_t3 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t3, padding=3)
        self.TopNotebook.tab(3, text="TEMA2 EX.4", compound="none", underline="-1", )

        self.TopNotebook_t4 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t4, padding=3)
        self.TopNotebook.tab(4, text="TEMA2 EX.5", compound="none", underline="-1", )

        self.TopNotebook_t5 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t5, padding=3)
        self.TopNotebook.tab(5, text="EX.5.A", compound="none", underline="-1", )

        self.TopNotebook_t6 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t6, padding=3)
        self.TopNotebook.tab(6, text="EX.5.B", compound="none", underline="-1", )

        self.TopNotebook_t7 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t7, padding=3)
        self.TopNotebook.tab(7, text="EX.5.C", compound="none", underline="-1", )

        self.TopNotebook_t8 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t8, padding=3)
        self.TopNotebook.tab(8, text="EX.5.D", compound="none", underline="-1", )

        self.LabelCreate = Label(self.TopNotebook_t0)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text="Matricea dupa descompunerea/factorizarea Cholesky")

        self.LabelCreate = Label(self.TopNotebook_t0)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=desc)

        self.LabelCreate = Label(self.TopNotebook_t1)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 18))
        self.LabelCreate.configure(text="Determinant")

        self.LabelCreate = Label(self.TopNotebook_t1)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=detA)

        self.LabelCreate = Label(self.TopNotebook_t2)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 15))
        self.LabelCreate.configure(text="substitutiei directe si inverse :")

        self.LabelCreate = Label(self.TopNotebook_t2)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=substA)

        self.LabelCreate = Label(self.TopNotebook_t3)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text="Norma:")

        self.LabelCreate = Label(self.TopNotebook_t3)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=normaA)

        self.LabelCreate = Label(self.TopNotebook_t4)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text="Inversa")

        self.LabelCreate = Label(self.TopNotebook_t4)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=invers)

        self.LabelCreate = Label(self.TopNotebook_t5)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text="printam descompunerea: L si U")

        self.LabelCreate = Label(self.TopNotebook_t5)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        #problema de la returnarea functii 
        self.LabelCreate.configure(text=luA)

        self.LabelCreate = Label(self.TopNotebook_t6)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text="printam descompunerea: determinantul A")

        self.LabelCreate = Label(self.TopNotebook_t6)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=det_l)

        self.LabelCreate = Label(self.TopNotebook_t7)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=" printam solutia aprox: x_LU")

        self.LabelCreate = Label(self.TopNotebook_t7)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=xA)

        self.LabelCreate = Label(self.TopNotebook_t8)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text="printam norma: || A_init * x_LU - b_init ||2 < 10 ** (-8)")

        self.LabelCreate = Label(self.TopNotebook_t8)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=check)


if __name__ == '__main__':
    start_gui()
