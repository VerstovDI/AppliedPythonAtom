#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
    raise NotImplementedError
    if operator == "plus":
        return obj_1+obj_2
    if operator == "minus":
        return obj_1-obj_2
    if operator == "mult":
        return obj_1*obj_2
    if operator == "divide":
        return obj_1/obj_2 if obj_2 != 0 else None
    return None
