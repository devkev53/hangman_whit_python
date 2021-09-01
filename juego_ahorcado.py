def slection():
    select = input('Seleccione una opcion: ')
    assert select.isnumeric(), 'Solo puede ingresar las opciones mostradas'

def screen():
    print(
        '''
        Bienvenido al juego de ahorcado..!
        '''
    )
    menu()

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
    run()