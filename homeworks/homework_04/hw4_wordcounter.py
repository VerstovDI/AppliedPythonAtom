#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Pool, Queue, cpu_count
import os


def word_counter(file) -> int:  # Возвращает кол-во слов в текущем файле
    f = open(file, "r",  encoding="utf8")
    words = f.read()
    f.close()
    return len(words.split())


def built_queue(path_to_dir: str):  # Возвращает multiprocessing.Queue()
    shared_queue = Queue()
    files_list = os.listdir(path_to_dir)
    for file in files_list:
        shared_queue.put(file)
    return shared_queue


def word_count_inference(path_to_dir):  # Многопроцессный счётчик слов
    """
    Метод, считающий количество слов в каждом файле из директории
    и суммарное количество слов.
    Слово - все, что угодно через пробел, пустая строка "" словом не считается,
    пробельный символ " " словом не считается. Все остальное считается.
    Решение должно быть многопроцессным. Общение через очереди.
    :param path_to_dir: путь до директории с файлами
    :return: словарь, где ключ - имя файла, значение - число слов +
    специальный ключ "total" для суммы слов во всех файлах
    """
    res_dict = {"total": 0}  # Результирующий словарь
    total_cnt = 0  # Суммарное число слов во всех файлах

    q = built_queue(path_to_dir)  # Создаём очередь из файлов директории

    # Запустим n процессов(cpu_count()-кол-во ядер исполняющего устройства)
    p = Pool(processes=cpu_count())
    with p:
        while not q.empty():
            cur_file = q.get()
            string = path_to_dir + cur_file
            cnt = p.apply(word_counter, (path_to_dir + "/" + cur_file,))
            total_cnt += cnt
            res_dict.update({cur_file: cnt})

    p.close()
    p.join()
    res_dict.update({"total": total_cnt})
    return res_dict
