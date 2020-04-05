# -*- coding: utf-8 -*-
"""
  Created by Wesley on 2020/4/1.
"""
from config.config import Config
from program.draw_table import draw_bar_year_category, show_all_chart, draw_line_year_category, draw_bar_country_movie, \
    draw_pie_country_movie, draw_bar_category_average_score
from program.get_data import DataObject
from program.utils import support_zh

if __name__ == '__main__':
    file_path = './data/test/data2000.xlsx'      # 数据文件路径，仅支持 xlsx 格式
    Config.set_data_file(file_path)                 # 配置数据文件
    data_obj = DataObject()                         # 操作数据的对象

    draw_line_year_category(data_obj)               # 各年份各电影类型下的电影数折线图
    draw_bar_year_category(data_obj)                # 各年份各电影类型下的电影数直方图
    draw_bar_country_movie(data_obj)                # 各制片国家/地区的电影数直方图
    draw_pie_country_movie(data_obj)                # 各制片国家/地区电影数量饼图
    draw_bar_category_average_score(data_obj)       # 不同类型电影平均分直方图

    support_zh()                                    # 支持显示中文
    show_all_chart()                                # 绘制所有图表