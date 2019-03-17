#!/usr/bin/env python
# coding: utf-8
import collections


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.__activity_list = collections.deque()

    def register_event(self, user_id, time):
        self.__activity_list.appendleft((time, user_id))
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        return None

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]),
        совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        """
        Словарь query_dict: key - user_id, value - числов событий из интервала
        """
        activity_count = 0
        query_dict = {}
        for item in self.__activity_list:
            if time - self.FIVE_MIN < item[0] <= time:
                if item[1] in query_dict:
                    query_dict[item[1]] = query_dict.get(item[1]) + 1
                else:
                    query_dict[item[1]] = 1
        for key, value in query_dict.items():
            if query_dict.get(key) == count:
                activity_count += 1
        return activity_count
