# ---------------------------------------------------------------------------- #
#                                  SOLUCIÓN 1                                  #
# ---------------------------------------------------------------------------- #

# --------- INFORMACIÓN ACERCA DE LAS ESTRUCTURAS DE DATOS A UTILIZAR -------- #
# Para almacenar la información de los animales se utilizará un diccionario
# Para almacenar las escenas se utilizaran las listas. Cada escena será una lista de 3 elementos
# Para almacenar las partes se utilizaran las listas. Cada parte será una lista de escenas

# -------------- INFORMACIÓN ACERCA DE LOS ALGORITMOS A UTILIZAR ------------- #
# Para ordenar las escenas y las partes podemos utilizar el algoritmo de ordenamiento por mezcla (merge sort) con algunas modificaciones, las cuales no afectaran la complejidad del algoritmo

from Solucion_1.Versions import (
    version1_solution1,
    version2_solution1,
    version3_solution1,
    version4_solution1,
    solution_1,
)

# ---------------------------------------------------------------------------- #
#                                  SOLUCIÓN 2                                #
# ---------------------------------------------------------------------------- #

# --------- INFORMACIÓN ACERCA DE LAS ESTRUCTURAS DE DATOS A UTILIZAR -------- #
# Para almacenar la información de los animales se utilizará una lista de tuplas
# Para almacenar las escenas se utilizaran las listas. Cada escena será una lista de 3 elementos
# Para almacenar las partes se utilizaran las listas. Cada parte será una lista de escenas

# -------------- INFORMACIÓN ACERCA DE LOS ALGORITMOS A UTILIZAR ------------- #
# Para ordenar las escenas y las partes podemos utilizar el algoritmo de ordenamiento por mezcla (merge sort) con algunas modificaciones, las cuales no afectaran la complejidad del algoritmo

from Solucion_2.Versions import (
    version1_solution2,
    version2_solution2,
    version3_solution2,
    version4_solution2,
    solution_2
)

# ---------------------------------------------------------------------------- #
#                                  SOLUCIÓN 3                                  #
# ---------------------------------------------------------------------------- #

# --------- INFORMACIÓN ACERCA DE LAS ESTRUCTURAS DE DATOS A UTILIZAR -------- #
# Para almacenar la información de los animales se utilizará una lista de listas
# Para almacenar las escenas se utilizaran las listas. Cada escena será una lista de 3 elementos
# Para almacenar las partes se utilizaran las listas. Cada parte será una lista de escenas

# -------------- INFORMACIÓN ACERCA DE LOS ALGORITMOS A UTILIZAR ------------- #
# Para ordenar las escenas y las partes podemos utilizar el algoritmo de ordenamiento por mezcla (merge sort) con algunas modificaciones, las cuales no afectaran la complejidad del algoritmo

from Solucion_3.Versions import (
    version1_solution3,
    version2_solution3,
    version3_solution3,
    version4_solution3,
    solution_3
)

if __name__ == "__main__":
    solution = 1
    version = 4
    if(solution == 1):
        if(version == 1):
            solution_1(version1_solution1())
        elif(version == 2):
            solution_1(version2_solution1())
        elif(version == 3):
            solution_1(version3_solution1())
        elif(version == 4):
            solution_1(version4_solution1())
    elif(solution == 2):
        if(version == 1):
            solution_2(version1_solution2())
        elif(version == 2):
            solution_2(version2_solution2())
        elif(version == 3):
            solution_2(version3_solution2())
        elif(version == 4):
            solution_2(version4_solution2())
    elif(solution == 3):
        if(version == 1):
            solution_3(version1_solution3())
        elif(version == 2):
            solution_3(version2_solution3())
        elif(version == 3):
            solution_3(version3_solution3())
        elif(version == 4):
            solution_3(version4_solution3())