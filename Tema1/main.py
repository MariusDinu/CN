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

def exProdusNeasociativ():
    a=1.999*2.3
    b=2.000
    c=2.000
    if (a * b) * c != a * (b * c):
        print("Produsul este neasociativ")
        print(a, b, c)

if __name__ == '__main__':
    #firstPrecision = minimnumber()
    #neasociativeOp(firstPrecision)
    exProdusNeasociativ()


