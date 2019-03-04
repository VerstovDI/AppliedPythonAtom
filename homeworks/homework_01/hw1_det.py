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
    global t
    t = 0

    if not isinstance(list_of_lists[t], list):
        return None

    if not list_of_lists[0]:
        return None

    for t in range(len(list_of_lists[t])):
        if len(list_of_lists[t]) != len(list_of_lists):
            return None

    swap_cnt = 1

    for i in range(0, size):
        global j
        global k
        global supp_ind
        supp_ind = i
        for j in range(i + 1, size):

            if abs(list_of_lists[j][i]) > abs(list_of_lists[supp_ind][i]):
                supp_ind = j
                fl = True

            else:
                fl = False

            if fl:
                for k in range(0, size):
                    buf = list_of_lists[i][k]
                    list_of_lists[i][k] = list_of_lists[supp_ind][k]
                    list_of_lists[supp_ind][k] = buf
                if i != supp_ind:
                    swap_cnt = -swap_cnt * 1

                else:
                    swap_cnt = -swap_cnt * (-1)

            if list_of_lists[i][i] != 0:
                for j in range(i + 1, size):
                    if isinstance(list_of_lists[j][k], (float, int)) \
                            and isinstance(list_of_lists[i][i], (float, int)):
                        c = -list_of_lists[j][i] / list_of_lists[i][i]
                    else:
                        return None
                    for k in range(size - 1, i - 1, -1):
                        if isinstance(list_of_lists[j][k], (float, int)) \
                                and isinstance(list_of_lists[i][k], (float, int)):
                            list_of_lists[j][k] += list_of_lists[i][k] * c
                        else:
                            return None

    res = 1
    for i in range(0, size):
        res *= list_of_lists[i][i]

    if isinstance(res * swap_cnt, (float, int)):
        return res * swap_cnt
    else:
        return None
    raise NotImplementedError
