import json

import numpy
from functions import det,descLLT,tliber,subst,norma,inversa
from lu import LU_factorization, determinant_L, solve_system, check_solution
def load_input(file_name=r'config'):
    with open(file_name, 'r') as file_handler:
        return json.load(file_handler)

def citireFisier():
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
    determinant_L(luA, n, print_determinant=True)
    xA = solve_system(luA, n, b, x)
    check_solution(A_init, b, xA, n)

def citireTastatura():
    print("Introdu n: ")
    n = int(input())
    print("Introdu matricea: ")
    A_init = []
    for i in range(n):
        # taking row input from the user
        row = list(map(int, input().split()))
        # appending the 'row' to the 'matrix'
        A_init.append(row)
    print(A_init)

    c=[]
    for i in range(0, n):

        c.append(int(input()))
    b=c.copy()
    print(b[0])
    x = numpy.array([])

    epsilon = 1e-16
    desc = descLLT(A_init, n)
    detA = det(desc, n)
    substA = subst(desc, n, b)
    normaA = norma(A_init, n, substA, tliber)
    invers = inversa(A_init, n, detA)

    luA = LU_factorization(A_init.copy(), n)
    determinant_L(luA, n, print_determinant=True)
    xA = solve_system(luA, n, b, x)
    check_solution(A_init, b, xA, n)

def citireRandom():
    data = load_input()
    A_init = numpy.matrix(data[0])
    b = numpy.array(data[1])
    x = numpy.array([])
    n = len(A_init)
def main():
    #citireTastatura()
    #citireRandom()
    citireFisier()





if __name__ == '__main__':
        main()