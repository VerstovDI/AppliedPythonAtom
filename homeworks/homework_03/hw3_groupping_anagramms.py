#!/usr/bin/env python
# coding: utf-8


def groupping_anagramms(words):
    words_dict = dict()
    res_list = []
    for word in words:
        tmp = ''.join(sorted(word.lower()))
        if tmp in words_dict:
            words_dict.setdefault(tmp, [])
            words_dict[tmp].append(word)
        else:
            words_dict[tmp] = [word]

    for key, value in words_dict.items():
        if len(value) > 1:
            res_list.append(value)
    return res_list
