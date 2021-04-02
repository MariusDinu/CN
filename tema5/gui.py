from tkinter import ttk

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import json
import numpy
import numpy as np
from numpy.linalg import eig
from main import citireFisier, getNorm, conditioning_number, checkSim, Jacobi, checkEgal


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
x = numpy.array([])
n = len(A_init)
epsilon = 1e-16
ev, Q, t = Jacobi(A_init)

U, S, Vt = np.linalg.svd(A_init, full_matrices=True)
inverse_numpy_matrix_MP = np.linalg.pinv(A_init)

get_pseudoinv_smallest_squares = np.dot(np.linalg.inv(np.dot(A_init, A_init)), A_init)
# calculate the difference and get norm
diff = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        diff[i].append(0)
for i in range(n):
    for j in range(n):
        diff[i][j] = inverse_numpy_matrix_MP[i, j] - get_pseudoinv_smallest_squares[i, j]
get_norm = np.linalg.norm(diff, ord=1)


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
        self.TopNotebook.tab(0, text="EX.1-Metoda Jacobi", compound="none", underline="-1", )

        self.TopNotebook_t1 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t1, padding=3)
        self.TopNotebook.tab(1, text="proprii (Λ)", compound="none", underline="-1", )

        self.TopNotebook_t2 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t2, padding=3)
        self.TopNotebook.tab(2, text="proprii (U)", compound="none", underline="-1", )

        self.TopNotebook_t3 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t3, padding=3)
        self.TopNotebook.tab(3, text="Norma", compound="none", underline="-1", )

        self.TopNotebook_t4 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t4, padding=3)
        self.TopNotebook.tab(4, text="EX.3", compound="none", underline="-1", )

        self.TopNotebook_t5 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t5, padding=3)
        self.TopNotebook.tab(5, text="Moore-Penrose", compound="none", underline="-1", )

        self.TopNotebook_t6 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t6, padding=3)
        self.TopNotebook.tab(6, text="pseudo-inversa", compound="none", underline="-1", )

        self.TopNotebook_t7 = Frame(self.TopNotebook)
        self.TopNotebook.add(self.TopNotebook_t7, padding=3)
        self.TopNotebook.tab(7, text="Norma", compound="none", underline="-1", )


        self.LabelCreate = Label(self.TopNotebook_t0)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text="Matricea A Este simetrica \n Metoda Jacobi: Numar maxim de rotatii = ")

        self.LabelCreate = Label(self.TopNotebook_t0)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=t)

        self.LabelCreate = Label(self.TopNotebook_t1)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 18))
        self.LabelCreate.configure(text="Valoriile proprii (Λ)=")

        self.LabelCreate = Label(self.TopNotebook_t1)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=ev)

        self.LabelCreate = Label(self.TopNotebook_t2)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 15))
        self.LabelCreate.configure(text="Vectorul de valori proprii (U) =")

        self.LabelCreate = Label(self.TopNotebook_t2)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=100, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=Q)

        self.LabelCreate = Label(self.TopNotebook_t3)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=100, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text="Norma||AinitU − UΛ||.  \n unde A_initU este \n si UΛ este")

        self.LabelCreate = Label(self.TopNotebook_t3)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=getNorm(A_init, ev, Q))

        self.LabelCreate = Label(self.TopNotebook_t3)
        self.LabelCreate.place(relx=0.050, rely=0.70, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=np.dot(A_init, ev))

        self.LabelCreate = Label(self.TopNotebook_t3)
        self.LabelCreate.place(relx=0.050, rely=0.80, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text= np.dot(ev, Q))

        self.LabelCreate = Label(self.TopNotebook_t4)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=80, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text="Valorile singulare ale matricei A:\n Rangul matricei: \n Numarul de conditionare al matricei A:")

        self.LabelCreate = Label(self.TopNotebook_t4)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=S)

        self.LabelCreate = Label(self.TopNotebook_t4)
        self.LabelCreate.place(relx=0.050, rely=0.70, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=np.linalg.matrix_rank(A_init))

        self.LabelCreate = Label(self.TopNotebook_t4)
        self.LabelCreate.place(relx=0.050, rely=0.80, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=conditioning_number(A_init, n))

        self.LabelCreate = Label(self.TopNotebook_t5)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text="Moore-Penrose:")

        self.LabelCreate = Label(self.TopNotebook_t5)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        #self.LabelCreate.configure(np.linalg.pinv(A_init))

        self.LabelCreate = Label(self.TopNotebook_t6)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text="Matricea pseudo-inversa in sensul celor mai mici patrate:")

        self.LabelCreate = Label(self.TopNotebook_t6)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=get_pseudoinv_smallest_squares)

        self.LabelCreate = Label(self.TopNotebook_t7)
        self.LabelCreate.place(relx=0.050, rely=0.30, height=30, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=" Norma pentru matricea pseudo-inversa in sensul celor mai mici patrate:")

        self.LabelCreate = Label(self.TopNotebook_t7)
        self.LabelCreate.place(relx=0.050, rely=0.60, height=60, width=500)
        self.LabelCreate.configure(foreground="#9F009F")
        self.LabelCreate.configure(font=("Courier", 10))
        self.LabelCreate.configure(text=get_norm)



if __name__ == '__main__':
    start_gui()
