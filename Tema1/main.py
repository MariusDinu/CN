

def minimnumber():
    #am creat un array ca sa salvam toate numerele u care respecta conditiile
    numbers = []
    for m in range(1000):
        #declaram si initializam u unde m este de la 0 la 1000
        u = 1 / pow(10, m)
        #verificam prima conditie
        if 1.0 + u != 1.0:
            #verificam daca u este mai mare ca 0
            if u > 0:
                #inseram in array u
                numbers.insert(m,u)
            #afisam fiecare u care respecta conditiile
            print(u)
    print(numbers)
    #sortam array-ul ca sa avem pe prima pozitie cel mai mic numar
    numbers.sort()
    #afisam numarul cel mai mic din array
    print(numbers[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    minimnumber()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
