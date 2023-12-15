class Algorithms:
    @staticmethod
    def merge(list_to_be_sorted: list, left: int, middle: int, right: int, animal_grandezas: dict, key_func) -> None:
        """
        Merge function for the Merge Sort algorithm.

        Args:
            list_to_be_sorted (list): List to be sorted.
            left (int): Left index of the subarray.
            middle (int): Middle index of the subarray.
            right (int): Right index of the subarray.
            animal_grandezas (dict): Dictionary containing animal sizes.
            key_func: Function to extract the key for comparison.

        Returns:
            None
        """
        n_left: int = middle - left + 1
        n_right: int = right - middle

        left_list: list = [None for _ in range(n_left)]
        right_list: list = [None for _ in range(n_right)]

        for i in range(n_left):
            left_list[i] = list_to_be_sorted[left + i]

        for j in range(n_right):
            right_list[j] = list_to_be_sorted[middle + 1 + j]

        i: int = 0
        j: int = 0
        k: int = left

        while i < n_left and j < n_right:
            if key_func(left_list[i], animal_grandezas) <= key_func(right_list[j], animal_grandezas):
                list_to_be_sorted[k] = left_list[i]
                i += 1
            else:
                list_to_be_sorted[k] = right_list[j]
                j += 1
            k += 1

        while i < n_left:
            list_to_be_sorted[k] = left_list[i]
            i += 1
            k += 1

        while j < n_right:
            list_to_be_sorted[k] = right_list[j]
            j += 1
            k += 1

    @staticmethod
    def merge_sort(list_to_be_sorted: list, left: int, right: int, animal_grandezas: dict, key_func) -> None:
        """
        Merge Sort algorithm.

        Args:
            list_to_be_sorted (list): List to be sorted.
            left (int): Left index of the subarray.
            right (int): Right index of the subarray.
            animal_grandezas (dict): Dictionary containing animal sizes.
            key_func: Function to extract the key for comparison.

        Returns:
            None
        """
        if left < right:
            middle: int = (left + right) // 2

            Algorithms.merge_sort(list_to_be_sorted, left, middle, animal_grandezas, key_func)       # T(n/2)
            Algorithms.merge_sort(list_to_be_sorted, middle + 1, right, animal_grandezas, key_func)  # T(n/2)

            Algorithms.merge(list_to_be_sorted, left, middle, right, animal_grandezas, key_func)     # O(n)

    @staticmethod
    def counting_sort(n: int, list_to_be_sorted: list, criterion: int, k: int):
        """
        Counting Sort algorithm.

        Args:
            n (int): Size of the list.
            list_to_be_sorted (list): List to be sorted.
            criterion (int): Criterion for sorting.
            k (int): Range of values for the criterion.

        Returns:
            list: Sorted list.
        """
        relative_frequency = [0] * k
        sorted_list = [None] * n

        for element in list_to_be_sorted:
            relative_frequency[element[criterion] - 1] += 1

        for i in range(1, k):
            relative_frequency[i] += relative_frequency[i - 1]

        for i in range(n - 1, -1, -1):
            sorted_list[relative_frequency[list_to_be_sorted[i][criterion] - 1] - 1] = list_to_be_sorted[i]
            relative_frequency[list_to_be_sorted[i][criterion] - 1] -= 1

        return sorted_list


class Methods:
    @staticmethod
    def len(list: list) -> int:
        """
        Get the length of a list.

        Args:
            list (list): Input list.

        Returns:
            int: Length of the list.
        """
        length = 0

        for _ in list:
            length += 1
        return length

    @staticmethod
    def sum(numbers: list) -> 'number':
        """
        Calculate the sum of a list of numbers.

        Args:
            numbers (list): List of numbers.

        Returns:
            'number': Total sum.
        """
        total = 0

        for number in numbers:
            total += number
        return total

    @staticmethod
    def max(list: list) -> 'number':
        """
        Find the maximum element in a list of numbers.

        Args:
            list (list): List of numbers.

        Returns:
            'number': Maximum element.
        """
        max_element = list[0]

        for i in range(Methods.len(list)):
            if list[i] > max_element:
                max_element = list[i]
        return max_element
    
    def min(list: list) -> 'number':
        """
        Find the minimum element in a list of numbers.

        Args:
            list (list): List of numbers.

        Returns:
            'number': Minimum element.
        """
        min_element = list[0]

        for i in range(Methods.len(list)):
            if list[i] < min_element:
                min_element = list[i]
        return min_element

    @staticmethod
    def reverse(list: list) -> list:
        """
        Reverse a list.

        Args:
            list (list): Input list.

        Returns:
            list: Reversed list.
        """
        reversed_list = []

        for i in range(Methods.len(list) - 1, 0, -1):
            reversed_list.append(list[i])
        return reversed_list

    @staticmethod
    def zip(list1, list2) -> list:
        """
        Zip two lists together.

        Args:
            list1: First list.
            list2: Second list.

        Returns:
            list: Zipped list of tuples.
        """
        return [(list1[i], list2[i]) for i in range(Methods.len(list1))]
