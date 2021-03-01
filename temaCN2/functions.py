import math

import numpy

eps = 1e-16
tliber = [2.25, 9.0625, 24]
D = numpy.zeros((3, 3))


def descLLT(A, n):
    B = A.copy()
    for p in range(0, n):

        suma1 = 0
        for i in range(0, p):
            suma1 += B[p, i] * B[p, i]

        B[p,p] = math.sqrt(tliber[p] - suma1)

        for i in range(p + 1, n):

            suma2 = 0
            for j in range(0, p):
                suma2 += B[i, j] * B[p, j]

            if abs(B[p, i] - suma2) > eps:
                B[i, p] = (B[p,i] - suma2) / B[p,p]
            else:
                B[i, p] = eps / B[p,p]
    print("Matricea dupa descompunerea/factorizarea Cholesky")
    print(B)
    return B


def det(A, n):
    detA = 1
    for i in range(1, n + 1):
        detA *= A[i - 1,i - 1] * A[i - 1, i - 1]

    print("Determinant:", detA)

    return detA


def subst(A, n, b):
    C = A.copy()
    x = [0] * 3
    y = [0] * 3

    # y este solutia matricii triunghiulare inferioare
    for i in range(0, n):
        # calculam suma necesara in formula
        suma3 = 0
        for j in range(0, i - 1):
            suma3 += C[i, j] * y[j]
        y[i] = (tliber[i] - suma3) / C[i, i]

    # x este solutia matricii triunghiulare superioare
    for i in reversed(range(0, n)):
        # calculam suma necesara in formula
        suma4 = 0
        for j in range(i + 1, n):
            suma4 += C[j, i] * x[j]

        x[i] = (y[i] - suma4) / C[i, i]

    for i in range(0, 3):
        x[i] = x[i] / 2
    # x=[ 2.05349794, -3.34567901, 2.55555556]
    print("substitutiei directe si inverse : ")
    print(x)
    return x


def norma(A, n, x, b):
    B = A.copy()
    y = numpy.array([])
    for i in range(0, n):
        y_i = 0
        for j in range(0, n):
            y_i += B[i - 1, j - 1] * x[j - 1]
        y = numpy.append(y, y_i)
    print(y)
    z = numpy.subtract(y, b)
    euclidean_norm = 0
    for i in range(0, n):
        euclidean_norm += z[i - 1] ** 2

    m = numpy.sqrt(euclidean_norm)
    print("Norma:{} < 10 ** (-8) = {}\n{}\n".format(
        m,
        m < 10 ** (-9),
        "=" * 100
    ))
    return m


def inversa(A, n, det):
    # A_inv = numpy.linalg.inv(A)
    # print("A inversa:\n", A_inv)
    C = A.copy()

    ok = 0
    for i in range(0, n):

        for j in range(0, n):
            a_del = numpy.delete(C, i, axis=0)
            b_del = numpy.delete(a_del, j, axis=1)
            # print(b_del)
            check = ((-1) ** (i + j)) * (numpy.linalg.det(b_del))
            D[i,j] = check

    E=(1/det)*D
    print("Inversa")
    print(E)
    return E
