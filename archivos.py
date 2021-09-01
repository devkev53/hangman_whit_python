def read():
    numbers = []
    with open(
        './archivos/numbers.txt', 'r', encoding='utf-8'
        ) as f:
        for line in f:
            numbers.append(int(line))

    print(numbers)

def write():
    names = [
        'Kevin', 'Pedro', 'Maria', 'Bellini', 'Roció', 'Mañana',
        'Concepción', 'Martín', 'Carlos', 'Estuardo', 'Brayan'
    ]
    index = 0
    with open(
        './archivos/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            index += 1
            f.write(str(index) + '-' + name)
            f.write('\n')

def run():
    write()


if __name__ == '__main__':
    run()