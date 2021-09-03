import random
from os import system
from draw_game_hangman import draw

def validate_letter(letter, spaces, chars_dict, word):
    exist = False
    # Verificamos que la letra este en la lista de caracteres de la palabra
    if letter in word:
        # Ahra decimos que por cada indice con la llave de la letra
        for index in chars_dict[letter]:
            # Colocamos la letra en los espacios correspondientes al indice
            spaces[index] = letter
        exist = True
    string = ''.join(spaces)

    return (string, exist)


def select_word():
    system('clear')
    word = ''
    word_list = []
    with open(
        './archivos/words.txt', 'r', encoding='utf-8'
        ) as f:
        word_list = [word.strip() for word in f]
    word = random.choice(word_list)
        
    return str(word.upper())


def register_player(nickname, points):
    print(nickname, ' - ', points)
    with open('./archivos/records.txt', 'w', encoding='utf-8') as f:
        pass


def play(nickname, points):
    word_list_char = list(select_word())
    spaces = (['_'] * len(word_list_char))
    input_try = 0
    chars_dict = {}
    game = False
    
    # print(word_list_char)
    
    # Creamos un diccionario con las letras de la palabra
    for index, char in enumerate(word_list_char):
        # Vemos que la llave de la letra no exista para agregarla al diccionario
        if not chars_dict.get(char):
            chars_dict[char] = []
        # Agregamos las posiciones de las llaves para colocarlas en los spaces
        chars_dict[char].append(index)

    response = ''.join(spaces)

    while game == False:
        system('clear')
        print('Intentos Restantes: ', (10 - input_try))
        print('             ', response[0])
        draw(input_try)
        letter = input('Ingrese una letra: ')
        
        try:
            if not letter.isalpha():
                raise Exception
            
            response = validate_letter(letter.upper(), spaces, chars_dict, word_list_char)
            print(response[0])
            if response[1] == False:
                input_try += 1
            if list(response[0]) == word_list_char:
                game = True
            if input_try == 10:
                break
        except Exception:
            print('Error')
    
    system('clear')
    if game == True:
        print('🏆 Ganaste la palabra correcta era: ', "".join(word_list_char))
        points += 1
        register_player(nickname, points)
        slection()
    else:
        print('😭 Lo siento la palabra era: ', "".join(word_list_char))
        slection()


def slection():
    menu()
    nickname = ''
    select = input('Seleccione una opcion: ')
    assert select.isnumeric(), 'Solo puede ingresar las opciones mostradas'
    select = int(select)
    assert select <= 3 and select >=1 , 'Seleccione solo las opciones mostradas'
    if select == 1:
        # Aqui va la logica para el inicio del Juego
        if len(nickname) <= 0:
            nickname = input('Ingresa tu nombre o nickname: ')
            points = 0
        play(nickname, points)
    elif select == 2:
        # Aqui va la logica de los punteos
        pass
    else:
        system('clear')
        print('Gracias por jugar..!')

def screen():
    print(
        '''
        Bienvenido al juego de ahorcado..!
        '''
    )

def menu():
    print('''
    [1] - Jugar 🎮
    [2] - Ver Puntajes 🥇
    [3] - Salir ❌
    ''')

def run():
    screen()
    slection()


if __name__ == '__main__':
    system('clear')
    run()