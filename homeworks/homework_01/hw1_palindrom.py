#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    '''
    Метод проверяющий строку на то, является ли
    она палиндромом.
    :param input_string: строка
    :return: True, если строка являестя палиндромом
    False иначе
    '''
    raise NotImplementedError
    tmp_str = str[::-1]
    if str == tmp_str:
        return True
    else:
        return False
    return False
