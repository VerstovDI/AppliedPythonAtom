#!/usr/bin/env python
# coding: utf-8


import numpy as np
from sklearn.metrics import mean_squared_error as mse


class DecisionStumpRegressor:
    """
    Класс, реализующий решающий пень (дерево глубиной 1)
    для регрессии. Ошибка в смысле MSE.
    """

    def __init__(self):
        """
        th - порог
        y1, y2 - ответы для x<= th и x > th соответственно
        is_fitted - обучена ли модель
        """
        self._th = None
        self._y1 = None
        self._y2 = None
        self.is_fitted = False

    def fit(self, X, y):
        """
        Метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        """
        assert np.shape(X) == np.shape(y), "Sizes are not equal!"
        if X.shape[1] < 1 or y.shape[1] < 1:
            raise Exception("Incorrect input")
        """
        https://people.csail.mit.edu/dsontag/courses/ml16/slides/lecture11.pdf
        """
        basic_mse = mse(y, np.mean(y))
        for it in range(X[1] - 1):
            th = (X[it + 1] + X[it]) / 2
            left_part, right_part = y[:it + 1], y[it + 1:]
            left_part_mse = mse(y, np.mean(left_part))
            right_part_mse = mse(y, np.mean(right_part))
            cur_mse = left_part_mse + right_part_mse
            if basic_mse > cur_mse:
                self._th = th
                self._y1, self._y2 = np.mean(left_part), np.mean(right_part)
                basic_mse = cur_mse
        self.is_fitted = True
        return None

    def predict(self, X):
        """
        Метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        """
        if self.is_fitted is False:
            raise Exception("The model is not fitted")
        if X.shape[1] < 1:
            raise Exception("Incorrect input")
        pred_arr = list()
        for it in X:
            if it <= self._th:
                pred_arr.append(self._y1)
            else:
                pred_arr.append(self._y2)
        return pred_arr
