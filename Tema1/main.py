#Dinu Marius 3A5
#Nassar Mahmoud 3A5
#Tema 1
#Calcule Numerice


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


import math
import random
import time


def minimnumber():
    # am creat un array ca sa salvam toate numerele u care respecta conditiile
    numbers = []
    for m in range(1000):
        # declaram si initializam u unde m este de la 0 la 1000
        u = 1 / pow(10, m)
        # verificam prima conditie
        if 1.0 + u != 1.0:
            # verificam daca u este mai mare ca 0
            if u > 0:
                # inseram in array u
                numbers.insert(m, u)
            # afisam fiecare u care respecta conditiile
            print(u)
    print(numbers)
    # sortam array-ul ca sa avem pe prima pozitie cel mai mic numar
    numbers.sort()
    # afisam numarul cel mai mic din array
    print(numbers[0])
    return numbers[0]


def neasociativeOp(u):
    a = 1.0
    b = u / 10
    c = u / 10
    if (a + b) + c != a + (b + c):
        print("Suma este neasociativa:")
        print(a, b, c)

    if (a * b) * c != a * (b * c):
        print("Produsul este neasociativ")
        print(a, b, c)
    return a, b, c


def exProdusNeasociativ(u):
    a = 2.2
    b = u / 10
    c = u / 10
    if (a * b) * c != a * (b * c):
        print("Produsul este neasociativ")
        print("Primul produs:", (a * b) * c)
        print("Al doilea produs:", a * (b * c))
    return a, b, c


def method2Tan(number):
    c1 = 0.33333333333333333
    c2 = 0.133333333333333333
    c3 = 0.053968253968254
    c4 = 0.0218694885361552

    x1 = number ** 3
    x2 = number ** 5
    x3 = number ** 7
    x4 = number ** 9

    polinom = number + c1 * x1 + c2 * x2 + c3 * x3 + c4 * x4
    return polinom


def runTan():
    print("Method 2: Polinoms")
    # preluam valoare pi
    pi = math.pi
    # salvam timpul de start
    startTime = time.time()
    sumError = 0

    #avel cele 10000 de variabile din for
    for i in range(0, 10000):
        myTan = 0
        pyTan = 0
        #luam variabile random uniform din intervalul nostru
        value = random.uniform(-pi / 2, pi / 2)

        if -pi / 4 < value < pi / 4:
            myTan = method2Tan(value)
            pyTan = math.tan(value)

        if pi / 4 < value < pi / 2:
            myTan = 1 / (method2Tan((pi / 2) - value))
            pyTan = 1 / (math.tan((pi / 2) - value))

        if -pi / 2 < value < -pi / 4:
            myTan = 1 / (method2Tan(pi - ((pi / 2) - value)))
            pyTan = 1 / (math.tan(pi - ((pi / 2) - value)))
        #calculam suma de la eroarea medie
        sumError = sumError + abs(pyTan - myTan)
        print("[", i + 1, "]", "Pentru x = ", value, ", Eroare medie =", abs(pyTan - myTan))

    avgErr = sumError / 10000
    print("Formula eroare medie: (|tan(x)−my tan(x)|) ")
    print("Eroarea medie de calcul:", format(avgErr, ".12f"))

    finalTime = time.time()
    print("Timpul de calcul :", (finalTime - startTime))

    return format(avgErr, ".12f"), (finalTime - startTime)


if __name__ == '__main__':

    # Ex1
    firstPrecision = minimnumber()

    # Ex2 a.
    neasociativeOp(firstPrecision)
    # Ex2 b.
    exProdusNeasociativ(firstPrecision)

    # Ex3 method1: Continuous Fractions

    # Ex3 method2: Polinoms
    runTan()
