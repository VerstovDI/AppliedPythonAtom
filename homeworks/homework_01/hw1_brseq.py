#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    s_len = len(input_string)
    if s_len % 2 != 0:  # Если кол-во нечётн. - заведомо False
        return False
    if s_len == 0:  # Если длина строк == 0 ('') - заведомо True
        return True

    if '()' in input_string:
        fl_1 = is_bracket_correct(input_string.replace('()', ''))
        return fl_1

    if '[]' in input_string:
        fl_2 = is_bracket_correct(input_string.replace('[]', ''))
        return fl_2

    if '{}' in input_string:
        fl_3 = is_bracket_correct(input_string.replace('{}', ''))
        return fl_3

    return False
    return NotImplementedError
