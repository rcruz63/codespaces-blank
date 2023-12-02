""" Dia 1-1: 
    1. Leer un archivo de texto. 
    2. Para cada linea del archivo encontrar el primer digito que aparece y el último, 
        devolver la suma de ambos.
    3. Sumar todos los resultados de cada linea.
    4. Imprimir el resultado.
"""

import os

# buscar todas las veces que aparece un string en otro y devolver una lista
# con parejas de {string, posición}
def find_all(line, number, lista, verbose: bool = False):
    """ Recibe un string y un substring, busca todas las apariciones del substring en el string
        y devuelve una lista con las posiciones de cada aparición.
    """
    index = line.find(number)
    while index != -1:
        lista.append({number:index})
        index = line.find(number, index + 1)
        if verbose:
            print(f'lista: {lista}')

    if verbose:
        print(f'lista final: {lista}')
    return lista



def decode_line(line, verbose: bool = False):
    """ Recibe un texto, busca el primer digito y el último, devuelve la suma de ambos. """
    # Buscar el primer digito
    first = 0
    for char in line:
        if char.isdigit():
            first = char
            break
    # Buscar el último digito
    last = 0
    for char in reversed(line):
        if char.isdigit():
            last = char
            break
    # Devolver la suma
    suma = first + last
    if verbose:
        print(f'{line} = {suma}')
    return int(suma)

def decode_numbers(line, verbose: bool = False):
    """ Recibe una linea de texto busca la aparición de las cadenas: 
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"
        y las reemplaza por los números correspondientes.
        devuelve la linea con los números reemplazados.
    """
    decode = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
                "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
                "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
                "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
    aparece = []
    # Buscar la aparición de las cadenas
    if verbose:
        print(f'linea: {line}')
    for number in numbers:
        # Buscar en linea si aparece el número y guardar en aparece todas las veces 
        # que aparece como {número: posición}
        if number in line:
            aparece = find_all(line, number, aparece, verbose=verbose)

    if verbose:
        print(f'aparece asorted: {aparece}')
    # Ordenar la lista de apariciones por posición
    aparece.sort(key=lambda x: list(x.values())[0])
    if verbose:
        print(f'aparece sorted: {aparece}')
    first = decode[list(aparece[0].keys())[0]]
    last = decode[list(aparece[-1].keys())[0]]

    if verbose:
        print(f'first: {first}, last: {last}')
    # Devolver concatenados el primer y último número
    return int(first + last)

def dia1_1(data, verbose: bool = False):
    """ Función principal del día 1-1. """

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
            result += decode_line(line, verbose=verbose)
        # Imprimir el resultado
        print(f'resultado dia 1 - 1 = "{result}"')

def dia1_2(data, verbose: bool = False):
    """ Función principal del día 1-2. """

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
        print(f'resultado dia 1 - 2 = "{result}"')


def main(file, verbose: bool = False):
    """ Esta es la función principal del día 1. """
    dia1_1(file, verbose=verbose)



if __name__ == "__main__":
    dia1_1("test1_1.txt", verbose=True)
    dia1_2("test1_2.txt", verbose=True)
