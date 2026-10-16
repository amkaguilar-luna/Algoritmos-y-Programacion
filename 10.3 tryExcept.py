while True:

    try:
        calificacion = float(input("Ingrese una calificación (0 a 10): "))

        if ______________________________:
            raise _________________________

    except __________________ as error:
        print("Error:", error)

    else:
        print(f"Calificación registrada correctamente: {calificacion}")
        break

print("Proceso terminado.")
