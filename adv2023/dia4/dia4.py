import os

def procesar_tarjeta(line, verbose: bool = False):
    """ Procesar una tarjeta. """

    if verbose:
        print(f'line = "{line}"')

    # Separar la linea en partes
    card, numbers = line.strip().split(":")
    if verbose:
        print(f'card = "{card}"')
        print(f'numbers = "{numbers}"')

    # Separar los numeros
    lista_ganadores, jugada = numbers.strip().split("|")
    if verbose:
        print(f'ganadores = "{lista_ganadores}"')
        print(f'jugada = "{jugada}"')

    # Separar los numeros ganadores
    ganadores = [int(num) for num in lista_ganadores.split()]
    if verbose:
        print(f'ganadores = "{ganadores}"')

    # Separar los numeros de la jugada
    jugada = [int(num) for num in jugada.split()]
    if verbose:
        print(f'jugada = "{jugada}"')

    # Procesar la jugada
    power = 0
    for numero in jugada:
        if numero in ganadores:
            power += 1

    # Imprimir el resultado
    
    if verbose:
        print(f'resultado tarjeta = "{power}"')

    return power

def dia4_1(data, verbose: bool = False):
    """ Función principal del día 4-1. """

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
            power = procesar_tarjeta(line, verbose=verbose)
            if verbose:
                print(f'power = "{power}"')
            # Acumular el resultado
            if power > 0:
                result += 2**(power-1)
        # Imprimir el resultado

    print(f'resultado dia 4 - 1 = "{result}"')

def procesar_pila(jugadas, verbose: bool = False):
    """ Procesar la pila de tarjetas. """

    if verbose:
        print(f'jugadas = "{jugadas}"')

    # Procesar la pila de tarjetas
    index_jugada = 0
    for jugada in jugadas:
        if verbose:
            print(f'jugada = "{jugada}"')
        if jugada[1] > 0:
            for copias in range(jugada[1]):
                if verbose:
                    print(f'copias = "{copias}"')
                jugadas[index_jugada + copias + 1][2] += jugada[2]
                if verbose:
                    print(f'jugada = "{jugadas[index_jugada + copias + 1]}"')
        index_jugada += 1

    # Imprimir el resultado
    if verbose:
        print(f'resultado pila = "{jugadas}"')

    return jugadas


def dia4_2(data, verbose: bool = False):
    """ Función principal del día 4-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        num_line = 1
        jugadas = []
        for line in file:
            # Decodificar la linea
            power = procesar_tarjeta(line, verbose=verbose)
            jugadas.append([num_line, power, 1])
            num_line += 1
            if verbose:
                print(f'power = "{power}"')
        
        if verbose:
            print(f'jugadas = "{jugadas}"')

        # Procesar pila de tarjetas
        pila_tarjetas = procesar_pila(jugadas, verbose=verbose)
        
        result = 0
        for tarjeta in pila_tarjetas:
            result += tarjeta[2]

        # Imprimir el resultado

    print(f'resultado dia 4 - 2 = "{result}"')

if __name__ == "__main__":
    dia4_1("test4_1.txt", verbose=False)
    dia4_2("test4_2.txt", verbose=True)
