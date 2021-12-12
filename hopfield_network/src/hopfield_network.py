from typing import Optional
import numpy as np


class HopfieldNetwork:
    def __init__(self, max_iter: int = 300):
        """

        :param max_iter: максимальное количество итераций при предсказании одного инстанса
        """
        self.weights: Optional[np.array] = None
        self.dimension: Optional[int] = None
        self.max_iter = max_iter

    def fit(self, sample: np.array) -> 'HopfieldNetwork':
        """

        :param sample: список эталонных образцов, матрица из 1 и -1
        :return: экземпляр обученной модели
        """
        self.dimension = sample.shape[1]
        self.weights = sum(np.outer(instance, instance)/self.dimension for instance in sample) - np.eye(self.dimension)
        return self

    def predict(self, sample: np.array) -> np.array:
        """

        :param sample: объекты, для которых необходимо выполнить предсказания
        :return: список эталонных объектов обучающей выборки, наиболее близких к данным
        """
        result = [self.__predict(instance) for instance in sample]
        return np.array(result, dtype=np.int32)

    def __predict(self, instance: np.array) -> np.array:
        if self.weights is None:
            return None

        current = instance.copy()
        for _ in range(self.max_iter):
            old, current = current, np.array(np.sign(self.weights.dot(current)), dtype=np.int32)
            if np.all(old == current):
                break

        return current
