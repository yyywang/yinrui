# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2020/4/5.
"""
import matplotlib.pyplot as plt

def progress_bar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 50, fill = '#', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    iteration += 1
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    suffix = suffix + '{0}/{1}'.format(iteration, total)
    # print('\r%s [\033[1;31;32m%s\033[0m] %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    print('\r%s [%s] %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)

    # Print New Line on Complete
    if iteration == total:
        print()

def zip_sort(names, values, reverse=False):
    """
    打包两个数据并排序返回
    :param names: 
    :param values: 
    :param reverse: 是否排序反转
    :return: 
    """
    data = list()
    # 将类别与评分绑定在一起，不然排序后评分对应的类别就乱掉了
    for i in range(len(names)):
        data.append(dict(
            name=names[i],
            value=values[i]
        ))
    data = sorted(data, key=lambda item: item['value'], reverse=reverse)
    resp_names = [item['name'] for item in data]
    resp_values = [item['value'] for item in data]
    return dict(names=resp_names, values=resp_values)

def add_column_label(data, decimals=0):
    """
    为图每一栏添加 label
    :param data: 
    :param decimals: 保留几位小数，默认不保留
    :return: 
    """
    for idx, item in enumerate(data):
        plt.text(item + 0.5, idx-0.3, str(round(item, decimals)), color='black')