def run():
    string = input('Ingrese una palabra con acento:' )
    letter_list = list(string.upper())
    for letter in letter_list:
        if letter == 'Á':
            letter_list[letter_list.index(letter)] = 'A'
        elif letter == 'É':
            letter_list[letter_list.index(letter)] = 'E'
        elif letter == 'Í':
            letter_list[letter_list.index(letter)] = 'I'
        elif letter == 'Ó':
            letter_list[letter_list.index(letter)] = 'O'
        elif letter == 'Ú':
            letter_list[letter_list.index(letter)] = 'U'
    print('Se palabra queda asi: ', ''.join(letter_list))



if __name__ == '__main__':
    run()