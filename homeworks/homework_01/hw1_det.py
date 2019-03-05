#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    size = len(list_of_lists)

    if size <= 0 or not list_of_lists[0]:
        return None
    if size == 1:
        if isinstance(list_of_lists[0], list):
            return None
        else:
            return list_of_lists[0]

    global t
    t = 0
    for t in range(len(list_of_lists[t])):
        if len(list_of_lists[t]) != len(list_of_lists):
            return None

    global i
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
                    c = -list_of_lists[j][i] / list_of_lists[i][i]
                    for k in range(size - 1, i - 1, -1):
                        list_of_lists[j][k] += list_of_lists[i][k] * c

    res = 1
    for i in range(0, size):
        res *= list_of_lists[i][i]

    return res * swap_cnt
