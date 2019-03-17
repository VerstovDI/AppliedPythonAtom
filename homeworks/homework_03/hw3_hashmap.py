#!/usr/bin/env python
# coding: utf-8


class HashMap:
    # Информацию необходимо скрывать и защищать. Поэтому __ для атрибутов
    __CONST_THRESHOLD = 0.75  # Константа - предел заполненности HashMap

    class Entry:  # Данные необходимо скрывать и защищать. Поэтому __
        def __init__(self, key, value):
            self.__hkey = key  # Ключ Entry
            self.__hval = value  # Значение Entry

        def get_key(self):  # Геттер ключа
            return self.__hkey

        def get_value(self):  # Геттер значения
            return self.__hval

        def set_value(self, value):  # Cеттер значения
            self.__hval = value

        def __eq__(self, other):  # Cравнение по ключу
            return self.get_key() == other.get_key()

    def __init__(self, bucket_num=64):
        self.__cur_sz = bucket_num  # Текущий размер HashMap
        # Структура: cписок списков Entry
        self.__htable = [[] for i in range(self.__cur_sz)]
        self.__buckets = 0  # Количество непустых ячеек (bucket's)
        # Процент заполненности таблицы.
        # Если (self.__load_factor >= __CONST_THRESHOLD) -> resize
        self.__load_factor = self.__buckets / self.__cur_sz

    def get(self, key, default_value=None):  # Возвращает значение по ключу
        ind = self._get_index(self._get_hash(key))
        if ind is None:
            return default_value
        else:
            for item in self.__htable[ind]:
                if item.get_key() == key:
                    return item.get_value()
        return default_value

    def put(self, key, value):  # Вставка в HashMap
        ind = self._get_index(self._get_hash(key))
        if ind is not None:
            fl = False
            for item in self.__htable[ind]:
                if item.get_key() == key:
                    item.set_value(value)
                    fl = True
                    break
            if fl is False:
                self.__htable[ind].append(self.Entry(key, value))
                self.__buckets += 1
        else:
            print("Invalid key")
        if self.__load_factor >= self.__CONST_THRESHOLD:
            self._resize()

    def __len__(self):  # Возвращает длину списка списков (Hash table)
        return self.__buckets

    def _get_hash(self, key):  # Возвращает хэш (встроенная хэш-ф-я)->int
        return hash(key)

    def _get_index(self, hash_value):  # Возвращает индекс по хэшу
        return hash_value % self.__cur_sz

    def values(self):  # Итератор значений
        __values = list()
        for bucket in self.__htable:
            for it in bucket:
                __values.append(it.get_value())
        return __values

    def keys(self):  # Итератор ключей
        __keys = list()
        for bucket in self.__htable:
            for it in bucket:
                __keys.append(it.get_key())
        return __keys

    def items(self):  # Итератор пар ключ-значение
        __it, __bucket_list = list(), list()
        for bucket in self.__htable:
            __it += [(it.get_key(), it.get_value()) for it in bucket]
        return __it

    def _resize(self):  # resize по capacity
        self.__cur_sz *= 2
        old_htable = self.items()
        self.__htable = [[] for i in range(self.__cur_sz)]
        for item in old_htable:
            self.put(item[0], item[1])

    def __str__(self):  # Вывод
        print("buckets: {}, items: {}".format(self.__buckets, self.items()))

    def __contains__(self, item):  # check: in ?
        for i in self.__htable:
            for j in i:
                if j.get_key() == item:
                    return True
        return False
