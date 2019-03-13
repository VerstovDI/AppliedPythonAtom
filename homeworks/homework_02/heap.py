#!/usr/bin/env python
# coding: utf-8


class Heap():

    def __init__(self, array):
        self.heaplist = array[::]
        self.build_heap()

    # Ф-ии heapify и sift_up - восстанавливают св-ва кучи
    def heapify(self, i):  # Он же - Sift Down
        l, r = 2 * i + 1, 2 * i + 2  # Левый и правый сыновья соответственно
        # Найдём большего сына (если таковой имеется)
        sz = len(self.heaplist)
        largest = i

        if l < sz and \
                comparator_d(self.heaplist[l], self.heaplist[largest]):
            largest = l
        if r < sz and \
                comparator_d(self.heaplist[r], self.heaplist[largest]):
            largest = r

        if largest != i:  # Проталкиваем в корень большего сына, если он есть
            self.heaplist[i], self.heaplist[largest] = \
                self.heaplist[largest], self.heaplist[i]
            self.heapify(largest)

    def sift_up(self, i):
        while i > 1:
            parent = int((i - 1) / 2)
            if comparator_d(self.heaplist[parent], self.heaplist[i]):
                break
            self.heaplist[i], self.heaplist[parent] = \
                self.heaplist[parent], self.heaplist[i]
            i = parent

    def build_heap(self):  # Функция создания кучи
        sz = len(self.heaplist)
        for i in range(sz, -1, -1):
            self.heapify(i)

    def getHeap(self):  # Геттер для кучи
        return self.heaplist

    def add(self, elem_with_priority):  # Функция добавления эл-та в кучу
        self.heaplist.append(elem_with_priority)
        sz = len(self.heaplist)
        self.sift_up(sz - 1)


class MaxHeap(Heap):  # Потомок класса Heap

    def __init__(self, array):
        super(MaxHeap, self).__init__(array)

    def extract_maximum(self):  # Возвращает максимальный элемент из кучи,
        if len(self.heaplist):  # перестраивая кучу после извлечения
            max = self.heaplist.pop(0)
            self.build_heap()
            return max


# Вспомогательные ф-ии (приведены ниже)
def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
