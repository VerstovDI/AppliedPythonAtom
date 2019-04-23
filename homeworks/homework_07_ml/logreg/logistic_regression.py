#!/usr/bin/env python
# coding: utf-8


# Использовал:
#  1) https://becominghuman.ai/
#  2) http://www.machinelearning.ru/wiki/
#  3) http://easydan.com/arts/2016/logreg-scikitlearn/
#  4) https://habr.com/ru/company/ods/blog/322076/
#  5) Слайды презентации
#  6) Часть узнал и спросил у товарища по проекту:
#         https://github.com/Kinetikm/AppliedPythonAtom/pull/363


class LogisticRegression:
    def __init__(self, lambda_coef=1.0, regularization=None, alpha=0.5):
        """
        LogReg for Binary case
        :param lambda_coef: constant coef for gradient descent step
        :param regularization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        :attr: is trained: fitted or not
        :attr: _w: curr weights
        """
        self.lambda_coef = lambda_coef
        self.regularization = regularization
        self.alpha = alpha
        self.is_trained = False
        self._w = None

    def sigmoid(self, z):  # f(x)
        return 1/1+np.exp(-z)

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        # Sizes check
        if X_train.shape[0] != y_train.shape[0]:
            raise Exception("Size mismatch")
        # Введём константу для градиентного спуска
        eps = 1e-8
        # Кол-во итерация для метода градиентного спуска
        iterations = 5000
        # Cоздадим матрицу x-ов + единичный столбец в конце
        X_train_new = np.hstack([np.ones(X_train.shape[0]), X_train])
        self._w = np.zeros(X_train_new.shape[1])

        for _ in range(iterations):  # Регуляризация
            if self.regularization == "L1":
                coef_regul = self.alpha * np.abs(self._w)
            elif self.regularization == "L2":
                coef_regul = self.alpha * (np.abs(self._w))**2
            else:
                coef_regul = 0

        prediction = self.predict_proba(X_train).T
        y_train = y_train.T

        # Здесь сам градиентный спуск в направлении антиградиента,
        # исп. eps., iterations раз
        # self._w -= ...

        self.is_trained = True  # Модель обучена. Возращаем рез-т
        return self

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        if self.is_trained is False:
            raise Exception("Model is not fitted. Do it first, please!")
        thresh = 0.5  # Порог, после которого мы говорим, что 1, до - 0

        X_test_new = np.hstack([np.ones(X_train.shape[0]), X_test])
        z = X_test_new.dot(self._w)
        prob = sigmoid(z)
        prob_classes = [0, 1]
        if 0 <= prob < thresh:
            return prob_classes[0]
        else:
            if thresh <= prob <= 1:
                return prob_classes[1]
            else:
                raise Exception("Something goes wrong")

    def predict_proba(self, X_test):
        """
        Predict probability using model.
        :param X_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        X_test_new = np.hstack([X_test, np.ones((X_test.shape[0], 1))])
        z = X_test_new.dot(self._w).T
        res = sigmoid(z)
        return res

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        try:
            return self._w
        except:
            raise Exception("Model is not fitted")
