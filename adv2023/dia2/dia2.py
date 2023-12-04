import os

BAG = {"red": 12, "green": 13, "blue": 14}


def process_game(line: str, verbose: bool = False) -> int:
    """ Procesa una linea del juego. """
    
    # Separar la linea en sus componentes. Primero el juego de las jugadas
    game, hands = line.split(":")
    if verbose:
        print(f'game = "{game}"')
        print(f'hands = "{hands}"')

    valid = True

    # Obtener el ID del juego
    game_id = game.split()[1]
    if verbose:
        print(f'game_id = "{game_id}"')

    # Separar las jugadas
    hands = hands.split(";")
    if verbose:
        print(f'hands = "{hands}"')


    for hand in hands:
        # Separar la jugada en sus componentes
        colors = hand.split(",")
        if verbose:
            print(f'colors = "{colors}"')
        
        # Procesar cada color
        for color in colors:
            # Eliminar los espacios en blanco al principio y al final
            color = color.strip()
            if verbose:
                print(f'color = "{color}"')
            # Separar el color y el numero
            number, col = color.split(" ")
            if verbose:
                print(f'number = "{number}"')
                print(f'col = "{col}"')

            # Verificar si la jugada es válida
            if int(number) > BAG[col]:
                valid = False
                if verbose:
                    print(f'Jugada invalida: {col}:{number} - {BAG[col]}')
                break

        if not valid:
            break
    if verbose:
        print(f'line = "{line}"')
        print(f'valid = "{valid}"')
        print(f'game_id = "{game_id}"')
    return (valid, game_id)


def dia2_1(data, valido, verbose: bool = False):
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
            salida = process_game(line, verbose=verbose)
            if verbose:
                print(f'salida = "{salida}"')
            if valido and salida[0]:
                result += int(salida[1])
            if not valido and not salida[0]:
                result += int(salida[1])
        # Imprimir el resultado
        print(f'resultado dia 2 - 1 = "{result}"')

def power(line: str, verbose: bool = False) -> int:
    """ Procesa una linea del juego. """
    
    # Separar la linea en sus componentes. Primero el juego de las jugadas
    game, hands = line.split(":")
    if verbose:
        print(f'game = "{game}"')
        print(f'hands = "{hands}"')

    # Obtener el ID del juego
    red = 0
    green = 0
    blue = 0

    # Separar las jugadas
    hands = hands.split(";")
    if verbose:
        print(f'hands = "{hands}"')

    for hand in hands:
        # Separar la jugada en sus componentes
        colors = hand.split(",")
        if verbose:
            print(f'colors = "{colors}"')

        # Procesar cada color
        for color in colors:
            # Eliminar los espacios en blanco al principio y al final
            color = color.strip()
            if verbose:
                print(f'color = "{color}"')
            # Separar el color y el numero
            number, col = color.split(" ")
            if verbose:
                print(f'number = "{number}"')
                print(f'col = "{col}"')

            if col == "red" and int(number) > red:
                red = int(number)
            elif col == "green" and int(number) > green:
                green = int(number)
            elif col == "blue" and int(number) > blue:
                blue = int(number)

    if verbose:
        print(f'line = "{line}"')
        print(f'red = "{red}"')
        print(f'green = "{green}"')
        print(f'blue = "{blue}"')
        print(f'result = "{red * green * blue}"')
    return red * green * blue


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
            result += power(line, verbose=verbose)
        # Imprimir el resultado
        print(f'resultado dia 2 - 2 = "{result}"')


if __name__ == "__main__":
    dia2_1("test2_1.txt", True, verbose=True)
    dia2_2("test2_2.txt", verbose=True)
