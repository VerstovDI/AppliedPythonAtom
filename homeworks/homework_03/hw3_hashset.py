#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):  # Класс HashMap написан. Просто унаследуем методы
        super().__init__()

    def get(self, key, default_value=None):
        if key in self:
            return True
        else:
            return default_value

    def put(self, key):
        super().put(key, key)

    def __len__(self):
        return super().__len__()

    def values(self):
        return super().values()

    def intersect(self, another_hashset):
        intersection = HashSet()
        for item in another_hashset.values():
            if item in self.values():
                intersection.put(item)
            else:
                continue
        return intersection
