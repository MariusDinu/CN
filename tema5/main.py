# Dinu Marius
# Nassar Mahmoud
# 3A5 Tema 5
import json
import numpy
import numpy as np
from numpy.linalg import eig


def load_input(file_name=r'config'):
    with open(file_name, 'r') as file_handler:
        return json.load(file_handler)


def citireFisier():
    data = load_input()
    A_init = numpy.matrix(data[0])
    x = numpy.array([])
    n = len(A_init)
    epsilon = 1e-16
    print("Ex.1--------------------------")
    checkSim(A_init, n)
    # Jacobi-method
    ev, Q, t = Jacobi(A_init)
    print("Metoda Jacobi: Numar maxim de rotatii = ", t)
    print("Valoriile proprii (Λ)= ", ev)
    print("Vectorul de valori proprii (U) = ", Q)
    print("Norma ||AinitU − UΛ||. =", getNorm(A_init, ev, Q), " unde A_initU este ", np.dot(A_init, ev), " si UΛ este ",
          np.dot(ev, Q))

    U, S, Vt = np.linalg.svd(A_init, full_matrices=True)
    inverse_numpy_matrix_MP = np.linalg.pinv(A_init)

    print("\n\nEx.3:--------------------------------(folosind numpy)");
    print("Valorile singulare ale matricei A:\n", S)
    print("Rangul matricei: ", np.linalg.matrix_rank(A_init))
    print("Numarul de conditionare al matricei A: ", conditioning_number(A_init, n))
    print("Moore-Penrose: \n", inverse_numpy_matrix_MP)
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
    print("Matricea pseudo-inversa in sensul celor mai mici patrate: \n", get_pseudoinv_smallest_squares)
    print("Norma pentru matricea pseudo-inversa in sensul celor mai mici patrate: ", get_norm)


def getNorm(A_init, ev, Q):
    return abs(np.dot(A_init, ev) - np.dot(ev, Q))


def conditioning_number(A, n):
    max = 0
    min = 10000
    for i in range(n):
        for j in range(n):
            if A[i, j] > max:
                max = A[i, j]
            if min > A[i, j] > 0:
                min = A[i, j]
    return max / min


def checkSim(A, n):
    ok = 1
    trans = numpy.transpose(A)
    # print(trans)
    for p in range(0, n):
        for q in range(0, n):
            if checkEgal(A[p, q], trans[p, q]):
                ok = 1
            else:
                ok = 2

    if ok == 1:
        print("Matricea A Este simetrica")
    else:
        print("Nu este simetrica")


# formula din curs poate fi rescrisa ca A · (u1,u2, · · · ,un) = (λ1u1, λ2u2, · · · , λnun)
def Jacobi(A):
    n = A.shape[0]
    maxit = 100  # numarul maxim de iteratii pentru metoda Jacobi
    eps = 1.0e-15  # epsilon
    pi = np.pi  # pi
    info = 0  # return flag
    ev = np.zeros(n, float)  # initializam valoriile proprii
    U = np.zeros((n, n), float)  # initializam vectorii proprii corespunzatori
    for i in range(0, n):
        U[i, i] = 1.0

    for t in range(0,
                   maxit):  # avem un maxim de iteratii ca sa evitam un loop infinit deoarece se poate ca conditiile noastre de iesire sa nu functioneze
        s = 0  # suma elementelor care nu sunt pe diagonale
        for i in range(0, n):
            s = s + np.sum(np.abs(A[i, (i + 1):n]))
        if s < eps:
            info = t
            for i in range(0, n):
                ev[i] = A[i, i]
            break
        else:
            limit = s / (n * (n - 1) / 2.0)  # average value of off-diagonal elements
            for i in range(0, n - 1):  # sarim diagonala
                for j in range(i + 1, n):  # incep indicii pentru p si q
                    if np.abs(A[i, j]) > limit:  # aflam perechea perechea de tip i,j
                        denom = A[i, i] - A[j, j]
                        # incep indicii pentru unghi
                        if np.abs(denom) < eps:  # calculam unghiul
                            phi = pi / 4
                        else:
                            phi = 0.5 * np.arctan(2.0 * A[i, j] / denom)
                        si = np.sin(phi)
                        co = np.cos(phi)

                        # trecerea de la matricea A la store
                        # B pj si B qj
                        for k in range(i + 1, j):
                            store = A[i, k]
                            A[i, k] = A[i, k] * co + A[k, j] * si  # Bpj
                            A[k, j] = A[k, j] * co - store * si  # Bqj
                        for l in range(j + 1, n):
                            store = A[i, l]
                            A[i, l] = A[i, l] * co + A[j, l] * si
                            A[j, l] = A[j, l] * co - store * si
                        for z in range(0, i):
                            store = A[z, i]
                            A[z, i] = A[z, i] * co + A[z, j] * si
                            A[z, j] = A[z, j] * co - store * si
                        store = A[i, i]
                        A[i, i] = A[i, i] * co * co + 2.0 * A[i, j] * co * si + A[j, j] * si * si  # Bpp
                        A[j, j] = A[j, j] * co * co - 2.0 * A[i, j] * co * si + store * si * si  # Bqq
                        A[i, j] = 0.0
                        for p in range(0, n):
                            store = U[p, j]
                            U[p, j] = U[p, j] * co - U[p, i] * si
                            U[p, i] = U[p, i] * co + store * si
        info = -t  # in case no convergence is reached set info to a negative value "-t"
    return ev, U, t


def checkEgal(num1, num2):
    if num1 == num2:
        return True


def main():
    citireFisier()


if __name__ == '__main__':
    main()
