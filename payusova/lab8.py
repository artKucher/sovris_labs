from random import randint
import numpy as np


class PageRank:
    page_count = None
    iterations = None

    def __init__(self, page_count=4, iterations=5):
        self.page_count = page_count
        self.iterations = iterations
        self.init_vector = self.get_vector()
        self.init_matrix = self.get_matrix()

    def probability(self):
        try:
            return round(1 / randint(0, self.page_count - 1), 2)
        except ZeroDivisionError:
            return 0

    def get_matrix(self):
        return np.array([[self.probability() for _ in range(self.page_count)] for __ in range(self.page_count)])

    def get_vector(self):
        return np.array([1 / self.page_count for _ in range(self.page_count)])

    def calculate_result(self):
        response_vector = self.init_vector
        for iteration in range(self.iterations):
            response_vector = self.init_matrix @ response_vector
        return response_vector

    def __str__(self):
        response = f"Init matrix: \n{self.init_matrix}\n Init vector: \n{self.init_vector}\n" \
                   f"After {self.iterations} iterations vector of probability will be: \n{self.calculate_result()}"
        return response


if __name__ == '__main__':
    print(str(PageRank()))
