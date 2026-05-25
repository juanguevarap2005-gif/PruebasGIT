# -----------------
# Nombre del estudiante: Juan David Guevara Patino
# Grupo:213022_937
# Programa: Ingenieria Electronica
# Codigo fuente: Autoria Propia
# ----------------


# Matriz con 4 recursos y sus horas trabajadas de Lunes a Viernes
# Formato: [Nombre del Recurso, Lunes, Martes, Miercoles, Jueves, Viernes]

# Función para ingresar horas válidas
def pedir_horas(dia, nombre):

    while True:
        dato = input(f"Ingrese horas trabajadas por {nombre} el {dia}: ")

        try:
            horas = int(dato)

            if horas >= 0:
                return horas
            else:
                print("Ingrese un número válido")

        except ValueError:
            print("Solo se permiten números. Intente nuevamente")


# Función para clasificar
def calcular_horas(total):

    if total > 40:
        return "Sobretiempo"

    else:
        return "Horario Estándar"


# Función para mostrar tabla
def mostrar_tabla(recursos):

    print("\n┌──────────────────────────────────────────────────────────────┐")
    print("│                     INFORME DE HORAS                       │")
    print("├────┬────────────────────┬───────────────┬──────────────────┤")
    print("│ No │ Nombre             │ Total Horas   │ Jornada          │")
    print("├────┼────────────────────┼───────────────┼──────────────────┤")

    for i in range(len(recursos)):

        nombre = recursos[i][0]

        total = sum(recursos[i][1:])

        jornada = calcular_horas(total)

        print(
            f"│ {i+1:<2} │ "
            f"{nombre:<18} │ "
            f"{total:<13} │ "
            f"{jornada:<16} │"
        )

    print("└────┴────────────────────┴───────────────┴──────────────────┘")


# Repetir programa
while True:

    recursos = []

    # Ingreso de datos
    for i in range(4):

        nombre = input(f"\nIngrese nombre del recurso {i+1}: ")

        lunes = pedir_horas("Lunes", nombre)
        martes = pedir_horas("Martes", nombre)
        miercoles = pedir_horas("Miércoles", nombre)
        jueves = pedir_horas("Jueves", nombre)
        viernes = pedir_horas("Viernes", nombre)

        recursos.append([
            nombre,
            lunes,
            martes,
            miercoles,
            jueves,
            viernes
        ])

    # Mostrar resultados en tabla
    mostrar_tabla(recursos)

    # Menú final
    print("\n1. Ingresar datos nuevamente")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "2":
        print("Programa finalizado")
        break
    