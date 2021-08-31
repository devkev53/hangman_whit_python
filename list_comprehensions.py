def run():
    # squares = []
    # for i in range(1, 101):
    #     if i%3 != 0:
    #         squares.append(i**2)
    
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    # list_challenge = [
    #     i for i in range(1, 100000) 
    #     if i % 9 == 0 and i % 6 == 0 and i % 4 == 0
    #     ]

    # Aplicando el conocimiento del MCD de los numeros (9, 6, 4) seria 36

    list_challenge = [i for i in range(1, 100000) if i % 36 == 0]
    print(list_challenge)


if __name__ == '__main__':
    run()