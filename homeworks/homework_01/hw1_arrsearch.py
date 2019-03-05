#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    buf_d = {}
    for cnt in range(0, len(input_list)):
        buf_d[input_list[cnt]] = cnt
    t = 0
    for item in input_list:
        temp = buf_d.get(n - item)
        if temp and temp and n - item != item:
            return tuple([t, temp])
        t += 1
    return None
