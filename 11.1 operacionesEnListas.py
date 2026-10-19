# ==============================================================================
# RETO DE CLASE: REBANADO DE LISTAS (SLICING) Y MANEJO DE EXCEPCIONES
# Instrucciones: Lee atentamente cada comentario marcado con "TODO:" y completa
# las pistas de código que se proporcionan abajo para resolver el ejercicio.
# ==============================================================================

# Lista base con objetos visuales usando camelCase
misPremios = ["🍎", "🍌", "🍇", "🎁", "🍉", "🍓"]


print("=== PARTE A: Uso de Slicing (Rebanado) ===")

# 1. TODO: Extrae las primeras tres frutas (índices 0, 1 y 2) de la lista 'misPremios'.
# Pista: Completa los índices dentro de los corchetes [inicio:fin]
primerasFrutas = misPremios[ : ]
print("Primeras tres frutas:", primerasFrutas)



# 2. TODO: Extrae el rango medio que va desde la uva hasta la sandía (índices 2, 3 y 4).
# Pista: Recuerda que el índice de 'fin' debe ser uno más arriba del que deseas capturar.
seccionMedia = misPremios[ : ]
print("Sección media del contenedor:", seccionMedia)



# 3. TODO: Crea una copia exacta de toda la lista original utilizando la sintaxis de corte sin números.
# Pista: Deja el espacio vacío antes y después de los dos puntos.
copiaPremios = misPremios[ : ]
print("Copia completa de la lista:", copiaPremios)



print("\n=== PARTE B: Protección de código con try ... except ===")

# 4. TODO: Escribe un bloque try-except completo que intente acceder al índice 5 de la lista 'misPremios'.
# Pista: Completa las estructuras de control y pon el índice correcto.
try:
    objetoExistente = misPremios[ ]
    print(f"Éxito: Se encontró el objeto {objetoExistente}")
except IndexError:
    print("Error: El índice no existe.")



# 5. TODO: Escribe un bloque try-except completo que intente acceder al índice 10 de la lista 'misPremios'.
# Pista: El bloque 'except' debe escuchar específicamente el tipo de error "IndexError".
try:
    print(misPremios[10])
except :
    print("¡Bloqueo seguro! El índice solicitado está fuera de rango.")



# Mensaje de control final para verificar el flujo continuo del programa
print("\n[Sistema]: El programa finalizó su ejecución de manera exitosa y segura.")
