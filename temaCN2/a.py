import numpy
import json


def load_input(file_name=r'config'):
    with open(file_name, 'r') as file_handler:
        return json.load(file_handler)


def main():
    c = []
    for i in range(0, 3):
        c.append(int(input()))
    print(c)
    x = numpy.array([])








if __name__ == '__main__':
        main()