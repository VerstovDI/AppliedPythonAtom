#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    _prev, _next = None, None
    _cur = head
    while _cur is not None:
        _next = _cur.next_node
        _cur.next_node = _prev
        _prev = _cur
        _cur = _next
    return _prev
