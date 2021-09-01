def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input('Ingresa un numero: '))
        if num <= 0:
            raise Exception('Los numeros negativos no estan permitidos')
        print(divisors(num))
        print('Termino la Ejecución')
    except ValueError:
        print('Solo puedes ingresar un numero', ValueError)
    except Exception:
        print('No se permiten numeros negativos')

        
if __name__ == '__main__':
    run()