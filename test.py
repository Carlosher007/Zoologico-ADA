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

def version4():
    m = 27
    n = 30
    k = 6

    def crear_n_animales(n):
      letras_disponibles = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
      
      # Verificar que n no sea mayor que la cantidad de letras disponibles
      n = min(n, len(letras_disponibles))

      # Tomar n letras distintas al azar
      letras_seleccionadas = random.sample(letras_disponibles, n)

      # Crear un diccionario de animales con símbolos únicos y grandeza asignada
      animales_creados = {letra: i + 1 for i, letra in enumerate(letras_seleccionadas)}

      return animales_creados

    animals = crear_n_animales(n)
  
    # Crear la apertura con (m-1)*k escenas, donde en cada escena participan 3 animales distintos
    aperture = []
    for i in range(m - 1):
        for j in range(k):
            scene = [list(animals.keys())[x % len(animals)] for x in range(j * 3, (j + 1) * 3)]
            aperture.append(scene)

    # Crear el resto del show con m-1 partes de k escenas cada una, y en cada escena participan 3 animales distintos
    rest_of_show = []
    for i in range(m - 1):
        part = []
        for j in range(k):
            scene = [list(animals.keys())[x % len(animals)] for x in range(j * 3, (j + 1) * 3)]
            part.append(scene)
        rest_of_show.append(part)

    return {'m': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show}
  
def version3():
    m = 18
    n = 21
    k = 6

    # Definir nombres de animales y asignarles números para representar su grandeza
    animals = {
        'An': 1,
        'Bo': 2,
        'Ca': 3,
        'Do': 4,
        'El': 5,
        'Fl': 6,
        'Ga': 7,
        'Ho': 8,
        'Ig': 9,
        'Jo': 10,
        'Ki': 11,
        'La': 12,
        'Mi': 13,
        'Nu': 14,
        'Ow': 15,
        'Pa': 16,
        'Qu': 17,
        'Ro': 18,
        'Sn': 19,
        'Tu': 20,
        'Tr': 20,
    }

    # Crear la apertura con (m-1)*k escenas, donde en cada escena participan 3 animales distintos
    aperture = []
    for i in range(m - 1):
        for j in range(k):
            scene = [list(animals.keys())[x] for x in range(j * 3, (j + 1) * 3)]
            aperture.append(scene)

    # Crear el resto del show con m-1 partes de k escenas cada una, y en cada escena participan 3 animales distintos
    rest_of_show = []
    for i in range(m - 1):
        part = []
        for j in range(k):
            scene = [list(animals.keys())[x] for x in range(j * 3, (j + 1) * 3)]
            part.append(scene)
        rest_of_show.append(part)

    return {'m': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show}


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


def plot_execution_times(versions, function_to_test):
    sizes = [(version['m'] - 1) * version['k'] for version in versions]
    times = measure_execution_time(versions, function_to_test)

    plt.plot(sizes, times, marker='o', label='Actual Performance')
    
    # Añadir línea de ajuste
    z = np.polyfit(sizes, times, 1)
    p = np.poly1d(z)
    plt.plot(sizes, p(sizes), 'r--', label='Fit Line')
    
    

    plt.title('Execution Time vs Input Size for ' + function_to_test.__name__) 
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')

    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    versions = [version1(), version2(), version3(), version4()]
    
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

    for function in functions_to_test:
        header = f"Tiempos de la solución para {function.__name__}:"
        times = measure_execution_time(versions, function)
        table = tabulate(enumerate(times, start=1), headers=["Ejecución", "Tiempo (s)"], tablefmt="pretty")
        print(f"\n{header}\n{table}")
        
        # Gráfica de tiempos de ejecución
        plot_execution_times(versions, function)


