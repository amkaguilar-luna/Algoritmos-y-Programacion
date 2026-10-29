# PISTA 1: variable GLOBAL con el nombre de la materia (texto entre comillas)
materia = ______

# PISTA 2: palabra reservada para definir una función
___ calcularPromedio(n1, n2, n3):
    # PISTA 3: suma las tres calificaciones (+) y divide (/) entre la cantidad de calificaciones
    promedio = (n1 ___ n2 ___ n3) ___ ___
    # PISTA 4: muestra el promedio con 1 decimal (formato de f-string)
    ______(f"Promedio calculado: {promedio:___}")
    # PISTA 5: la función debe devolver el resultado al programa principal
    ______ promedio

# PISTA 6: define la función principal
___ main():
    # PISTA 7: inicia el bloque donde puede ocurrir un error
    ___:
        # PISTA 8: muestra en pantalla la materia (variable global)
        ______("Materia:", ______)

        # PISTA 9: input() devuelve texto, conviértelo a número decimal
        cal1 = _____(______("Calificación 1: "))
        cal2 = _____(______("Calificación 2: "))
        cal3 = _____(______("Calificación 3: "))

        # PISTA 10: fuera de rango = menor que 0 O mayor que 100
        if cal1 ___ 0 ___ cal1 ___ 100:
            # PISTA 11: palabra para lanzar un error a propósito
            ______ ValueError("La calificación 1 está fuera de rango.")

        if cal2 ___ 0 ___ cal2 ___ 100:
            ______ ValueError("La calificación 2 está fuera de rango.")

        if cal3 ___ 0 ___ cal3 ___ 100:
            ______ ValueError("La calificación 3 está fuera de rango.")

        # PISTA 12: llama a la función y guarda lo que devuelve
        ______ = calcularPromedio(______, ______, ______)

        # PISTA 13: variable LOCAL (solo existe dentro de main)
        mensaje = ""

        # PISTA 14: aprueba con 70 o más; si no, reprueba
        if promedio ___ 70:
            mensaje = ______
        ___:
            mensaje = ______

        # PISTA 15: muestra el resultado guardado en la variable local
        print("Resultado:", ______)

    # PISTA 16: captura el tipo de error y guárdalo con el nombre "error"
    ______ ______ ___ error:
        # PISTA 17: muestra el mensaje del error
        print("Error:", ______)

# PISTA 18: ejecuta el programa
______
