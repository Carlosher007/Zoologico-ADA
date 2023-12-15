# ---------------------------------------------------------------------------- #
#                                  SOLUCIÓN 1                                  #
# ---------------------------------------------------------------------------- #

# --------- INFORMACIÓN ACERCA DE LAS ESTRUCTURAS DE DATOS A UTILIZAR -------- #
# Para almacenar la información de los animales se utilizará un diccionario
# Para almacenar las escenas se utilizaran las listas. Cada escena será una lista de 3 elementos
# Para almacenar las partes se utilizaran las listas. Cada parte será una lista de escenas

# -------------- INFORMACIÓN ACERCA DE LOS ALGORITMOS A UTILIZAR ------------- #
# Para ordenar las escenas y las partes podemos utilizar el algoritmo de ordenamiento por mezcla (merge sort) con algunas modificaciones, las cuales no afectaran la complejidad del algoritmo


import random
from Solucion_1.ConcertZoo import ConcertZoo
from Solucion_2.ConcertZoo2 import ConcertZoo2
from Solucion_3.ConcertZoo3 import ConcertZoo3

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

def version3():
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
  
def version4():
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



# ---------------------------------------------------------------------------- #
#                                  SOLUCIÓN 2                                #
# ---------------------------------------------------------------------------- #

# --------- INFORMACIÓN ACERCA DE LAS ESTRUCTURAS DE DATOS A UTILIZAR -------- #
# Para almacenar la información de los animales se utilizará un diccionario
# Para almacenar las escenas se utilizaran las listas. Cada escena será una lista de 3 elementos
# Para almacenar las partes se utilizaran las listas. Cada parte será una lista de escenas

# -------------- INFORMACIÓN ACERCA DE LOS ALGORITMOS A UTILIZAR ------------- #
# Para ordenar las escenas y las partes podemos utilizar el algoritmo de ordenamiento por mezcla (merge sort) con algunas modificaciones, las cuales no afectaran la complejidad del algoritmo

# ---------------------------- VARIABLES INICIALES --------------------------- #

def version1_sol2():
    m = 3
    n = 6
    k = 2

    animals = [
        ('Ci', 1),
        ('Li', 2),
        ('Ga', 3),
        ('Pe', 4),
        ('Ta', 5),
        ('Nu', 6)
    ]

    aperture = [
        ['Pe', 'Nu', 'Ta'],
        ['Ta', 'Pe', 'Ga'],
        ['Ta', 'Ci', 'Ga'],
        ['Ga', 'Li', 'Ci'],
    ]

    rest_of_show = [
        [['Ta', 'Ci', 'Ga'], ['Pe', 'Nu', 'Ta']],
        [['Ta', 'Pe', 'Ga'], ['Ci', 'Li', 'Ga']],
    ]

    return {'m': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show}


def version2_sol2():
    m = 4
    n = 9
    k = 3

    animals = [
        ('Ca', 1),
        ('Lo', 2),
        ('Cai', 3),
        ('Bo', 4),
        ('Co', 5),
        ('Ce', 6),
        ('Pa', 7),
        ('Ti', 8),
        ('Le', 9),
    ]

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

    return {'m': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show}

def version3_sol2():
    m = 27
    n = 30
    k = 6

    def crear_n_animales(n):
        letras_disponibles = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        
        # Verificar que n no sea mayor que la cantidad de letras disponibles
        n = min(n, len(letras_disponibles))

        # Tomar n letras distintas al azar
        letras_seleccionadas = random.sample(letras_disponibles, n)

        # Crear una lista de tuplas de animales con símbolos únicos y grandeza asignada
        animales_creados = [(letra, i + 1) for i, letra in enumerate(letras_seleccionadas)]

        return animales_creados

    animals = crear_n_animales(n)
  
    # Crear la apertura con (m-1)*k escenas, donde en cada escena participan 3 animales distintos
    aperture = []
    for i in range(m - 1):
        for j in range(k):
            scene = [animals[x % len(animals)][0] for x in range(j * 3, (j + 1) * 3)]
            aperture.append(scene)

    # Crear el resto del show con m-1 partes de k escenas cada una, y en cada escena participan 3 animales distintos
    rest_of_show = []
    for i in range(m - 1):
        part = []
        for j in range(k):
            scene = [animals[x % len(animals)][0] for x in range(j * 3, (j + 1) * 3)]
            part.append(scene)
        rest_of_show.append(part)

    return {'m': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show}
  
def version4_sol2():
    m = 18
    n = 21
    k = 6

    # Definir nombres de animales y asignarles números para representar su grandeza
    animals = [
        ('An', 1),
        ('Bo', 2),
        ('Ca', 3),
        ('Do', 4),
        ('El', 5),
        ('Fl', 6),
        ('Ga', 7),
        ('Ho', 8),
        ('Ig', 9),
        ('Jo', 10),
        ('Ki', 11),
        ('La', 12),
        ('Mi', 13),
        ('Nu', 14),
        ('Ow', 15),
        ('Pa', 16),
        ('Qu', 17),
        ('Ro', 18),
        ('Sn', 19),
        ('Tu', 20),
        ('Tr', 20),
    ]

    # Crear la apertura con (m-1)*k escenas, donde en cada escena participan 3 animales distintos
    aperture = []
    for i in range(m - 1):
        for j in range(k):
            scene = [animals[x][0] for x in range(j * 3, (j + 1) * 3)]
            aperture.append(scene)

    # Crear el resto del show con m-1 partes de k escenas cada una, y en cada escena participan 3 animales distintos
    rest_of_show = []
    for i in range(m - 1):
        part = []
        for j in range(k):
            scene = [animals[x][0] for x in range(j * 3, (j + 1) * 3)]
            part.append(scene)
        rest_of_show.append(part)

    return {'m': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show}

# /////////////////////////
def version1_sol3():
    m = 3
    n = 6
    k = 2

    animals = [
        ['Ci', 1],
        ['Li', 2],
        ['Ga', 3],
        ['Pe', 4],
        ['Ta', 5],
        ['Nu', 6]
    ]

    aperture = [
        ['Pe', 'Nu', 'Ta'],
        ['Ta', 'Pe', 'Ga'],
        ['Ta', 'Ci', 'Ga'],
        ['Ga', 'Li', 'Ci'],
    ]

    rest_of_show = [
        [['Ta', 'Ci', 'Ga'], ['Pe', 'Nu', 'Ta']],
        [['Ta', 'Pe', 'Ga'], ['Ci', 'Li', 'Ga']],
    ]

    return {'m': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show}

def version2_sol3():
    m = 4
    n = 9
    k = 3

    animals = [
        ['Ca', 1],
        ['Lo', 2],
        ['Cai', 3],
        ['Bo', 4],
        ['Co', 5],
        ['Ce', 6],
        ['Pa', 7],
        ['Ti', 8],
        ['Le', 9],
    ]

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

    return {'m': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show}

def version3_sol3():
    m = 27
    n = 30
    k = 6

    # def crear_n_animales(n):
    #     letras_disponibles = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    #     n = min(n, len(letras_disponibles))

    #     letras_seleccionadas = random.sample(letras_disponibles, n)

    #     animales_creados = [[letra, i + 1] for i, letra in enumerate(letras_seleccionadas)]

    #     return animales_creados

    # animals = crear_n_animales(n)

    # aperture = []
    # for i in range(m - 1):
    #     for j in range(k):
    #         scene = [list(animals[x]) for x in range(j * 3, (j + 1) * 3)]
    #         aperture.append(scene)

    # rest_of_show = []
    # for i in range(m - 1):
    #     part = []
    #     for j in range(k):
    #         scene = [list(animals[x]) for x in range(j * 3, (j + 1) * 3)]
    #         part.append(scene)
    #     rest_of_show.append(part)

    # return {'m': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show}
    def crear_n_animales(n):
        letras_disponibles = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

        n = min(n, len(letras_disponibles))

        letras_seleccionadas = random.sample(letras_disponibles, n)

        animales_creados = [[letra, i + 1] for i, letra in enumerate(letras_seleccionadas)]

        return animales_creados

    animals = crear_n_animales(n)

    aperture = []
    for i in range(m - 1):
        scene = [list(animals[x]) for x in range(i * 3, min((i + 1) * 3, n))]
        aperture.append(scene)

    rest_of_show = []
    for i in range(m - 1):
        part = []
        for j in range(k):
            scene = [list(animals[x]) for x in range((i * k + j) * 3, min((i * k + j + 1) * 3, n))]
            part.append(scene)
        rest_of_show.append(part)

    return {'m': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show}

def version4_sol3():
    m = 18
    n = 21
    k = 6

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
        ['Jo', 10],
        ['Ki', 11],
        ['La', 12],
        ['Mi', 13],
        ['Nu', 14],
        ['Ow', 15],
        ['Pa', 16],
        ['Qu', 17],
        ['Ro', 18],
        ['Sn', 19],
        ['Tu', 20],
        ['Tr', 20],
    ]

    aperture = []
    for i in range(m - 1):
        for j in range(k):
            scene = [list(animals[x]) for x in range(j * 3, (j + 1) * 3)]
            aperture.append(scene)

    rest_of_show = []
    for i in range(m - 1):
        part = []
        for j in range(k):
            scene = [list(animals[x]) for x in range(j * 3, (j + 1) * 3)]
            part.append(scene)
        rest_of_show.append(part)

    return {'m': m, 'n': n, 'k': k, 'animals': animals, 'aperture': aperture, 'rest_of_show': rest_of_show}

def solution_1 (version):
  concert = ConcertZoo( version['n'], version['m'], version['k'] )
  concert.add_animals( version['animals'] )
  concert.add_aperture( version['aperture'] )
  concert.add_rest_of_show( version['rest_of_show'])

  concert.show()

  concert.show_sorted()
  
  # EL que participo mas veces
  most_appearing_animals, max_appearances = concert.most_appearances()
  print(f"Animales que aparecen en la mayor cantidad de escenas: {most_appearing_animals}")
  print(f"Número de apariciones: {max_appearances}")
  print()
  
  # El que participo menos veces
  least_appearing_animals, min_appearances = concert.least_appearances()
  print(f"Animales que aparecen en la menor cantidad de escenas: {least_appearing_animals}")
  print(f"Número de apariciones: {min_appearances}")
  print()
  
  # La escena de mayor grandeza
  max_grandeur_scene = concert.max_grandeur_scene()
  print(f"Escena de mayor grandeza: {max_grandeur_scene}")

  # La escena de menor grandeza
  min_grandeur_scene = concert.min_grandeur_scene()
  print(f"Escena de menor grandeza: {min_grandeur_scene}")
  
  # La grandeza promedio de todo el espectaculo
  average_grandeur = concert.average_grandeur()
  print(f"Grandeza promedio de todo el espectaculo: {average_grandeur}")

def solution_2 (version):
  concert = ConcertZoo2( version['n'], version['m'], version['k'] )
  concert.add_animals( version['animals'] )
  concert.add_aperture( version['aperture'] )
  concert.add_rest_of_show( version['rest_of_show'])

  concert.show()

  concert.show_sorted()
  
  # EL que participo mas veces
  most_appearing_animals, max_appearances = concert.most_appearances()
  print(f"Animales que aparecen en la mayor cantidad de escenas: {most_appearing_animals}")
  print(f"Número de apariciones: {max_appearances}")
  print()
  
  # El que participo menos veces
  least_appearing_animals, min_appearances = concert.least_appearances()
  print(f"Animales que aparecen en la menor cantidad de escenas: {least_appearing_animals}")
  print(f"Número de apariciones: {min_appearances}")
  print()
  
  # La escena de mayor grandeza
  max_grandeur_scene = concert.max_grandeur_scene()
  print(f"Escena de mayor grandeza: {max_grandeur_scene}")

  # La escena de menor grandeza
  min_grandeur_scene = concert.min_grandeur_scene()
  print(f"Escena de menor grandeza: {min_grandeur_scene}")
  
  # La grandeza promedio de todo el espectaculo
  average_grandeur = concert.average_grandeur()
  print(f"Grandeza promedio de todo el espectaculo: {average_grandeur}")

def solution_3 (version):
  concert = ConcertZoo3( version['n'], version['m'], version['k'] )
  concert.add_animals( version['animals'] )
  concert.add_aperture( version['aperture'] )
  concert.add_rest_of_show( version['rest_of_show'])

  concert.show()

  concert.show_sorted()
  
  # EL que participo mas veces
  most_appearing_animals, max_appearances = concert.most_appearances()
  print(f"Animales que aparecen en la mayor cantidad de escenas: {most_appearing_animals}")
  print(f"Número de apariciones: {max_appearances}")
  print()
  
  # El que participo menos veces
  least_appearing_animals, min_appearances = concert.least_appearances()
  print(f"Animales que aparecen en la menor cantidad de escenas: {least_appearing_animals}")
  print(f"Número de apariciones: {min_appearances}")
  print()
  
  # La escena de mayor grandeza
  max_grandeur_scene = concert.max_grandeur_scene()
  print(f"Escena de mayor grandeza: {max_grandeur_scene}")

  # La escena de menor grandeza
  min_grandeur_scene = concert.min_grandeur_scene()
  print(f"Escena de menor grandeza: {min_grandeur_scene}")
  
  # La grandeza promedio de todo el espectaculo
  average_grandeur = concert.average_grandeur()
  print(f"Grandeza promedio de todo el espectaculo: {average_grandeur}")

if __name__ == "__main__":
    solution =3
    version = 3
    if(solution == 1):
        if(version == 1):
            solution_1(version1() )
        elif(version == 2):
            solution_1(version2())
        elif(version == 3):
            solution_1(version3())
        elif(version == 4):
            solution_1(version4())
    elif(solution == 2):
        if(version == 1):
            solution_2(version1_sol2() )
        elif(version == 2):
            solution_2(version2_sol2())
        elif(version == 3):
            solution_2(version3_sol2())
        elif(version == 4):
            solution_2(version4_sol2())
    elif(solution == 3):
        if(version == 1):
            solution_3(version1_sol3() )
        elif(version == 2):
            solution_3(version2_sol3())
        elif(version == 3):
            solution_3(version3_sol3())
        elif(version == 4):
            solution_3(version4_sol3())
    