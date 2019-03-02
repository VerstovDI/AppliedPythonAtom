#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    raise NotImplementedError
    list = []
    if number < 0:
        fl = True
    else:
        fl = False
    number = abs(number)
    if number == 0:
        return 0
    while number >= 1:
        tmp = number%10
        list.append((tmp))
        number = number//10
    list = [str(i) for i in list]
    res = "".join(list)
    if fl:
        return -1*int(res)
    return int(res)
