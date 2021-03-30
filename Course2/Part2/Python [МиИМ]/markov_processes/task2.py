import numpy as np


class QueueBranch:
    """Система массового обслуживания для рассчета вероятностей событий"""

    def __init__(self, l: int, m: int, u: int, n: int):
        self.l = l
        self.m = m
        self.u = u
        self.n = n

        s = m + n
        matrix = np.zeros((s + 1, s + 1))
        np.fill_diagonal(matrix[:, 1:], l)
        np.fill_diagonal(matrix[1:, :], [*[i * u for i in range(1, m)], *[m * u for j in range(n + 1)]])

        self.matrix = matrix

    def __str__(self):
        return f"lambda={self.l}\n" + f"m={self.m}\n" + f"u={self.u}\n" + f"n={self.n}\n" + f"{self.matrix}"

    def probability_of_steady_states(self):
        """Установившиеся вероятности"""

        matrix = np.copy(self.matrix).transpose()
        s = len(self.matrix)

        np.fill_diagonal(matrix, [(-1) * sum(matrix[:, i]) for i in range(s)])
        matrix[-1, :] = 1

        vector = np.zeros(s)
        vector[-1] = 1

        return np.linalg.inv(matrix).dot(vector)

    def service_intensity(self) -> tuple:
        """Относительная и абсолютная иненсивность обслуживания"""

        relative = 1 - self.probability_of_failure()
        absolute = relative * self.l

        return relative, absolute

    def probability_of_failure(self) -> float:
        """Вероятность отказа в обслуживании"""
        return self.probability_of_steady_states()[-1]

    def probability_of_skip(self) -> float:
        """Вероятность, что поступающая заявка не будет ждать в очереди"""
        return sum(self.probability_of_steady_states()[:self.m])

    def average_length(self) -> float:
        """Средняя длина в очереди"""
        return sum((i * self.probability_of_steady_states()[self.m + i]) for i in range(1, self.n + 1))

    def average_time(self) -> float:
        """Среднее время в очереди"""
        return sum(((i + 1) / (self.m * self.u) *
                    self.probability_of_steady_states()[self.m + i]) for i in range(self.n))

    def average_busy_channels(self) -> float:
        """Среднее число занятых каналов"""
        return (sum((i * self.probability_of_steady_states()[i]) for i in range(1, self.m + 1)) +
                sum((self.m * self.probability_of_steady_states()[i]) for i in range(self.m + 1, self.m + self.n + 1)))

    def average_wait_time(self) -> float:
        """Среднее время простоя системы массового обслуживания"""

        res = 1 / np.sum(self.matrix, axis=1)
        return res[0]


if __name__ == '__main__':
    qb = QueueBranch(25, 6, 5, 6)
    print(qb)

    # a) Найдите установившиеся вероятности состояний.
    print("a)", end=" ")
    print(qb.probability_of_steady_states())

    # b) Найдите вероятность отказа в обслуживании
    print("b)", end=" ")
    print(qb.probability_of_failure())

    # c) Найдите относительную и абсолютную интенсивность обслуживания
    print("c)", end=" ")
    print(qb.service_intensity())

    # d) Найдите среднюю длину в очереди
    print("d)", end=" ")
    print(qb.average_length())

    # e) Найдите среднее время в очереди
    print("e)", end=" ")
    print(qb.average_time())

    # f) Найдите среднее число занятых каналов
    print("f)", end=" ")
    print(qb.average_busy_channels())

    # g) Найдите вероятность того, что поступающая заявка не будет ждать в очереди
    print("g)", end=" ")
    print(qb.probability_of_skip())

    # h) Найти среднее время простоя системы массового обслуживания
    print("h)", end=" ")
    print(qb.average_wait_time())
