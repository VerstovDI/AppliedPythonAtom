#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    '''
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''
    """
    Поскольку необходимо время O(len(input_list)),
    логично воспользоваться хэш-таблицей (время доступа!) -> словарь
    Данный алгоритм выполняетcя за требуемое время,
    однако вместе с тем необходимо памяти также O(len(input_list))
       1) Скопируем массив в словарь
       2) Будем проходить массив и оценивать n - input_list[i]
    """
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
