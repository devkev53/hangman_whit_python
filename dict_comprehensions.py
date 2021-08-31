# Importar la libreria math permite operaciones matematicas
import math


def run():

    dict_example = {i:(i**3) for i in range(1, 101) if i % 3 != 0}
    dict_challenge = {i: round(math.sqrt(i), 2) for i in range(1, 1000)}
    print(dict_challenge)

if __name__ == '__main__':
    run()