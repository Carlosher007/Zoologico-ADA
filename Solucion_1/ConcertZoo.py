import math
import random
from Solucion_1.Algorithms_Sol1 import Algorithms, Methods

class ConcertZoo:
    def __init__(self, n, m, k, verification=True):
        """
        Clase que representa un show.

        Args:
            n (int): Número de animales.
            m (int): Número total de partes en el show.
            k (int): Número de escenas en cada parte.
            verification (bool): Indica si se deben realizar verificaciones al agregar elementos (por defecto, True).
        """
        # Inicializar las variables de instancia.
        self.n = n
        self.m = m
        self.k = k
        self.verification = verification
        self.animals = None
        self.aperture = None
        self.rest_of_show = None

    def _verify(self, condition, error_message):
        if self.verification:
            assert condition, error_message

    def add_animals(self, animals):
        """
        Agrega la lista de animales al show.

        Args:
            animals (list): Lista de animales.

        Returns:
            None
        """
        # Verificar que el número de animales sea correcto.
        self._verify(len(animals) == self.n, "El número de animales debe ser igual a n")
        # Guardar los animales.
        self.animals = animals

    def add_aperture(self, aperture):
        """
        Agrega la apertura al show.

        Args:
            aperture (list): Lista de escenas en la apertura.

        Returns:
            None
        """
        # # Verificar que los animales ya se hayan agregado.
        # self._verify(self.animals is not None, "Debe agregar animales antes de la apertura")
        # # Verificar que cada animal en la apertura esté en la lista de animales.
        # self._verify(len(aperture) == (self.m - 1) * self.k, "La apertura debe tener (m-1)*k escenas")
        # # Verificar que el número de escenas en la apertura sea correcto.
        # self._check_animals_in_aperture(aperture)
        # # Guardar la apertura.
        # self.aperture = aperture

        # Verificar que los animales ya se hayan agregado.
        self._verify(self.animals is not None, "Debe agregar animales antes de la apertura")
        # Verificar que cada animal en la apertura esté en la lista de animales.
        self._verify(len(aperture) == (self.m - 1) * self.k, "La apertura debe tener (m-1)*k escenas")
        # Verificar que el número de escenas en la apertura sea correcto.
        self._check_animals_in_aperture(aperture)
        # Guardar la apertura.
        self.aperture = aperture

    def _check_animals_in_aperture(self, aperture):
        """
        Verifica que cada animal en cada escena de la apertura esté en la lista de animales.

        Args:
            aperture (list): Lista de escenas en la apertura.

        Returns:
            None
        """
        for scene in aperture:
          self._verify(all(animal in self.animals for animal in scene), f"Un animal en la apertura no está en la lista de animales")


    def add_rest_of_show(self, rest_of_show):
        """
        Agrega el resto del show al show.

        Args:
            rest_of_show (list): Lista que representa el resto del show.

        Returns:
            None
        """
        # # Verificar que la apertura ya se haya agregado.
        # self._verify(self.aperture is not None, "Debe agregar la apertura antes del resto del show")
        # # Verificar que el número de partes en el resto del show sea correcto.
        # self._verify(len(rest_of_show) == self.m - 1, "Debe haber m-1 partes en el resto del show")
        # # Verificar que cada escena en cada parte del resto del show esté en la apertura.
        # self._check_scenes_in_rest_of_show(rest_of_show)
        # # Verificar que el número de escenas en cada parte del resto del show sea correcto.
        # self._check_number_of_scenes_in_parts(rest_of_show)
        # # Guardar el resto del show.
        # self.rest_of_show = rest_of_show
        # Verificar que la apertura ya se haya agregado.
        # Verificar que la apertura ya se haya agregado.
        self._verify(self.aperture is not None, "Debe agregar la apertura antes del resto del show")
        # Verificar que el número de partes en el resto del show sea correcto.
        self._verify(len(rest_of_show) == self.m - 1, "Debe haber m-1 partes en el resto del show")
        # Verificar que cada escena en cada parte del resto del show esté en la apertura.
        self._check_scenes_in_rest_of_show(rest_of_show)
        # Verificar que el número de escenas en cada parte del resto del show sea correcto.
        self._check_number_of_scenes_in_parts(rest_of_show)
        # Guardar el resto del show.
        self.rest_of_show = rest_of_show

    def _check_scenes_in_rest_of_show(self, rest_of_show):
        """
        Verifica que cada escena en cada parte del resto del show esté en la apertura.

        Args:
            rest_of_show (list): Lista que representa el resto del show.

        Returns:
            None
        """
        # Convertir todas las escenas de la apertura y el resto del show a conjuntos.
        aperture_set = {frozenset(scene) for scene in self.aperture}
        rest_of_show_set = {frozenset(scene) for part in rest_of_show for scene in part}
        # Verificar que cada escena en cada parte del resto del show esté en la apertura.
        self._verify(all(scene_set in aperture_set for scene_set in rest_of_show_set), "Cada escena en las partes debe estar en la apertura")


    def _check_number_of_scenes_in_parts(self, rest_of_show):
        """
        Verifica que el número de escenas en cada parte del resto del show sea correcto.

        Args:
            rest_of_show (list): Lista que representa el resto del show.

        Returns:
            None
        """
        # Verificar que el número de escenas en cada parte del resto del show sea correcto.
        self._verify(all(len(part) == self.k for part in rest_of_show), "Cada parte en el resto del show debe tener k escenas")

    def show_aperture(self):
        """
        Muestra la apertura del show.

        Returns:
            None
        """
        self._show_scenes("Apertura", self.aperture)

    def show_rest_of_show(self):
        """
        Muestra el resto del show.

        Returns:
            None
        """
        self._show_parts("Resto del show", self.rest_of_show)

    def show(self):
        """
        Muestra el show completo.

        Returns:
            None
        """
        # self.show_aperture()
        # self.show_rest_of_show()
        print(f"Apertura {self.aperture}")
        print(f"Resto del show {self.rest_of_show}")
        print()
        
    def _show_scenes(self, title, scenes):
        print(f"{title}:")
        for i, scene in enumerate(scenes, start=1):
            print(f"Escena {i}: {scene}")
        print()
        
    def _show_parts(self, title, parts):
        print(f"{title}:")
        for i, part in enumerate(parts, start=1):
            print(f"Parte {i}:")
            self._show_scenes(f"Escena {i}", part)
        print()
    
    @staticmethod
    def scene_grandness_key(scene, animals):
        """
        Devuelve la suma de las grandezas de los animales en una escena.

        Args:
            scene (list): Escena que contiene animales.
            animals (dict): Diccionario que mapea animales a sus grandezas.

        Returns:
            int: Suma de las grandezas de los animales en la escena.
        """
        return Methods.sum(animals[animal] for animal in scene)

    @staticmethod
    def max_animal_grandness_key(scene, animals):
        """
        Devuelve la máxima grandeza individual de los animales en una escena.

        Args:
            scene (list): Escena que contiene animales.
            animals (dict): Diccionario que mapea animales a sus grandezas.

        Returns:
            int: Máxima grandeza individual en la escena.
        """
        return Methods.max([animals[animal] for animal in scene])

    def random_animal_in_animals(self):
        """
        Devuelve un animal aleatorio de la lista de animales.

        Returns:
            str: Animal aleatorio.
        """
        return random.choice(list(self.animals.keys()))

    @staticmethod
    def scene_grandness_by_animal(animal, animals):
        """
        Devuelve la grandeza de un animal específico.

        Args:
            animal (str): Nombre del animal.
            animals (dict): Diccionario que mapea animales a sus grandezas.

        Returns:
            int: Grandeza del animal.
        """
        return animals[animal]

    @staticmethod
    def part_grandness_key(part, animals):
        """
        Devuelve la suma de las grandezas totales de las escenas en una parte del show.

        Args:
            part (list): Parte del show que contiene escenas.
            animals (dict): Diccionario que mapea animales a sus grandezas.

        Returns:
            int: Suma de las grandezas totales de las escenas en la parte.
        """
        return Methods.sum(ConcertZoo.scene_grandness_key(scene, animals) for scene in part)

    def sort_aperture(self):
        """
        Ordena la apertura del show.

        Returns:
            None
        """
        # Ordenar cada escena de forma ascendente según la grandeza de sus animales.
        for scene in self.aperture:
            Algorithms.merge_sort(scene, 0, len(scene) - 1, self.animals, ConcertZoo.scene_grandness_by_animal)

        # Ordenar cada escena por grandeza total.
        Algorithms.merge_sort(self.aperture, 0, len(self.aperture) - 1, self.animals, key_func=ConcertZoo.scene_grandness_key)

        # Ordenar las escenas por máxima grandeza individual en caso de empate.
        Algorithms.merge_sort(self.aperture, 0, len(self.aperture) - 1, self.animals, key_func=ConcertZoo.max_animal_grandness_key)

    def sort_rest_of_show(self):
        """
        Ordena el resto del show.

        Returns:
            None
        """
        for part in self.rest_of_show:
            # Ordenar cada escena de cada parte de forma ascendente según la grandeza de sus animales.
            for scene in part:
                Algorithms.merge_sort(scene, 0, len(scene) - 1, self.animals, ConcertZoo.scene_grandness_by_animal)

            # Ordenar cada escena por grandeza total.
            Algorithms.merge_sort(part, 0, len(part) - 1, self.animals, key_func=ConcertZoo.scene_grandness_key)

            # Ordenar las escenas por máxima grandeza individual en caso de empate.
            Algorithms.merge_sort(part, 0, len(part) - 1, self.animals, key_func=ConcertZoo.max_animal_grandness_key)

        # Ordenar cada parte por su grandeza total de parte que es la suma de las grandezas totales de la escena.
        Algorithms.merge_sort(self.rest_of_show, 0, len(self.rest_of_show) - 1, self.animals, key_func=ConcertZoo.part_grandness_key)

    def show_sorted_rest_of_show(self):
        """
        Muestra el resto del show después de ordenarlo.

        Returns:
            None
        """
        self.sort_rest_of_show()    
        self.show_rest_of_show()

    def show_sorted_aperture(self):
        """
        Muestra la apertura del show después de ordenarla.

        Returns:
            None
        """
        self.sort_aperture()
        self.show_aperture()

    def show_sorted(self):
        """
        Muestra el show completo después de ordenarlo.

        Returns:
            None
        """
        self.sort_rest_of_show()
        self.sort_aperture()
        self.show()
    
    def most_appearances(self):
        """
        Encuentra el animal o los animales que aparecen en la mayor cantidad de escenas y devuelve el número de apariciones.

        Returns:
            list, int: Lista de animales que aparecen en la mayor cantidad de escenas y el número de apariciones.
        """
        # Paso 1: Inicializar un diccionario vacío para contar las apariciones de cada animal.
        appearances = {}

        # Paso 2: Iterar solo sobre las escenas en la apertura.
        for scene in self.aperture:
            # Paso 3: Para cada escena, iterar sobre todos los animales en la escena.
            for animal in scene:
                # Paso 4: Incrementar el conteo para cada animal en el diccionario en 2 unidades.
                if animal in appearances:
                    appearances[animal] += 2
                else:
                    appearances[animal] = 2

        # Paso 5: Encontrar el número máximo de apariciones.
        max_appearances = Methods.max(list(appearances.values()))

        # Paso 6: Iterar sobre el diccionario y agregar todos los animales con el número máximo de apariciones a una lista.
        most_appearing_animals = [animal for animal, count in appearances.items() if count == max_appearances]

        # Paso 7: Devolver la lista de animales y el número máximo de apariciones.
        return most_appearing_animals, max_appearances

    def least_appearances(self):
        """
        Encuentra el animal o los animales que aparecen en la menor cantidad de escenas y devuelve el número de apariciones.

        Returns:
            list, int: Lista de animales que aparecen en la menor cantidad de escenas y el número de apariciones.
        """
        appearances = {}

        for scene in self.aperture:
            for animal in scene:
                if animal in appearances:
                    appearances[animal] += 2
                else:
                    appearances[animal] = 2

        min_appearances = Methods.min(list(appearances.values()))

        least_appearing_animals = [animal for animal, count in appearances.items() if count == min_appearances]

        return least_appearing_animals, min_appearances

    def max_grandeur_scene(self):
        """
        Encuentra la escena de mayor grandeza total en la apertura.

        Returns:
            list: La escena de mayor grandeza total en la apertura.
        """
        max_grandeur = 0
        max_grandeur_scene = None

        for scene in self.aperture:
            grandeur_sum = ConcertZoo.scene_grandness_key(scene, self.animals)
            if grandeur_sum > max_grandeur:
                max_grandeur = grandeur_sum
                max_grandeur_scene = scene

        return max_grandeur_scene
    
    def min_grandeur_scene(self):
        """
        Encuentra la escena de menor grandeza total en la apertura.

        Returns:
            list: La escena de menor grandeza total en la apertura.
        """
        min_grandeur = float('inf')
        min_grandeur_scene = None

        for scene in self.aperture:
            grandeur_sum = ConcertZoo.scene_grandness_key(scene, self.animals)
            if grandeur_sum < min_grandeur:
                min_grandeur = grandeur_sum
                min_grandeur_scene = scene

        return min_grandeur_scene
    
    def average_grandeur(self):
        """
        Calcula el promedio de grandeza de todo el espectáculo.

        Returns:
            float: Promedio de grandeza de todo el espectáculo.
        """
        total_grandeur = 0

        for scene in self.aperture:
            total_grandeur += 2 * ConcertZoo.scene_grandness_key(scene, self.animals)

        average = total_grandeur / ((self.m - 1) * self.k * 2)
        rounded_average = math.ceil(average * 100) / 100 

        return rounded_average