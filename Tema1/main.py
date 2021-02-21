

def minimnumber():
    #
    numbers = []
    for m in range(1000):
        u = 1 / pow(10, m)
        if 1.0 + u != 1.0:
            if u > 0:
                numbers.insert(m,u)
            print(u)
    print(numbers)
    numbers.sort()
    print(numbers[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    minimnumber()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
