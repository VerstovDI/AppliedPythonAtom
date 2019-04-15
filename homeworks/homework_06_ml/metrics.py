#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    """
    Mean squared error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    if y_true.size() != y_hat.size():
        print("Size of y_true != size of y_hat)
        return -1
    loss = (1 / y_hat.size()) * np.sum((y_true - y_hat)**2)
    return loss


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    if y_true.size() != y_hat.size():
        print("Size of y_true != size of y_hat)
        return -1
    loss = (1 / y_hat) * np.sum(np.abs(y_true - y_hat))
    return loss


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    if y_true.size() != y_hat.size():
        print("Size of y_true != size of y_hat)
        return -1
    loss = 1 - np.sum((y_true - y_ht)**2) / np.sum((y_true - y_hat)**2)
    return loss
