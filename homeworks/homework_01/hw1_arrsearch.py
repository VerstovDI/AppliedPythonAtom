#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    buf_d = {}  # Создаём пустой словарь
    for cnt in range(0, len(input_list)):  # Перегоняем в словарь поиндексно
        buf_d[input_list[cnt]] = cnt  # Ключ - число, значение - индекс
    t = 0
    for item in input_list:
        temp = buf_d.get(n - item)
        if temp and temp and n - item != item:
            return tuple([t, temp])
        t += 1
    return None
    raise NotImplementedError
