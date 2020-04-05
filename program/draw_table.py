# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2020/4/3.
"""
import matplotlib.pyplot as plt
from program.get_data import DataObject
import numpy as np
from program.utils import progress_bar, zip_sort, add_column_label, support_zh


def draw_line_year_category(data_obj):
    """
    2000年之后，每个电影类型下的电影数
    x: 年份
    y: 电影数量
    类型：折线图
    """
    plt.figure()
    years = data_obj.years # 升序排列的年份列表
    categories = data_obj.categories # 所有电影类型
    # 创建存储每年份各类别电影的数量
    # 行为类别，列为年份的二维数组，初始值为0
    dt = np.zeros([len(categories), len(years)], dtype=int)

    # 计算每年各类型电影数量
    for idx in range(data_obj.row_num):
        progress_bar(idx, data_obj.row_num, prefix='计算每年各<类型>电影数量')
        year = data_obj.get_year_of_row(idx)
        dt_y_idx = years.index(year)
        # 一个电影有多个“类别”数据
        row_categories = data_obj.get_category_of_row(idx)
        for category in row_categories:
            dt_x_idx = categories.index(category)
            dt[dt_x_idx][dt_y_idx] += 1

    # 循环一次绘制一条折线
    # 横轴为“年份”，纵轴为“类别数量”
    for idx, category_data in enumerate(dt):
        plt.plot(years, category_data, label=categories[idx])
        plt.legend(loc='upper left') # 显示图例，设置位置为左上

    plt.xlabel('年份')                    # 横轴标签
    plt.ylabel('数量')                    # 纵轴标签
    plt.suptitle('每年电影类型数量')       # 标题

def draw_bar_year_category(data_obj):
    """
    每个年份每个电影类型下的电影数
    x: 年份
    y: 电影数
    类型：条形图
    :return: 
    """
    plt.figure()
    years = data_obj.years # 升序排列的年份列表
    categories = data_obj.categories # 所有电影类型

    # 创建存储每年份各类别电影的数量
    # 行为类别，列为年份的二维数组，初始值为0
    dt = np.zeros([len(categories), len(years)], dtype=int)

    # 计算每年各类型电影数量
    for idx in range(data_obj.row_num):
        progress_bar(idx, data_obj.row_num, prefix='计算每年各<类型>电影数量')
        year = data_obj.get_year_of_row(idx)
        dt_y_idx = years.index(year)
        # 一个电影有多个“类别”数据
        row_categories = data_obj.get_category_of_row(idx)
        for category in row_categories:
            dt_x_idx = categories.index(category)
            dt[dt_x_idx][dt_y_idx] += 1

    # 横轴为“数量”，纵轴为“类别”
    data = zip_sort(categories, np.sum(dt, axis=1))
    plt.barh(data['names'], data['values'])
    add_column_label(data['values'])        # 为每一栏数据添加label
    plt.xlabel('数量')                      # 横轴标签
    plt.suptitle('所有类别电影数量')          # 标题

def draw_bar_country_movie(data_obj):
    """各制片国家/地区的电影数柱状图
    x: 电影数
    y: 制片国家/地区
    """
    plt.figure()
    countries = data_obj.countries # 所有国家
    # 行为国家/地区，该国家/地区的电影数，初始值为0
    dt = np.zeros(len(countries), dtype=int)

    # 计算各国家/地区电影数量
    for idx in range(data_obj.row_num):
        progress_bar(idx, data_obj.row_num, prefix='计算各<制片国家/地区>电影数量')
        temp_countries = data_obj.get_country_of_row(idx)
        # 一个电影有多个制片国家/地区
        for country in temp_countries:
            dt_row_idx = countries.index(country)
            dt[dt_row_idx] += 1

    # 横轴为“数量”，纵轴为“制片国家/地区”
    data = zip_sort(countries, dt, reverse=True, count=10)
    plt.barh(data['names'], data['values']) # 取前10
    add_column_label(data['values'])
    plt.xlabel('数量')                    # 横轴标签
    plt.suptitle('各制片国家/地区电影数量')       # 标题

def draw_pie_country_movie(data_obj):
    """各制片国家/地区电影数量饼图"""
    plt.figure()
    countries = data_obj.countries # 所有国家
    # 各国家/地区的电影数，初始值为0
    dt = np.zeros(len(countries), dtype=int)

    # 计算各国家/地区电影数量
    for idx in range(data_obj.row_num):
        progress_bar(idx, data_obj.row_num, prefix='计算各<制片国家/地区>电影数量')
        temp_countries = data_obj.get_country_of_row(idx)
        # 一个电影有多个制片国家/地区
        for country in temp_countries:
            dt_row_idx = countries.index(country)
            dt[dt_row_idx] += 1

    data = zip_sort(countries, dt, reverse=True)
    # 前5 + 其他
    top5_values = data['values'][:5]
    rest_value = sum(data['values'][5:])
    data_values = top5_values + [rest_value]
    top5_labels = data['names'][:5]
    data_labels = top5_labels + ['其他']

    plt.pie(data_values, labels=data_labels, autopct = '%3.2f%%') #数值保留2位小数
    plt.suptitle('电影制片国家/地区饼图')  # 标题

def draw_bar_category_average_score(data_obj):
    """不同类型电影平均分柱状图
    x: 平均分
    y: 电影类型
    """
    plt.figure()
    categories = data_obj.categories # 所有电影类型
    # 各电影类型的总分、数量，初始值为0
    dt = np.zeros([len(categories), 2], dtype=float)

    # 计算各类型电影总分
    for idx in range(data_obj.row_num):
        progress_bar(idx, data_obj.row_num, prefix='计算各<类型>电影平均分数')
        score = data_obj.get_score_of_row(idx)
        category_list = data_obj.get_category_of_row(idx)
        # 一部电影可能属于多个类型
        for category in category_list:
            dt_row_idx = categories.index(category)
            dt[dt_row_idx][0] += score
            dt[dt_row_idx][1] += 1

    # 计算平均分
    dt = [sum_score / movie_num for sum_score, movie_num in dt]
    # 排序
    data = zip_sort(categories, dt)
    # 横轴为“平均评分”，纵轴为“电影类型”
    plt.barh(data['names'], data['values'])
    add_column_label(data['values'],x=0.1, decimals=2)
    plt.xlabel('评分')                            # 横轴标签
    plt.suptitle('不同类型电影平均分柱状图')        # 标题


def show_all_chart():
    """显示所有图表"""
    plt.show()

if __name__ == '__main__':
    data_obj = DataObject()
    draw_line_year_category(data_obj)
    # draw_bar_year_category(data_obj)
    # draw_bar_country_movie(data_obj)
    # draw_pie_country_movie(data_obj)
    # draw_bar_category_average_score(data_obj)
    support_zh()
    show_all_chart()