#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        '''
        принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        '''
        """
        Поскольку на вход пришли отсортированные списки, используем кучу.
        Запишем туда кортежи:
        Сами значения и номера списков,из которых будем брать следующий элемент
        """
        output_list = []  # Искомый список
        heap_list = []  # Список для кучи

        """
        Пройдём все элементы (N списков в списке), и воспользуемся тем,
        что он отсортирован: достанем последний элемент - самый большой.
        Временная сложность на данном этапе - O'(N). 
        Запишем кортежи в список для кучи.
        """
        for i, item in enumerate(list_of_lists):
            # item.pop() - достаёт последний элемент списка № i
            heap_tuple = (item.pop(), i)
            # Добавляем кортеж (значение, номер списка) в список для кучи
            heap_list.append(heap_tuple)

        # Создаём кучу tuples_heap из списка для кучи
        tuples_heap = MaxHeap(heap_list)
        # size_lim - максимальная длина формируемого списка
        size_lim = len(output_list)

        # Цикл пока длина сформированного списка не достигнет требуемой
        while tuples_heap.heap and size_lim != k:
            # Извлекаем максимальный элемент кучи, записываем в
            # value значение элемента, в index - номер списка
            value, index = tuples_heap.extract_maximum()
            # Добавляем в формируемый список
            output_list.append(value)
            if list_of_lists[index]:
                tuple_element = (list_of_lists[index].pop(), index)
                tuples_heap.add(tuple_element)
        """
        Поскольку глубина кучи = O(log p), где p - кол-во эл-ов, то в данном случае
        временная сложность составит как раз k прохождений циклов по O(log k), т.е.
        O" = k*O(log k). Т.о., в итоге O = O' + O" = O(N + k*log k), что и требовалось.
        """

        return output_list
