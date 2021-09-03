from os import system

hand = '''
    │▒│  /▒/        ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓           ▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓
    │▒│ /▒/        ▒▓▓▒▒▒▒▒▒▓▓   ▒▓▓▒▒▒▒▒▒   ▒▓▓▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▓▓▒▒▒▒▒         ▒▓▓▒▓▓   ▒▓▓▒▒▒▒▒▒▒▓▓
    │▒│/▒/─┬─┐     ▒▓▓      ▓▓   ▒▓▓         ▒▓▓                ▒▓▓            ▒▓▓  ▒▓▓   ▒▓▓      ▒▓▓
    │▒│▒|▒│▒│      ▒▓▓▓▓▓▓▓▓     ▒▓▓▓▓▓▓▓     ▒▓▓▓▓▓▓▓▓         ▒▓▓           ▒▒    ▒▓▓   ▒▓▓      ▒▓▓
    ┌┴─┴─┐-┘─┘     ▒▓▓▒▒▒▒▒▒▓▓   ▒▓▓▒▒▒▒       ▒▒▒▒▒▒▒▓▓        ▒▓▓                 ▒▓▓   ▒▓▓      ▒▓▓
    │▒┌──┘▒▒▒│     ▒▓▓      ▓▓   ▒▓▓                 ▒▓▓        ▒▓▓                 ▒▓▓   ▒▓▓      ▒▓▓
    └┐▒▒▒▒▒▒┌┘     ▒▓▓▓▓▓▓▓▓▓▓   ▒▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓         ▒▓▓                 ▒▓▓   ▒▓▓▓▓▓▓▓▓▓▓▓
     └┐▒▒▒▒┌┘      ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒           ▒▒                  ▒▒    ▒▒▒▒▒▒▒▒▒▒▒
'''
player_name = ''
menu = '''
    [1] - Nuevo Juego 🎮
    [2] - Ver Puntajes 🥇
    [3] - Salir ❌
'''

menu2 = '''
    [1] - Seguir Jugando 🎮
    [2] - Ver Puntajes 🥇
    [3] - Salir ❌
'''
def main():
    first_screen()

def first_screen():
    system('clear')
    print('''
     ▓▓    ▓▓   ▓▓▓▓▓▓▓▓  ▓▓▓▓   ▓▓   ▓▓▓▓▓▓▓▓▓   ▓▓▓▓   ▓▓▓▓   ▓▓▓▓▓▓▓▓  ▓▓▓▓   ▓▓
    ░▓▓   ░▓▓  ░▓▓░░░░▓▓ ░▓▓▓▓▓ ░▓▓  ░▓▓░░░░░░   ░▓▓░▓▓░▓▓░▓▓  ░▓▓░░░░▓▓ ░▓▓▓▓▓ ░▓▓
    ░▓▓▓▓▓▓▓▓  ░▓▓▓▓▓▓▓▓ ░▓▓░▓▓▓░▓▓  ░▓▓  ▓▓▓▓▓  ░▓▓░░▓▓▓ ░▓▓  ░▓▓▓▓▓▓▓▓ ░▓▓░▓▓▓░▓▓
    ░▓▓░░░░▓▓  ░▓▓░░░░▓▓ ░▓▓░░▓▓▓▓▓  ░▓▓  ░░░▓▓  ░▓▓ ░░░  ░▓▓  ░▓▓░░░░▓▓ ░▓▓░░▓▓▓▓▓
    ░▓▓   ░▓▓  ░▓▓   ░▓▓ ░▓▓ ░░▓▓▓▓  ░▓▓▓▓▓▓▓▓▓  ░▓▓      ░▓▓  ░▓▓   ░▓▓ ░▓▓ ░░▓▓▓▓
    ░░    ░░   ░░    ░░  ░░   ░░░░   ░░░░░░░░░   ░░       ░░   ░░    ░░  ░░   ░░░░  
    ''')
    print(menu)

    selection()

def selection():
    score = 0
    option = input('Ingresa un numero para una opcion del menu: ')
    try:
        if not option.isnumeric():
            raise Exception
        option = int(option)
        if option <= 0 or option >= 4:
            raise Exception  
    except Exception:
        print('👻 Solo puede seleccionar las opciones mostradas en el menu..!')

    if option == 1:
        play()
    elif option == 2:
        system('clear')
        read_records()
    elif option == 3:
        pass 

def play():
    system('clear')
    read_words()
    print(menu2)


def read_records():
    scores_dict = []
    print(hand)
    position = 1
    with open('./archivos/records.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line_list = line.split(':')
            print('''''',position, line_list[0], '....................', line_list[1],'pts.')
            position += 1

    print(menu)
    selection()


def read_words():
    with open('./archivos/words.txt', 'r', encoding='utf-8') as f:
        word_list = [word.strip().upper() for word in f]
        word_list = normalizer(word_list)

    print(word_list)


def normalizer(list_words):
    for word in list_words:
        letter_list = list(word)
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
        list_words[list_words.index(word)] = ''.join(letter_list)
    
    return(list_words)


if __name__ == '__main__':
    main()