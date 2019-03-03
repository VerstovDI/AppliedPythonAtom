#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    size = len(list_of_lists)
    if len(list_of_lists) <= 1:
        return None
    global i
    for i in range(0, size - 1):
        global j
        global k
        for j in range(i + 1, size):
            if len(list_of_lists[j]) != len(list_of_lists):
                return None
            coeff = list_of_lists[j][i] / list_of_lists[i][i]
            for k in range(i, size):
                list_of_lists[j][k] -= list_of_lists[i][k] * coeff

    global res
    res = 1
    for i in range(0, size):
        res *= list_of_lists[i][i]

    return res
    raise NotImplementedError
