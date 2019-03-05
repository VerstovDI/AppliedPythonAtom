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
    length = len(input_string)
    if length % 2 != 0:
        return False

    cnt_1 = 0  # Счётчик числа скобок типа '( - )'
    cnt_2 = 0  # Счётчик числа скобок типа '[ - ]'
    cnt_3 = 0  # Счётчик числа скобок типа '{ - }'
    fl_1 = False  # Флаги (cм. далее назначение)
    fl_2 = False
    fl_3 = False

    for item in input_string:
        if item == '(':
            cnt_1 += 1
            fl_1 = True  # Флаг поднят. Встречена открывающая скобка
        elif item == '[':
            cnt_2 += 1
            fl_2 = True  # Далее аналогично
        elif item == '{':
            cnt_3 += 1
            fl_3 = True

        if item == ')':
            if cnt_1 == 0:
                return False
            if fl_1:
                cnt_1 -= 1
            else:
                return False

        if item == ']':
            if cnt_2 == 0:
                return False
            if fl_2:
                cnt_2 -= 1
            else:
                return False

        if item == '}':
            if cnt_3 == 0:
                return False
            if fl_3:
                cnt_3 -= 1
            else:
                return False

    if cnt_1 % 2 != 0 or cnt_2 % 2 != 0 or cnt_3 % 2 != 0:
        return False
    else:
        return True

    return False
