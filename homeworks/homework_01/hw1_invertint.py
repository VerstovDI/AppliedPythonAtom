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
    lst = []
    if number < 0:
        fl = True
    else:
        fl = False
    number = abs(number)
    if number == 0:
        return 0
    while number >= 1:
        tmp = number%10
        lst.append(tmp)
        number = number//10
    lst = [str(i) for i in lst]
    res = "".join(lst)
    if fl:
        output_int = -1 * int(res)
        return output_int
    output_int = res
    return output_int

