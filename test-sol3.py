import random
import time

import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

from Solucion_3.ConcertZoo3 import ConcertZoo3

def version_generalizada(m, k):
    # n es constante
    n = 9

    # Definir la lista de animales
    animals = [
        ['An', 1],
        ['Bo', 2],
        ['Ca', 3],
        ['Do', 4],
        ['El', 5],
        ['Fl', 6],
        ['Ga', 7],
        ['Ho', 8],
        ['Ig', 9],
    ]
    
    # Inicializar la apertura y el resto del show
    aperture = []
    rest_of_show = []

    # Generar (m-1)*k escenas para la apertura
    for _ in range((m - 1) * k):
        # Seleccionar 3 animales aleatorios de la lista 'animals'
        scene_animals = random.sample(animals, 3)
        
        # Extraer los nombres de los animales seleccionados
        scene_names = [animal[0] for animal in scene_animals]
        
        # Agregar la escena a la apertura
        aperture.append(scene_names)
    
    # Crear una lista auxiliar igual a la apertura
    aux_aperture = aperture.copy()

    # Generar m-1 partes de k escenas cada una para el resto del show
    for _ in range(m-1):
        part = []
        for _ in range(k):
            # Tomar una escena aleatoria de la lista auxiliar y agregarla al resto del show
            scene = random.choice(aux_aperture)
            aux_aperture.remove(scene)
            part.append(scene)

        rest_of_show.append(part)

    # Devolver el resultado como un diccionario
    result = {
        'm': m,
        'n': n,
        'k': k,
        'animals': animals,
        'aperture': aperture,
        'rest_of_show': rest_of_show,
    }

    return result


def measure_execution_time(versions, function_to_test):
    times = []
    for version in versions:
        concert = ConcertZoo3(version['n'], version['m'], version['k'])
        concert.add_animals(version['animals'])
        concert.add_aperture(version['aperture'])
        concert.add_rest_of_show(version['rest_of_show'])

        start_time = time.time()
        function_to_test(concert)
        end_time = time.time()

        execution_time = end_time - start_time
        times.append(execution_time)

    return times



def plot_execution_times(versions, function_to_test, times):
    sizes = [(version['m'] -1) * version['k'] for version in versions]
    print(sizes)
    times = measure_execution_time(versions, function_to_test)

    plt.plot(sizes, times, marker='o', label='Actual Performance')
    
    # Añadir línea de ajuste
    z = np.polyfit(sizes, times, 1)
    p = np.poly1d(z)
    # plt.plot(sizes, p(sizes), 'r--', label='Fit Line')
    
    

    plt.title('Execution Time vs Input Size for ' + function_to_test.__name__) 
    plt.xlabel('Input Size: (m-1)*k')
    plt.ylabel('Execution Time (s)')

    plt.legend()
    plt.show()



if __name__ == "__main__":
    # Generamos  versiones de prueba con version_prueba, por ahroa solo vamos a viarar m, k se queda igual  a 3
    versions = []
    m_initial = 4
    k_initial = 3
    
    # funcion para ir agregando versiones, m va avanzando 3 en 3 y n 2 en 2
    for i in range(1, 71):
        versions.append(version_generalizada(m_initial, k_initial))
        m_initial += 1
        k_initial += 1
    
    # Funciones que deseas probar
    functions_to_test = [
        ConcertZoo3.sort_aperture,
        ConcertZoo3.sort_rest_of_show,
        ConcertZoo3.most_appearances,
        ConcertZoo3.least_appearances,
        ConcertZoo3.max_grandeur_scene,
        ConcertZoo3.min_grandeur_scene,
        ConcertZoo3.average_grandeur,
    ]

    # for function in functions_to_test:
    header = f"Tiempos de la solución para {ConcertZoo3.average_grandeur.__name__}:"
    times = measure_execution_time(versions, ConcertZoo3.average_grandeur)
    table = tabulate(enumerate(times, start=1), headers=["Ejecución", "Tiempo (s)"], tablefmt="pretty")
    print(f"\n{header}\n{table}")
    
    # Gráfica de tiempos de ejecución
    plot_execution_times(versions, ConcertZoo3.average_grandeur, times)

