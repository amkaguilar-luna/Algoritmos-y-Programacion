# Ejercicio 1 - Matriz de asientos de cine
cine = [
    ["1", "2", "3"],
    ["4", "X", "X"],
    ["7", "8", "X"]
]

print("Asientos disponibles:")

for fila in cine:
    print(fila)

asiento = input("\n_______________________________: ")

encontrado = False

for fila in range(len(cine)):
    for columna in range(len(cine[fila])):

        if cine[fila][columna] == asiento:
            cine[fila][columna] = "" #
            print("_______________________________")
            encontrado = #

if ___ encontrado:
    print("_________________________")

print("\nCine actualizado:")

for fila in cine:
    print("________________")
