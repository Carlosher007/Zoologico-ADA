import random
from Solucion_3.ConcertZoo3 import ConcertZoo3

def version1_solution3 ():
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

def version2_solution3 ():
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

def version3_solution3():
    m = 6
    n = 9
    k = 3

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

def version4_solution3():
    m = 18
    n = 21
    k = 6

    # Definir nombres de animales y asignarles números para representar su grandeza
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
        ['Tr', 21],
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
