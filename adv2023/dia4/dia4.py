import os

def procesar_tarjeta(line, verbose: bool = False):
    """ Procesar una tarjeta. """

    # Separar la linea en partes
    card, numbers = line.strip(":")
    if verbose:
        print(f'card = "{card}"')
        print(f'numbers = "{numbers}"')

    # Separar los numeros
    lista_ganadores, jugada = numbers.split("|")
    if verbose:
        print(f'ganadores = "{lista_ganadores}"')
        print(f'jugada = "{jugada}"')

    # Separar los numeros ganadores
    ganadores = lista_ganadores.split(" ")
    if verbose:
        print(f'ganadores = "{ganadores}"')

    # Separar los numeros de la jugada
    jugada = jugada.split(" ")
    if verbose:
        print(f'jugada = "{jugada}"')

    # Procesar la jugada
    power = -1
    for numero in jugada:
        if numero in ganadores:
            power += 1

    # Imprimir el resultado
    if verbose:
        print(f'power = "{power}"')

    if power == -1:
        result = power
    else:
        result = 2 ** power

    return result

def dia4_1(data, verbose: bool = False):
    """ Función principal del día 3-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        for line in file:
            # Decodificar la linea
            jugada = procesar_tarjeta(line, verbose=verbose)
            if verbose:
                print(f'jugada = "{jugada}"')
            if jugada != -1:
                result += jugada
        # Imprimir el resultado

    print(f'resultado dia 4 - 1 = "{result}"')


def dia4_2(data, verbose: bool = False):
    """ Función principal del día 4-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

if __name__ == "__main__":
    dia4_1("test4_1.txt", verbose=True)
    #dia4_2("test4_2.txt", verbose=True)
