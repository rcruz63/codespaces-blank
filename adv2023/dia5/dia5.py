import os


def dia5_1(data, verbose: bool = False):
    """ Función principal del día 5-1. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
        for line in file:
            result = 0

    print(f'resultado dia 5 - 1 = "{result}"')


def dia5_2(data, verbose: bool = False):
    """ Función principal del día 5-2. """

    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_dir, data)
    if verbose:
        print(f'Opening file {data_path}')

    # Leer el archivo
    with open(data_path, "r", encoding="utf-8") as file:
        # Leer cada linea del archivo
        result = 0
     
        for line in file:
           result=0

        # Imprimir el resultado

    print(f'resultado dia 5 - 2 = "{result}"')

if __name__ == "__main__":
    dia5_1("test5_1.txt", verbose=False)
    dia5_2("test5_2.txt", verbose=True)
