import random
import time

import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

from Solucion_1.ConcertZoo import ConcertZoo
# ---------------------------- VARIABLES INICIALES --------------------------- #


def version1 ():
  m = 3
  n = 6
  k = 2

  animals = {
    'Ci': 1,
    'Li': 2,
    'Ga': 3,
    'Pe': 4,
    'Ta': 5,
    'Nu': 6
  }
  aperture = [
    ['Pe', 'Nu', 'Ta'],
    ['Ta', 'Pe', 'Ga'],
    ['Ta', 'Ci', 'Ga'], 
    ['Ga', 'Li', 'Ci'],
  ]
  rest_of_show = [
    [['Ta', 'Ci', 'Ga'], ['Pe', 'Nu', 'Ta']],
    [ ['Ta', 'Pe', 'Ga'], ['Ci', 'Li', 'Ga']],
    ]
  
  return { 'm': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show }

def version2 ():
  m = 4
  n = 9
  k = 3

  animals = {
    'Ca': 1,
    'Lo': 2,
    'Cai': 3,
    'Bo': 4,
    'Co': 5,
    'Ce': 6,
    'Pa': 7,
    'Ti': 8,
    'Le': 9,
  }
  aperture = [
    ['Cai', 'Ca', 'Lo'],
    ['Bo', 'Cai', 'Ca'],
    ['Co', 'Ca', 'Lo'], 
    ['Pa', 'Co', 'Lo'],
    ['Ti', 'Lo', 'Ca'],
    ['Le', 'Cai', 'Lo'],
    ['Le', 'Co', 'Bo'],
    ['Le', 'Pa', 'Ce'],
    ['Ti', 'Ce', 'Pa'],
  ]
  rest_of_show = [
    [['Cai', 'Ca', 'Lo'], ['Ti', 'Lo', 'Ca'], ['Ti', 'Ce', 'Pa']],
    [['Pa', 'Co', 'Lo'], ['Le', 'Pa', 'Ce'], ['Co', 'Ca', 'Lo']],
    [['Bo', 'Cai', 'Ca'], ['Le', 'Cai', 'Lo'], ['Le', 'Co', 'Bo']],
  ]
  
  return { 'm': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show }

def version_generalizada(m, k):
    # n es constante
    n = 9

    # Definir la lista de animales
    animals = {
        'Ca': 1, 'Lo': 2, 'Cai': 3, 'Bo': 4,
        'Co': 5, 'Ce': 6, 'Pa': 7, 'Ti': 8, 'Le': 9,
    }
    
    # Convertir las claves del diccionario en una lista
    animal_keys = list(animals.keys())

    # Inicializar la apertura y el resto del show
    aperture = []
    rest_of_show = []

    # Generar (m-1)*k escenas para la apertura
    for _ in range((m-1)*k):
        scene = random.sample(animal_keys, 3)
        aperture.append(scene)

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
        concert = ConcertZoo(version['n'], version['m'], version['k'])
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
    sizes = [(version['m'] - 1) * version['k'] for version in versions]
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
    m_initial = 2
    k_initial = 1
    
    # funcion para ir agregando versiones, m va avanzando 3 en 3 y n 2 en 2
    for i in range(1, 71):
        versions.append(version_generalizada(m_initial, k_initial))
        m_initial += 2
        k_initial += 1
    
    # Funciones que deseas probar
    functions_to_test = [
        ConcertZoo.sort_aperture,
        ConcertZoo.sort_rest_of_show,
        ConcertZoo.most_appearances,
        ConcertZoo.least_appearances,
        ConcertZoo.max_grandeur_scene,
        ConcertZoo.min_grandeur_scene,
        ConcertZoo.average_grandeur,
    ]

    # for function in functions_to_test:
    header = f"Tiempos de la solución para {ConcertZoo.aver.__name__}:"
    times = measure_execution_time(versions, ConcertZoo.aver)
    table = tabulate(enumerate(times, start=1), headers=["Ejecución", "Tiempo (s)"], tablefmt="pretty")
    print(f"\n{header}\n{table}")
    
    # Gráfica de tiempos de ejecución
    plot_execution_times(versions, ConcertZoo.aver, times)