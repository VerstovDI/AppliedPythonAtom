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
    tmp_str = input_string[::-1]
    if input_string == tmp_str:
        return True
    else:
        return False
