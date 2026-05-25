# -----------------
# Nombre del estudiante: Juan David Guevara Patino
# Grupo:213022_937
# Programa: Ingenieria Electronica
# Codigo fuente: Autoria Propia
# ----------------


# Matriz con 4 recursos y sus horas trabajadas de Lunes a Viernes
# Formato: [Nombre del Recurso, Lunes, Martes, Miercoles, Jueves, Viernes]
matriz_horas = [
    ["Ana", 8, 8, 8, 8, 8],
    ["Luis", 9, 9, 8, 9, 8],
    ["Carlos", 7, 8, 7, 8, 8],
    ["Marta", 10, 10, 10, 8, 8]
]

def evaluar_jornada(empleado):
    nombre = empleado[0]
    
    # 1. Primero calculamos los totales sumando cada día
    total_horas = empleado[1] + empleado[2] + empleado[3] + empleado[4] + empleado[5]
    
    # 2. Luego validamos con el total ya calculado
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
        
    return nombre, total_horas, clasificacion

def imprimir_tabla(matriz):
    # Imprimimos el encabezado de la tabla usando comillas triples igual que en tu imagen
    print('''
    ┌────────────────────────────────────────────────────────┐
    │                  INFORME DE HORAS                      │
    ├────┬────────────────────┬───────────────┬──────────────┤
    │ No │ Nombre             │ Total Horas   │ Jornada      │
    ├────┼────────────────────┼───────────────┼──────────────┤''')
    
    # Recorremos la matriz para evaluar y mostrar cada empleado
    for i in range(len(matriz)):
        # Llamamos a la función para que nos dé los datos listos
     nombre, total, jornada = evaluar_jornada(matriz[i])
        
        # Usamos f-strings para alinear las columnas (ej: {nombre:18} deja 18 espacios)
    print(f"    │ {i+1:2} │ {nombre:18} │ {total:13} │ {jornada:12} │")
        
    # Cerramos la tabla al final del ciclo
    print("    └────┴────────────────────┴───────────────┴──────────────┘")

# Ejecutamos la función principal
imprimir_tabla(matriz_horas)
