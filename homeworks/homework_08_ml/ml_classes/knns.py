#!/usr/bin/env python
# coding: utf-8


import numpy as np
from sklearn.preprocessing import StandardScaler


class KNNRegressor:
    """
    Построим регрессию с помощью KNN. Классификацию писали на паре
    """

    def __init__(self, n):
        '''
        Конструктор
        :param n: число ближайших соседей, которые используются
        '''
        self._n = n

    def fit(self, X, y):
        '''
        :param X: обучающая выборка,
        матрица размерности (num_obj, num_features)
        :param y: целевая переменная,
        матрица размерности (num_obj, 1)
        :return: None
        '''
        self._X = X
        self._y = y

    def predict(self, X):
        '''
        :param X: выборка, на которой
        хотим строить предсказания (num_test_obj, num_features)
        :return: вектор предсказаний, матрица размерности (num_test_obj, 1)
        '''
        std_scaler = StandardScaler()
        X_norm = std_scaler.fit_transform(X)

        y = []
        assert len(X_norm.shape) == 2
        for curr in X_norm:
            # Посчитаем расстояние от всех элементов в тренировочной выборке
            # до текущего примера -> результат - вектор размерности трейна
            dist = np.sum(np.sqrt((self._X - curr)**2, axis=1))
            # Возьмем индексы n элементов, расстояние до которых минимально
            # результат -> вектор из n элементов
            idx = np.argsort(dist)[:self._n]
            q = 1/dist[idx]  # Взвешенный способ
            prediction = np.average(self._y[idx], weights=q)
            y.append(prediction)
        self.is_fitted = True
        return y

