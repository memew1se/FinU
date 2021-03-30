from functools import lru_cache
import numpy as np


class TransitionMatrix:
    """Матрица переходов для определения вероятностей событий"""

    def __init__(self, matrix: np.array):
        self.matrix = matrix

    def __str__(self):
        return "Матрица переходов:\n" + f"{self.matrix}"

    def probability_of_transition(self, n: int) -> np.array:
        """Матрица вероятностей переходов из x в y за n шагов"""
        return np.linalg.matrix_power(self.matrix, n)

    def probability_of_first_transition(self, n: int) -> np.array:
        """Матрица вероятностей первого перехода за n шагов"""

        previous_matrix = np.copy(self.matrix)
        for i in range(n - 1):
            previous_matrix = self.matrix_power_skip(self.matrix, previous_matrix)

        return previous_matrix

    def probability_of_last_transition(self, n: int) -> np.array:
        """Матрица вероятносей перехода не более n шагов"""

        previous_matrix = np.copy(self.matrix)
        res = np.copy(self.matrix)

        for i in range(n - 1):
            previous_matrix = self.matrix_power_skip(self.matrix, previous_matrix)
            res += previous_matrix

        return res

    def probability_of_first_return(self, n: int) -> np.array:
        """Матрица вероятностей первого возвращения на n-ом шаге"""
        matrix = np.copy(self.matrix)

        def first(n_: int) -> np.array:
            return self.probability_of_transition_static(matrix, n_) - \
                   sum([first(i) * self.probability_of_transition_static(matrix, n_ - i) for i in range(1, n_)])

        return np.diagonal(first(n))

    def probability_of_last_return(self, n: int) -> np.array:
        matrix = np.copy(self.matrix)
        result = []

        def first(n_):
            res = self.probability_of_transition_static(matrix, n_) - \
                  sum([first(i) * self.probability_of_transition_static(matrix, n_ - i) for i in range(1, n_)])
            result.append(np.diagonal(res))
            return res

        first(n)

        return sum(result)

    def probability_of_state(self, initial_matrix: np.array, n: int) -> np.array:
        """Матрица вероятностей состояний спустя n шагов"""
        return initial_matrix.dot(np.linalg.matrix_power(self.matrix, n))

    def probability_of_steady_states(self) -> np.array:
        """Установившиеся вероятности"""

        matrix = np.copy(self.matrix).transpose()
        np.fill_diagonal(matrix, np.diagonal(matrix) - 1)
        matrix[-1, :] = 1

        vec = np.zeros(len(matrix))
        vec[-1] = 1

        return np.linalg.inv(matrix).dot(vec)

    def average_time(self) -> float:
        """Среднее время возвращения"""
        matrix = np.copy(self.matrix)
        result = []

        @lru_cache(maxsize=None)
        def first(n_):
            res = self.probability_of_transition_static(matrix, n_) - \
                  sum([first(i) * self.probability_of_transition_static(matrix, n_ - i) for i in range(1, n_)])
            result.append(n_ * np.diagonal(res))
            return res

        first(1000)

        return sum(result)

    def average_steps(self) -> np.array:
        """Среднее количество шагов"""

        previous_matrix = np.copy(self.matrix)
        res = np.copy(self.matrix)

        for i in range(1000):
            previous_matrix = self.matrix_power_skip(self.matrix, previous_matrix)
            res += i * previous_matrix

        return res

    @staticmethod
    def matrix_power_skip(left: np.array, right: np.array) -> np.array:

        r = range(len(left))
        return np.array(
            [[sum(left[i, m] * right[m, j] if m != j else 0 for m in r) for j in r] for i in r])

    @staticmethod
    def probability_of_transition_static(matrix: np.array, n: int) -> np.array:
        return np.linalg.matrix_power(matrix, n)


if __name__ == '__main__':
    transition_matrix = np.array([
        [0.05, 0.41, 0.18, 0.36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0.27, 0.14, 0, 0, 0, 0, 0.27, 0.32, 0, 0, 0, 0, 0, 0],
        [0.22, 0, 0.05, 0.19, 0, 0.36, 0, 0.08, 0.1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0.34, 0.66, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0.42, 0, 0.57, 0, 0.01, 0, 0, 0, 0, 0],
        [0, 0, 0, 0.09, 0.21, 0.22, 0.21, 0, 0, 0.06, 0.21, 0, 0, 0],
        [0, 0, 0, 0, 0.19, 0.22, 0.17, 0.12, 0, 0, 0.3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0.38, 0.56, 0.06, 0, 0, 0, 0, 0],
        [0, 0, 0.12, 0, 0, 0, 0, 0.23, 0.3, 0, 0.27, 0.08, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0.11, 0, 0.41, 0.42, 0, 0.06, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0.31, 0, 0.14, 0.36, 0.19, 0],
        [0, 0, 0, 0, 0, 0.27, 0.33, 0, 0, 0, 0.14, 0.04, 0, 0.22],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.65, 0, 0.35, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.11, 0.36, 0, 0, 0.53]
    ])

    tm = TransitionMatrix(transition_matrix)

    print("Задание 1")
    print(tm)

    # 1) вероятность того, что за 9 шагов система перейдет из состояния 5 в состояние 2
    n = 9
    state1 = 5
    state2 = 2
    print("1)", end=" ")
    print(tm.probability_of_transition(n)[state1 - 1, state2 - 1])

    # 2) вероятности состояний системы спустя 7 шагов, если в начальный момент вероятность состояний были следующими
    # A=(0,07;0,03;0,14;0,14;0,16;0,03;0,06;0,05;0;0,09;0,02;0,15;0;0,06);
    n = 7
    A = np.array([0.07, 0.03, 0.14, 0.14, 0.16, 0.03, 0.06, 0.05, 0, 0.09, 0.02, 0.15, 0, 0.06])
    print("2)", end=" ")
    print(tm.probability_of_state(A, n))

    # 3) вероятность первого перехода за 10 шагов из состояния 12 в состояние 4
    n = 10
    state1 = 12
    state2 = 4
    print("3)", end=" ")
    print(tm.probability_of_first_transition(n)[state1 - 1, state2 - 1])

    # 4) вероятность перехода из состояния 13 в состояние 2 не позднее чем за 8 шагов
    n = 8
    state1 = 13
    state2 = 2
    print("4)", end=" ")
    print(tm.probability_of_last_transition(n)[state1 - 1, state2 - 1])

    # 5) среднее количество шагов для перехода из состояния 7 в состояние 14
    state1 = 7
    state2 = 14
    print("5)", end=" ")
    print(tm.average_steps()[state1 - 1, state2 - 1])

    # 6) вероятность первого возвращения в состояние 6 за 8 шагов
    n = 8
    target_state = 6
    print("6)", end=" ")
    print(tm.probability_of_first_return(n)[target_state - 1])

    # 7) вероятность возвращения в состояние 6 не позднее чем за 6 шагов
    n = 6
    target_state = 6
    print("7)", end=" ")
    print(tm.probability_of_last_transition(n)[target_state - 1])

    # 8) среднее время возвращения в состояние 2
    target_state = 2
    print("8)", end=" ")
    print(tm.average_time()[target_state - 1])

    # 9) Установившиеся состояния
    print("9)", end=" ")
    print(tm.probability_of_steady_states())
