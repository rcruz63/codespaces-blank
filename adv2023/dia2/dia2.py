import os

BAG = {"red": 12, "green": 13, "blue": 14}


def process_game(line: str, verbose: bool = False) -> int:
    """ Procesa una linea del juego. """
    
    # Separar la linea en sus componentes. Primero el juego de las jugadas
    game, moves = line.split(":")

    return result


def dia2_1(data, verbose: bool = False):
    """ Función principal del día 2-1. """

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
            result += process_game(line, verbose=verbose)
        # Imprimir el resultado
        print(f'resultado dia 2 - 1 = "{result}"')

def dia2_2(data, verbose: bool = False):
    """ Función principal del día 2-2. """

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
            result += decode_numbers(line, verbose=verbose)
        # Imprimir el resultado
        print(f'resultado dia 2 - 2 = "{result}"')


if __name__ == "__main__":
    dia2_1("test2_1.txt", verbose=True)
    dia2_2("test2_2.txt", verbose=True)
