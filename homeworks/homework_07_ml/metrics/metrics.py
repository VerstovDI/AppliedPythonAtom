#!/usr/bin/env python
# coding: utf-8


import numpy as np


def logloss(y_true, y_pred):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    # y_hat? -> Если y_pred -> probabilities, см. коммент. в конце ф-ии
    if y_true.size != y_pred.size:
        print("Size mismatch error! There will be return -1")
        return
    eps = 1e-15
    pred = np.maximum(eps, y_pred)
    pred_proba = np.minimum(1-eps, pred)
    n = y_true.size
    logsum = np.sum(y_true*np.log(pred_proba)+(1-y_true)*np.log(1-pred_proba))
    loss = (-1.0/n)*logsum
    """
    Т.к. в ф-ле log loss стоит вероятность,то:
    ->Если под y_pred имелась в виду вероятность P,
    то просто подставить в ф-лу log_loss -> ответ:
    ->Выглядеть будет так (p - probability):
    def logloss(y_true, p):
        # size-check
        loss = (-1/n)*(y_true * np.log(p) + (1-y_true)*np.log(1-p))
        return loss
    """
    return loss


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    if y_true.size != y_pred.size:
        print("Size mismatch error! There will be return -1")
        return
    tp_cnt = 0
    for j in range(len(y_true)):
        if y_true[j] == y_pred[j]:
            tp_cnt += 1
    loss = tp_cnt/len(y_true)
    return loss


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    if y_true.size != y_pred.size:
        print("Size mismatch error! There will be return -1")
        return
    types = np.unique(y_true)
    tp_list = [0] * len(types)
    tp_fp_list = np.bincount(y_pred)
    for j in range(0, len(y_true)):
        if y_true[j] == y_pred[j]:
            tp_list[y_true[j]] += 1
    presicion = []
    for _ in range(len(tp_list)):
        presicion.append(tp_list[_]/tp_fp_list[_])
    loss = sum(presicion)/len(presicion)
    """
    Или иначе просто в случае 2-х классов 0-1 аналогично тому,как реализован
    recall (см.ниже). Пройти y_true 0..i сравнив с
    y_pred по confusion matrix
    """
    return loss


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    if y_true.size != y_pred.size:
        print("Size mismatch error! There will be return -1")
        return
    tp, fn = 0, 0
    for j in range(len(y_true)):
        if y_true[j] == y_pred[j] and y_true[j] == 1:
            tp += 1
        if y_true[j] == 1 and y_pred[j] == 0:
            fn += 1
    loss = tp/(tp + fn)
    """
    Соответствует recall_score(y_true, y_pred, average='binary'))
    """
    return loss


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    if y_true.size != y_pred.size:
        print("Size mismatch error! There will be return -1")
        return
    tp, tn = 0, 0
    fp, fn = 0, 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            if y_true[i] == 1:
                tp += 1
            if y_true[i] == 0:
                tn += 1
        else:
            if y_true[i] == 0:
                fp += 1
            if y_true[i] == 1:
                fn += 1
    tpr = tp/(tp+fn)
    fpr = fp/(fp+tn)
    # Т.к. в данном случае tpr-fpr - два числа, то согласно
    # https://dyakonov.org/2017/07/28/ - раздел про auc_roc - получим:
    auc_roc_binary_loss = (1 + tpr - fpr)/2
    return auc_roc_binary_loss
