tablero = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "2"],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
# Función para validar que el tablero es 9x9
def validar_tablero(tablero):
    if len(tablero) != 9:  # Verificar la longitud del tablero
        return False
    for fila in tablero:
        if len(fila) != 9:  # Verificar la longitud de cada fila
            return False
    return True

# Función para validar que una fila no contiene números repetidos
def validar_fila(fila):
    numeros = []  # Lista para almacenar los números encontrados en la fila
    for elem in fila:
        if elem != ".":  # Verificar si el elemento es diferente de "."
            if elem in numeros:  # Verificar si el número ya está en la lista de números
                return False  # Si está repetido, la fila no es válida
            numeros.append(elem)  # Agregar el número a la lista de números
    return True  # Si no hay repetidos, la fila es válida

# Función para validar que una columna no contiene números repetidos
def validar_columna(columna, tablero):
    numeros = []  # Lista para almacenar los números encontrados en la columna
    for fila in tablero:
        elem = fila[columna]  # Obtener el elemento de la columna actual
        if elem != ".":  # Verificar si el elemento es diferente de "."
            if elem in numeros:  # Verificar si el número ya está en la lista de números
                return False  # Si está repetido, la columna no es válida
            numeros.append(elem)  # Agregar el número a la lista de números
    return True  # Si no hay repetidos, la columna es válida

# Función para validar que un cuadrante no contiene números repetidos
def validar_cuadrante(fila_inicio, columna_inicio, tablero):
    numeros = []  # Lista para almacenar los números encontrados en el cuadrante
    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(columna_inicio, columna_inicio + 3):
            elem = tablero[i][j]  # Obtener el elemento del cuadrante actual
            if elem != ".":  # Verificar si el elemento es diferente de "."
                if elem in numeros:  # Verificar si el número ya está en la lista de números
                    return False  # Si está repetido, el cuadrante no es válido
                numeros.append(elem)  # Agregar el número a la lista de números
    return True  # Si no hay repetidos, el cuadrante es válido

# Función para validar el sudoku completo
def validar_sudoku(tablero):
    if not validar_tablero(tablero):  # Validar que el tablero sea 9x9
        return False
    for fila in tablero:
        if not validar_fila(fila):  # Validar cada fila del tablero
            return False
    for columna in range(9):
        if not validar_columna(columna, tablero):  # Validar cada columna del tablero
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not validar_cuadrante(i, j, tablero):  # Validar cada cuadrante del tablero
                return False
    return True

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# Validar y mostrar el resultado del sudoku
if validar_sudoku(tablero):
    print("El sudoku es válido.")
else:
    print("El sudoku no es válido.")

# Imprimir el tablero
imprimir_tablero(tablero)
0