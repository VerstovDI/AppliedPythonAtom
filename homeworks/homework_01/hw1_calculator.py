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
    if operator == "plus":
        return x + y
    if operator == "minus":
        return x - y
    if operator == "mult":
        return x * y
    if operator == "divide":
        return x / y if y != 0 else None
    return None
    raise NotImplementedError
