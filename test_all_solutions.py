import time
from tabulate import tabulate

from Solucion_1.Versions import (
    version1_solution1,
    version2_solution1,
    version3_solution1,
    version4_solution1,
    solution_1,
)

from Solucion_2.Versions import (
    version1_solution2,
    version2_solution2,
    version3_solution2,
    version4_solution2,
    solution_2
)

from Solucion_3.Versions import (
    version1_solution3,
    version2_solution3,
    version3_solution3,
    version4_solution3,
    solution_3
)

def medir_tiempo_ejecucion(solucion, version):
    start_time = time.time()
    solucion(version())
    end_time = time.time()
    return end_time - start_time


def main():
    soluciones = [
        {"solucion": solution_1, "versiones": [version1_solution1, version2_solution1, version3_solution1, version4_solution1]},
        {"solucion": solution_2, "versiones": [version1_solution2, version2_solution2, version3_solution2, version4_solution2]},
        {"solucion": solution_3, "versiones": [version1_solution3, version2_solution3, version3_solution3, version4_solution3]}
    ]

    resultados = []

    for solucion_info in soluciones:
        tiempos_solucion = [solucion_info["solucion"].__name__]
        print(tiempos_solucion)
        for version in solucion_info["versiones"]:
            tiempo_ejecucion = medir_tiempo_ejecucion(solucion_info["solucion"], version)
            tiempos_solucion.append(tiempo_ejecucion)

        resultados.append(tiempos_solucion)

    encabezados = ["Solución/Version"] + [f"Versión {i}" for i in range(1, 5)]
    filas = resultados

    print(tabulate(filas, headers=encabezados, tablefmt="grid"))

if __name__ == "__main__":
    main()